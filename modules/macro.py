from pynput.keyboard import Controller
import time

class Macro:
    def __init__(self):
        self.keyboard = Controller()

    def run(self, macro_file):
        with open(macro_file, 'r') as file:
            for line in file:
                command, arg = line.strip().split(' ')
                if command == 'type':
                    self.type_text(arg)
                elif command == 'wait':
                    self.wait(float(arg))

    def type_text(self, text):
        for char in text:
            self.keyboard.type(char)
            time.sleep(0.05)

    def wait(self, duration):
        time.sleep(duration)
