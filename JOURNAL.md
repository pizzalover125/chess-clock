### May 15: (60 min)
- thought of this project a long time ago
- i wanted to build an open source chess clock
- then I thought, why make the chess clock also work as a rubiks cube timer?
- thats when this idea popped in my head
- going to make this basic and cheap, so a 4 point project
- start off w schematic
- added xiao from https://hackpad.hackclub.com/resources
- going to be making the following thing:

<img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/e0113383-66a4-4f6d-a145-6c65cbc159f8" />

- changing MCU to ESP32C3 bc i can create web app for chess clock!
- using low-profile switches to potentially make this folding
- finished schematic

<img width="518" height="491" alt="image" src="https://github.com/user-attachments/assets/bd538069-f70a-49a3-8f91-5d8ec7466044" />

- assigned footprints
- looked at 0.96" OLED on my desk and realized two numbers would be too small on that
- was thinking about 2 OLEDs but the Xiao has 1 i2c bus only
- guess we are switching to Pi Pico
- choc v2 switches have same travel distance but 4mm lower height than gateron
- did some research; choosing kalih PG1350

<img width="750" height="385" alt="image" src="https://github.com/user-attachments/assets/b089cffd-c9ff-4bed-becd-609c8902e000" />

- time to route

<img width="1006" height="486" alt="image" src="https://github.com/user-attachments/assets/7867a120-b394-43f8-87d4-baf68dad36e9" />

- ez routing
- had them flipped; had to route again
- added 3d models!
- ok im not going to make it round so its easier to CAD
- mounting holes took forever for some reason but I got it!

<img width="950" height="510" alt="image" src="https://github.com/user-attachments/assets/6f307050-94bd-4a88-b7f6-501f6963bea4" />

- created logo

<img width="148" height="65" alt="text-1778898806176" src="https://github.com/user-attachments/assets/57540851-d8f9-48f7-b8d0-e8615763d6ff" />

- tried to add texture but it didn't end up working
- ok i just realized the way i envisioned it is completely wrong
- i think i'll switch this to a cubing timer cause this is the proper thing for that

# 5/15 part 2: 45 minutes
- wanted to build cubing timer in person cause i have all the parts!
- finished placing and wiring super quickly

[will add image here; took photo on phone]

- will vibecode software something up super fast
- ok code generated but i don't have a cable; let me look for one
- found cable
- tried on my Microsoft Surface; didn't work
- tried another cable
- tried to connect to Mac; didn't work
- idk this is so weird; i've tried 2 different cables, 2 different OSes, and 3 different Picos and it never shows up on the computer.
- ok turns out the cables are power-only; not data; i need to buy a new cable
- oh well, will try tomorrow

# 5/16: 55 minutes
- okay i tried a THIRD cable and it STILL DOESN'T WORK
- I need to buy another cable later
- I'll work on PCB
- finished w schematic bc its super ez
- i want to use 1.3" OLED cause its bigger so easier to see
- downloaded the footprint + schematic from SNAPEDA
- updated schematic

<img width="1248" height="501" alt="image" src="https://github.com/user-attachments/assets/b7f07b0b-41b5-4a73-ac04-25c19f0b209f" />

- idk where to put MCU
- if I put it under then OLED pins would hit the MCU
- ok someone told me I can put it under
- found 3D model of OLED in GrabCAD and imported it
- downloaded Xiao RP2040 model from GrabCAD and imported it
- routed everything
- was going to move the mounting holes but decided not to
- ONSHAPE time!

<img width="1371" height="659" alt="image" src="https://github.com/user-attachments/assets/61dc47b7-db60-4894-9601-5c18b6fc022a" />

- nvm, i wanted to change it just to be safe
  
<img width="467" height="315" alt="image" src="https://github.com/user-attachments/assets/a7020b1a-d2fe-4c84-ba2f-30946ba0b75b" />

- rounded the corners and routed! now time for CAD

<img width="731" height="469" alt="image" src="https://github.com/user-attachments/assets/3144b1c8-f2c2-4245-be2c-568f3ff345c8" />

- added holes + the rectangle itself

<img width="882" height="597" alt="image" src="https://github.com/user-attachments/assets/fa774078-661e-41d1-ade7-dd036b48b9de" />

- tried to add top plate but i think its better to just have backplate
- printed the PCB IRL!
- going to print the backplate to get a feel on what this is going to be like

<img width="4032" height="3024" alt="image" src="https://github.com/user-attachments/assets/9e9c9ea2-bcee-4e27-bd25-c2c4acd9d142" />

- prined backplate out; pretty good fit!

### 5/23: 1 hour
- time for The Great Reset
- im starting over designs
- i want to rival the industry standard cubing timer
- browsing https://speedcubeshop.com/collections/timers-mats?srsltid=AfmBOopexjruzZxA7FfL3zBg9GQAVpsEH9dB6mVJ9Nki_ceUBmzxgrYh for inspo + ideas
- bro no way there is an AI speedcubing timer; this is wild
- ok im thinking to use capacitve touch pad instead of switches to not make this a hackpad
- watching https://www.youtube.com/watch?v=tTMsbL0eH_M to learn
- that video wasn't helpful; watching https://www.youtube.com/watch?v=42jUcqwKIw8
- that vid didn't have much so watching this https://www.youtube.com/watch?v=mWR9Q_pTagw
- ok capacitve touch is very hard to implement in such a large area such as a palm
- lots of chance for missed calls
- did some research and a grand total of 0 people have made an open source cubing timer
- soooo this is the first! thats kind of cool

<img width="496" height="251" alt="image" src="https://github.com/user-attachments/assets/f991011a-7c6c-40e6-8697-84e4f0002857" />

- okay i might use this type of design with infared/distance sensors on each side to determine
- mx switches aren't good bc they are designed for fingers, not hands
- ok this is a hard project
- wait i found [https://github.com/amadensor/cube-timer/tree/main/pcb/cube_timer](https://github.com/tibordp/cube-timer)
- ok mine is the first PCB + case; the project is just an ESP32 on a breadboard
- going to read https://ww1.microchip.com/downloads/en/DeviceDoc/40001946A.pdf
- ok idk if this is possible even 

### Jun 10 (2.5 hours)
- rebranding this to be a chess clock again
- planning to use 8-segment clock displays like this one:

<img width="1024" height="768" alt="image" src="https://github.com/user-attachments/assets/01e729d2-ef02-4143-a375-3601516b0e82" />

- thats what these clocks use:

<img width="191" height="143" alt="image" src="https://github.com/user-attachments/assets/20c3415b-d7c0-4b0c-b40e-fdee72febdc2" />

- going to also use mx switches cause hey are used in:

<img width="276" height="183" alt="image" src="https://github.com/user-attachments/assets/da560400-eb0f-454f-aaa3-49dcd3f03d11" />

- time to import all CAD models
- ah i can only find 1.2" not 0.56"
- i imported the mx switch
- time to decide what MCU
- i think ill use RP2040-zero
- wait nvm its hard to mount?
- i might use pico just because its easier to mount
- imported the pico!
- apparently i need beveled face to make it have good viewing angles
- watching https://www.youtube.com/watch?v=eApyyNPppaY

<img width="590" height="468" alt="image" src="https://github.com/user-attachments/assets/8f8208d8-e0c8-499c-a5b6-ee56ed98e7c5" />

- starting to look like a chess clock!
- did some more research on how to mount a mx switch
- i need a 14x14mm cutout with 1.5mm plate size

<img width="648" height="395" alt="image" src="https://github.com/user-attachments/assets/0f52844a-a498-48bd-9fa7-35b408e96f9c" />

- looks great!
- ill add pico mounting now

<img width="940" height="343" alt="image" src="https://github.com/user-attachments/assets/5c0409d1-6cbf-4a40-ab2a-6180264eb85d" />

- okay turns out every OLED is different
- so ig ill have to redo some dimensions
- also i might make it bigger

- ok found models for the 0.56 i2c 7-segment display!
- going to use that because its better

<img width="1024" height="586" alt="image" src="https://github.com/user-attachments/assets/8883df91-888a-4f60-a155-62bc183d6d64" />

- using this image
- annoying i need to covnert to mm

<img width="993" height="488" alt="image" src="https://github.com/user-attachments/assets/6e105b7e-b757-4066-8426-5e670031ae4f" />

- voila!
- time to add screen cutout

<img width="850" height="458" alt="image" src="https://github.com/user-attachments/assets/0419dc0a-494a-4753-a2f2-927db2587431" />

- looks like a chess clock
- will later figure out how to assemble

### Jun 15 (3 hours)
- i was away from my house for a couple of days
- time to get back on this project

<img width="1238" height="611" alt="image" src="https://github.com/user-attachments/assets/3d6369da-7720-4cc7-9f3c-4a258a74607c" />

- added tolerances

<img width="740" height="353" alt="image" src="https://github.com/user-attachments/assets/f4cbe432-88b3-45f3-a78f-0fe899530d4e" />

- added a border!
- it looks kinda weird ngl

<img width="714" height="429" alt="image" src="https://github.com/user-attachments/assets/e35a5a20-db87-4987-befc-5857d7a027a5" />

- added keycaps and colors! looks very cool

<img width="549" height="644" alt="image" src="https://github.com/user-attachments/assets/e62e6b37-a415-4e7e-a8d4-78e9f8741de2" />

- made it assembleable

<img width="467" height="363" alt="image" src="https://github.com/user-attachments/assets/26ea892a-684f-4013-885f-12ffd73a8078" />

- remade the assembly
- ill make a render cause why not
- technically i am done with the CAD
- but idk if i want to make a PCB
- cause it needs to arrive in time

<img width="569" height="443" alt="image" src="https://github.com/user-attachments/assets/7509eb5b-aca7-41cf-89a2-090ddfbddbb7" />

- ok made that
- apparently M1 screws don't work with 3d printed stuff
- so ill need M2
- made it M2
- ok im working super slow now idk why

- new session at night
- i added chamfer to add M3 holes!

<img width="591" height="358" alt="image" src="https://github.com/user-attachments/assets/252aa259-8b5a-4279-8413-a03a34368021" />

- the only major thing left other than firmware is how im going to assemble this
- i dont want to make a PCB cause i want it to be done in time
- PCB also not required?
- i could use a breadboard
- ok ill figure this out tmrw
- will create wiring diagram!

<img width="1437" height="563" alt="image" src="https://github.com/user-attachments/assets/c1aa0e42-26b6-47b1-a7eb-fdcd2e3f3d11" />

- kinda basic because wiring diagram is kinda basic
