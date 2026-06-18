from machine import Pin, I2C
import time
from adafruit_ht16k33.segments import Seg7x4
 
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
display = Seg7x4(i2c)
 
left_button = Pin(4, Pin.IN, Pin.PULL_UP)
right_button = Pin(5, Pin.IN, Pin.PULL_UP)
 
left_time = 180000
right_time = 180000
 
active = None
 
last_update = time.ticks_ms()
last_left_press = 0
last_right_press = 0
 
def fmt(ms):
    if ms < 0:
        ms = 0
    s = ms // 1000
    return f"{s // 60:02d}{s % 60:02d}"
 
while True:
    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, last_update)
    last_update = now
 
    if active == 0:
        left_time -= elapsed
        if left_time <= 0:
            left_time = 0
            active = None
 
    elif active == 1:
        right_time -= elapsed
        if right_time <= 0:
            right_time = 0
            active = None
 
    if not left_button.value():
        if time.ticks_diff(now, last_left_press) > 200:
            last_left_press = now
            if active is None:
                active = 1
            elif active == 0:
                active = 1
 
    if not right_button.value():
        if time.ticks_diff(now, last_right_press) > 200:
            last_right_press = now
            if active is None:
                active = 0
            elif active == 1:
                active = 0
 
    if active == 0:
        display.print(fmt(left_time))
    elif active == 1:
        display.print(fmt(right_time))
    else:
        display.print(fmt(left_time))
 
    display.colon = True
    time.sleep_ms(10)
