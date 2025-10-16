import os
from pathlib import Path
import time
import sys
time.sleep(1)

####################################################
#                  init                            #
#build = ".exe"                                     #
build = Path(sys.executable if getattr(sys, "frozen", False) else __file__).resolve()
#location = "appdata"                               #
####################################################


if getattr(sys, 'frozen', False):
    # Wenn mit PyInstaller gebaut
    apppath = Path(sys.executable).resolve().parent
else:
    # Wenn als normales Python-Skript ausgeführt
    apppath = Path(__file__).resolve().parent

#kill if open
if build == ".exe":
    try:
        os.system("taskkill /f /im main.exe")
    except:
        print("Not Open")
    time.sleep(2) #stopp to wait for pyinstaller
    apppath = apppath / f"main.{build}"
    os.startfile(apppath)
if build == ".py":
    apppath = apppath / f"main.{build}"
    os.startfile(apppath)