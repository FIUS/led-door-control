import requests
import threading
import os

doorIsOpen = False


def checkDoor():
    threading.Timer(5.0, checkDoor).start()
    r = requests.get("http://fius.informatik.uni-stuttgart.de/isOpen.php")

    if r.text == "open":
        setDoorOpen(True)
    else:
        setDoorOpen(False)


def setDoorOpen(state):
    global doorIsOpen

    if not(state == doorIsOpen):
        doorIsOpen = state
        ceilingIP = os.environ['LED_CEILING']
        if doorIsOpen:
            requests.post("http://"+ceilingIP+"?doorOpen")
        else:
            requests.post("http://"+ceilingIP+"?doorClosed")
    print(doorIsOpen)


checkDoor()
