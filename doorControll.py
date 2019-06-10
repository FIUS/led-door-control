import requests
import threading

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
        if doorIsOpen:
            requests.post("http://192.168.212.183?doorOpen")
        else:
            requests.post("http://192.168.212.183?doorClosed")
    print(doorIsOpen)

checkDoor()