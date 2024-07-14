import threading
from tkinter import Tk, Label, Entry, Button
from pynput import keyboard
from modules.clicker import AutoClicker
from modules.macro import Macro

auto_clicker = None

def start_clicker_with_interval(interval):
    global auto_clicker
    if auto_clicker is not None:
        auto_clicker.stop()
    auto_clicker = AutoClicker(delay=float(interval))
    
    clicker_thread = threading.Thread(target=auto_clicker.start)
    clicker_thread.start()

def on_press(key):
    try:
        if key == keyboard.Key.f4:
            stop_program()
    except AttributeError:
        pass

def stop_program():
    global auto_clicker
    if auto_clicker is not None:
        auto_clicker.stop()
    return False  # To stop the listener

def set_interval():
    interval = interval_entry.get()
    start_clicker_with_interval(interval)

def stop_clicking():
    stop_program()

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Create the GUI
root = Tk()
root.title("Auto Clicker & Macro")

Label(root, text="Interval (seconds):").grid(row=0, column=0)
interval_entry = Entry(root)
interval_entry.grid(row=0, column=1)

set_button = Button(root, text="Set Interval", command=set_interval)
set_button.grid(row=1, column=0)

stop_button = Button(root, text="Stop Clicking", command=stop_clicking)
stop_button.grid(row=1, column=1)

root.mainloop()
listener.stop()
