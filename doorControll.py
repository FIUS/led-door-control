
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
        dishwasherIP = os.environ['LED_DISHWASHER']
        if doorIsOpen:
            print("Door was opened")
            doCheckedPostRequestWithBody("http://"+ceilingIP+"/animationType",1)
            doCheckedPostRequest("http://"+dishwasherIP+"?doorOpen")
        else:
            print("Door was closed")
            doCheckedPostRequestWithBody("http://"+ceilingIP+"/animationType",0)
            doCheckedPostRequest("http://"+dishwasherIP+"/?doorClosed")

def doCheckedPostRequest(url):
    try:
        requests.post(url)
    except Exception as e:
        print("Error in post: ", e)

def doCheckedPostRequestWithBody(url,state):
    try:
        requests.post(url, json={"type": state})
    except Exception as e:
        print("Error in post: ", e)
        
while True:
    checkDoor()
    time.sleep(5)
