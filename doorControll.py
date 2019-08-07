
#!/usr/bin/env -S python3 -u

import requests
import os
import time

doorIsOpen = False

def checkDoor():
    try:
        r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php")
        if r.text == "open":
            setDoorOpen(True)
        else:
            setDoorOpen(False)
    except e:
        print("Error: " + str(e))

def setDoorOpen(state):
    global doorIsOpen

    if not(state == doorIsOpen):
        try:
            doorIsOpen = state
            ceilingIP = os.environ['LED_CEILING']
            if doorIsOpen:
                print("Door was opened")
                requests.post("http://"+ceilingIP+"?doorOpen")
                requests.post("http://led-dishwasher?doorOpen")
            else:
                print("Door was closed")
                requests.post("http://"+ceilingIP+"?doorClosed")
                requests.post("http://led-dishwasher?doorClosed")
        except e:
            print("Error: " + str(e))

while True:
    checkDoor()
    time.sleep(5)
