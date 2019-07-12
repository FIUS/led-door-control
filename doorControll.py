#!/usr/bin/env -S python3 -u

import requests
import os
import time

doorIsOpen = False

def checkDoor():
    r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php", timeout=3)
    try:
        if r.text == "open":
            setDoorOpen(True)
        else:
            setDoorOpen(False)
    except:
        print("Error")

def setDoorOpen(state):
    global doorIsOpen

    if not(state == doorIsOpen):
        try:
            doorIsOpen = state
            ceilingIP = os.environ['LED_CEILING']
            if doorIsOpen:
                print("Door was opened")
                requests.post("http://"+ceilingIP+"?doorOpen", timeout=5)
            else:
                print("Door was closed")
                requests.post("http://"+ceilingIP+"?doorClosed", timeout=5)
        except:
            print("Error")

while True:
    checkDoor()
    time.sleep(5)
