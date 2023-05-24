import os
from time import sleep
from sh import bluetoothctl
from gpiozero import LightSensor

PHONE_MAC = os.environ['PHONE_MAC']
ldr = LightSensor(4)
tries = 0

while True:
    ldr.wait_for_light()
    print("\nDoor opened. Detecting who...")

    try:
        bl: str = bluetoothctl("connect", PHONE_MAC)
        success = True if bl.find("uccessful") != -1 else False

        # blootooth also connected => I opened the door
        if success:
            tries = 0
            print("Yash opened the door")
            sleep(10) # sleep ten-seconds as I wont re-enter so soon
    except:
        # bluetooth could not connect / threw error => I didn't open the door
        tries += 1
        print("Stranger")

    if tries > 10:
        # door may be left open or spam
        sleep(30)

    if tries > 30:
        # door definitely left open
        # shout close the door
        pass
