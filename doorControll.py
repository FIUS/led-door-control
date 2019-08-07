
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
    except Exception as e:
        print("Error in checkDoor: ", e)

def setDoorOpen(state):
    global doorIsOpen

    if not(state == doorIsOpen):
        doorIsOpen = state
        ceilingIP = os.environ['LED_CEILING']
        if doorIsOpen:
            print("Door was opened")
            doCheckedPostRequest("http://"+ceilingIP+"?doorOpen")
            doCheckedPostRequest("http://led-dishwasher?doorOpen")
        else:
            print("Door was closed")
            doCheckedPostRequest("http://"+ceilingIP+"?doorClosed")
            doCheckedPostRequest("http://led-dishwasher?doorClosed")

def doCheckedPostRequest(url):
    try:
        requests.post(url)
    except Exception as e:
        print("Error in post: ", e)
        
while True:
    checkDoor()
    time.sleep(5)
