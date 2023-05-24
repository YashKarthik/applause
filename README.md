# applause

Will play "main character music" when I (and only I) walk in through the main door.

- Detect main door state:
    - ~~Checking door open/close state using LDR (laser tripwires basicall), might use something else
    later.~~
    - Using LDR, but not a full-blown laser tripwire circuit. The LDR will be stuck to the top of
    the door facing the door frame. So when the door is closed, ldr will read 0. When the door is
    opened, it reads non-zero (ambient light)

- Detect who opened door:
    - When the door is opened, try to connect bluetooth to my phone, if it connects, then I opened the door.
    - I tested it out and usually when the device connects, my phone is in range.
    - I tried using RSSI signal strength to estimate distance, but the RSSI values were too
    unreliable.

- Play "main character" music (lol):
    - Bluetooth speaker? Or Alexa.
