from pynput.mouse import Button, Controller
import time

class AutoClicker:
    def __init__(self, delay=0.1):
        self.mouse = Controller()
        self.delay = delay
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.mouse.click(Button.left)
            time.sleep(self.delay)

    def stop(self):
        self.running = False
