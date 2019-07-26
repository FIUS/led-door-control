import requests
import os
import time

doorIsOpen = False

def checkDoor():
    r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php")
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
                requests.post("http://"+ceilingIP+"?doorOpen")
                requests.post("http://led-dishwasher?doorOpen")
            else:
                requests.post("http://"+ceilingIP+"?doorClosed")
                requests.post("http://led-dishwasher?doorClosed")
        except:
            print("Error")
    print(doorIsOpen)


while True:
    checkDoor()
    time.sleep(5)
