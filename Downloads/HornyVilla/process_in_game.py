#geschichte button(101, 319)
#buy upgrade geschichte (2047, 713)
#weiter button after chest opening (1303, 1301)
import keyboard
import time
import sys
import pyautogui
import os

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
                sys.exit(0)
            pixel_color = pyautogui.pixel(161, 362)
            #print(pixel_color, "(161, 362)")
            if pixel_color == (217, 134, 19):
                pyautogui.click(x=101, y=319)
                time.sleep(0.02)
                pyautogui.click(x=2000, y=481)
                print("Upgrade")
                #time.sleep(0.2)
            else: 
                if pixel_color == (217, 134, 19):
                    pyautogui.click(x=101, y=319)
                    time.sleep(0.02)
                    pyautogui.click(x=2000, y=481)
                else:
                    pixel_color2 = pyautogui.pixel(1655, 1184)
                    #print(pixel_color2)
                    if pixel_color2 == (43, 181, 12):
                        pyautogui.click(x=2500, y=51)
                    #time.sleep(0.2)
                #clear_console()
                    pyautogui.click(x=1303, y=1301)
                #time.sleep(0.1)
                


            # Beispielarbeit (hier einfach warten)
            #print("Arbeite ...")
            #pyautogui.click(x=101, y=319)
            #time.sleep(0.2)
            #pyautogui.click(x=2047, y=713)
            #time.sleep(0.2)
            #for i in range(anzahl):
                #print(f"Durchlauf {i+1} von {anzahl}")
                #pyautogui.click(x=1303, y=1301)
                #time.sleep(0.1)
            #pixel_color = pyautogui.pixel(1306, 1324)
            #if pixel_color == (255, 255, 255):
                #print("True")
                #for i in range(anzahl):
                    #print(f"Durchlauf von dialog {i+1} von {anzahl}")
                    #pyautogui.click(x=2047, y=713)
                    #time.sleep(0.1)


            

    except KeyboardInterrupt:
        print("Mit STRG+C beendet.")

if __name__ == "__main__":
    main()
    sleapy()
time.sleep(30)
pixel_color = pyautogui.pixel(1306, 1324)
print(f"Die Farbe an Position ({1306},{1324}) ist: {pixel_color}")