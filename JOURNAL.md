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
