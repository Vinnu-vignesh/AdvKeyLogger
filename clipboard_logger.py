# It's used to get clipboard value and store in a file...
import time
import pyperclip
import os

LOG_FILE = "logs/clipboard.txt"

def startClipboard():
    if not os.path.exists("logs"):
        os.mkdir("logs")

    recentValue = ""
    while True:
        currentValue = pyperclip.paste()
        if recentValue != currentValue:
            recentValue = currentValue
        with open(LOG_FILE, "a") as f:
            f.write(f"[{time.ctime()}] - Copied : {recentValue}\n")

        try:
            time.sleep(5)
        except KeyboardInterrupt:
            pass
