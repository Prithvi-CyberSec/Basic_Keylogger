import os

def ensure_log_dir():
    if not os.path.exists("logs"):
        os.makedirs("logs")
