import keyboard
import time
import sys
import pyautogui
import os
import subprocess


anzahl = 20
time.sleep(5)
def sleapy():
    time.sleep(5)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    print("Programm gestartet. Drücke 'k' um sofort zu stoppen.")

    try:
        while True:
            # Überprüfen, ob Taste 'k' gedrückt wurde
            if keyboard.is_pressed('k'):
                print("Force Stop durch Taste 'k'.")
                time.sleep(40)
                sys.exit(0)
            pixel_color = pyautogui.pixel(2011, 1259)
            #print(pixel_color, "(2222, 1279)")
            if pixel_color == (74, 194, 16):
                print("Opening")
                pyautogui.click(x=2222, y=1279)
            else: 
                #print(pixel_color, "(2222, 1279)")
                pixel_color2 = pyautogui.pixel(1655, 1184)
                #print(pixel_color2)
                if pixel_color2 == (43, 181, 12):
                    pyautogui.click(x=2500, y=51)
                    #time.sleep(0.2)
                #clear_console()
                pyautogui.click(x=1400, y=1327)
                #time.sleep(0.1)

    except KeyboardInterrupt:
        print("Mit STRG+C beendet.")

if __name__ == "__main__":
    main()
    sleapy()
time.sleep(30)
pixel_color = pyautogui.pixel(1306, 1324)
print(f"Die Farbe an Position ({1306},{1324}) ist: {pixel_color}")