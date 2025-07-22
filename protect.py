import psutil

suspicious_keywords = ["keylogger", "pynput", "stealer", "logger", "rat"]

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        info = proc.info
        command = " ".join(info['cmdline']) if info['cmdline'] else ''
        for keyword in suspicious_keywords:
            if keyword.lower() in command.lower():
                print(f"[!] Suspicious process detected: {info['name']} (PID: {info['pid']})")
                print(f"    Command: {command}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
