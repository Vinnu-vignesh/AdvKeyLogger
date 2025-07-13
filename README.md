# AdvKeyLogger
It's actually a keylogger written in python, which can capture keystrokes, clipboard text, and screenshots.

# 🛡️ Advanced Keylogger (Linux-Compatible)

An advanced keylogger tool designed for **Linux systems**, capable of capturing:
- Keystrokes
- Clipboard content
- Screenshots (via `mss`)
- Daily automated report via email (ZIP file)

---

## ⚙️ Features

- ✅ Logs every keystroke into a timestamped file
- 📋 Tracks clipboard content every 5 seconds
- 📸 Captures screenshots periodically (default: every 60s)
- 📧 Sends a zipped report (daily) to your configured email
- 🔄 Runs all modules simultaneously using threads
- 🖥️ Automatically starts on system boot via `systemd` or `cron`
