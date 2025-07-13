# Used to capture screenshots for every 1 min...
import os
import time
from datetime import datetime

def start_screenshot_capture(interval=60):
    if not os.path.exists("logs/screenshots"):
        os.makedirs("logs/screenshots")

    while True:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"logs/screenshots/screenshot_{timestamp}.png"
        os.system(f"scrot {filename}") # uses system call with scrot tool to get screenshots for systems like Wayland.
        try:
            time.sleep(interval)
        except KeyboardInterrupt:
            pass
