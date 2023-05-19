import os
from sh import bluetoothctl

PHONE_MAC = os.environ['PHONE_MAC']

bl: str = bluetoothctl("connect", PHONE_MAC)
success = True if bl.find("uccessful") != -1 else False
print(success)
