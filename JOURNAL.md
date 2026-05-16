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
