import keyboard
import pyautogui
import time
import sys

got_trigger = False
trigger_key = ""
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
while True:
    cps_input = input("Bitte eine Zahl eingeben: ")
    if cps_input.isdigit():
        cps = int(cps_input)
        break
    else:
        print("❌ Ungültige Eingabe! Bitte gib nur Zahlen ein.")
print("Drücke um den tigger zu ändern ")

def on_press(event):
    global trigger_key
    global got_trigger
    if got_trigger:
        return
    trigger_key = event.name
    print(trigger_key)
    got_trigger = True
def start_keylogger():
    keyboard.on_press(on_press)

#pyautogui.PAUSE = 0
running = False
start_keylogger()
while not got_trigger:
    time.sleep(0.1)
while True:
    if keyboard.is_pressed(trigger_key):
        if running:
            running = False
            print(f"Autoclicker stopped. Press {trigger_key} to start.")
            time.sleep(1)
        elif not running:
           running = True
           print(f"Autoclicker started. Press {trigger_key} to stop.")
           time.sleep(1)
    if running:
       pyautogui.click()
       time.sleep(1 / cps)