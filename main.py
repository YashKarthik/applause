import os
from sh import bluetoothctl
from gpiozero import LightSensor

PHONE_MAC = os.environ['PHONE_MAC']
ldr = LightSensor(4)

ldr.wait_for_dark()
print("Dark")
bl: str = bluetoothctl("connect", PHONE_MAC)
success = True if bl.find("uccessful") != -1 else False

# tripwire was broker => door was opened
# blootooth also connected => I opened the door

if success:
    print("Me")
