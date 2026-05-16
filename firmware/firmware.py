# ─────────────────────────────────────────────────────────────────────────────
#  Cubing Timer — Raspberry Pi Pico  (CircuitPython)
#  Save this file as  code.py  in the CIRCUITPY drive root.
#
#  Wiring
#  ──────
#  SSD1306 OLED  SDA → GP0   SCL → GP1   (I2C address 0x3C)
#  Button A      GP16  (left / reset)     pin → GND
#  Button B      GP17  (right)            pin → GND
#  Internal pull-ups used — no external resistors needed.
#
#  Required libraries  (copy to CIRCUITPY/lib/)
#  ─────────────────────────────────────────────
#  From the Adafruit CircuitPython Bundle (https://circuitpython.org/libraries):
#    adafruit_displayio_ssd1306.mpy
#    adafruit_display_text/          (folder)
#    adafruit_bus_device/            (folder)
#  bitmaptools is built-in to CircuitPython 7+ — nothing to install.
#
#  Workflow
#  ────────
#  1. Hold A + B  →  "READY / release to start"
#  2. Release both  →  timer starts counting
#  3. Press A + B  →  timer stops, time frozen on screen
#  4. Release both
#  5. Hold A alone 3 s  →  progress bar fills → resets to 0.00
#  6. Repeat
# ─────────────────────────────────────────────────────────────────────────────

import board
import busio
import displayio
import terminalio
import bitmaptools
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from digitalio import DigitalInOut, Direction, Pull
import time

# ── Hardware ──────────────────────────────────────────────────────────────────

displayio.release_displays()  # safe restart after soft-reset

i2c = busio.I2C(scl=board.GP1, sda=board.GP0, frequency=400_000)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.auto_refresh = False   # we call display.refresh() manually

btn_a = DigitalInOut(board.GP16)   # left / reset
btn_a.direction = Direction.INPUT
btn_a.pull = Pull.UP

btn_b = DigitalInOut(board.GP17)   # right
btn_b.direction = Direction.INPUT
btn_b.pull = Pull.UP

# ── Display layout ────────────────────────────────────────────────────────────
#
#   ┌─────────────────────────────────┐  y=0
#   │                                 │
#   │          12.34  (2× font)       │  centred ~y=22
#   │                                 │
#   │    hold A+B to ready  (1×)      │  centred ~y=46
#   │  ██████████░░░░░░░░░░░░░░░░░░░  │  progress bar y=57
#   └─────────────────────────────────┘  y=63

root = displayio.Group()
display.root_group = root

# Large timer readout
time_lbl = label.Label(
    terminalio.FONT,
    text="0.00",
    color=0xFFFFFF,
    scale=2,
)
time_lbl.anchor_point = (0.5, 0.5)
time_lbl.anchored_position = (64, 22)

# Small status / hint line
hint_lbl = label.Label(
    terminalio.FONT,
    text="hold A+B to ready",
    color=0xFFFFFF,
    scale=1,
)
hint_lbl.anchor_point = (0.5, 0.5)
hint_lbl.anchored_position = (64, 46)

# Progress bar (128 × 6 px, 2-colour bitmap)
BAR_H   = 6
BAR_Y   = 57
bar_bmp = displayio.Bitmap(128, BAR_H, 2)
bar_pal = displayio.Palette(2)
bar_pal[0] = 0x000000   # off / background
bar_pal[1] = 0xFFFFFF   # on  / foreground
bar_tg = displayio.TileGrid(bar_bmp, pixel_shader=bar_pal, x=0, y=BAR_Y)

root.append(time_lbl)
root.append(hint_lbl)
root.append(bar_tg)

# ── Helpers ───────────────────────────────────────────────────────────────────

def ms_to_str(ms):
    """Format milliseconds → 'SS.ff' or 'M:SS.ff'."""
    t = ms / 1000.0
    if t < 60:
        return "{:05.2f}".format(t)        # "03.47"
    m = int(t) // 60
    s = t - m * 60
    return "{}:{:05.2f}".format(m, s)     # "1:03.47"


def set_bar(fill_px):
    """Draw a filled rectangle of fill_px pixels in the progress bar."""
    fill_px = max(0, min(128, int(fill_px)))
    if fill_px > 0:
        bitmaptools.fill_region(bar_bmp, 0, 0, fill_px, BAR_H, 1)
    if fill_px < 128:
        bitmaptools.fill_region(bar_bmp, fill_px, 0, 128, BAR_H, 0)


def render(time_text, hint_text="", bar_px=0):
    """Single point of truth for screen updates."""
    time_lbl.text = time_text
    hint_lbl.text = hint_text
    set_bar(bar_px)
    display.refresh()

# ── State machine ─────────────────────────────────────────────────────────────

IDLE    = 0
READY   = 1
RUNNING = 2
STOPPED = 3

RESET_HOLD_S     = 3.0    # seconds A must be held to reset
DISPLAY_INTERVAL = 0.04   # seconds between refreshes while running (~25 fps)

state            = IDLE
start_time       = 0.0
final_ms         = 0
reset_hold_start = None
waiting_release  = False   # True while waiting for buttons up after stopping
last_display     = 0.0

render(ms_to_str(0), "hold A+B to ready")

# ── Main loop ─────────────────────────────────────────────────────────────────

while True:
    now  = time.monotonic()
    a    = not btn_a.value    # True = pressed (active-low)
    b    = not btn_b.value
    both = a and b

    # ── IDLE: sit quietly until both buttons are held ─────────────────────────
    if state == IDLE:
        if both:
            state = READY
            render("READY", "release to start")

    # ── READY: wait for full release, then start clock ────────────────────────
    elif state == READY:
        if not a and not b:
            start_time   = time.monotonic()
            last_display = start_time
            state        = RUNNING
            render("0.00")          # clear hint, show zeroed time

    # ── RUNNING: update display each interval; stop on both held ──────────────
    elif state == RUNNING:
        elapsed_ms = int((now - start_time) * 1000)

        if now - last_display >= DISPLAY_INTERVAL:
            render(ms_to_str(elapsed_ms))
            last_display = now

        if both:
            final_ms        = elapsed_ms
            state           = STOPPED
            waiting_release = True
            render(ms_to_str(final_ms), "hold A to reset")

    # ── STOPPED: show final time; A held 3 s resets ───────────────────────────
    elif state == STOPPED:

        if waiting_release:
            # Ignore input until both buttons are physically released
            if not a and not b:
                waiting_release  = False
                reset_hold_start = None

        else:
            if a and not b:
                # A is being held — track duration
                if reset_hold_start is None:
                    reset_hold_start = now

                held = now - reset_hold_start

                if held >= RESET_HOLD_S:
                    # ── RESET ──────────────────────────────────────────────
                    final_ms         = 0
                    state            = IDLE
                    reset_hold_start = None
                    render(ms_to_str(0), "hold A+B to ready")

                elif now - last_display >= DISPLAY_INTERVAL:
                    # Animate the progress bar while holding
                    render(
                        ms_to_str(final_ms),
                        "hold A to reset",
                        bar_px=128 * held / RESET_HOLD_S,
                    )
                    last_display = now

            else:
                # A released before 3 s — cancel reset, restore clean display
                if reset_hold_start is not None:
                    reset_hold_start = None
                    render(ms_to_str(final_ms), "hold A to reset")

    time.sleep(0.01)
