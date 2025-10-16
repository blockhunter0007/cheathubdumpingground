import shutil
import os
from pathlib import Path
import requests
import time
import certifi
import sys
####################################################
#                  init                            #
#build = ".exe"                                     #
build = Path(sys.executable if getattr(sys, "frozen", False) else __file__).resolve()
#build = ".py"                                      #
#location = "local"                                 #
#location = "appdata"                               #
####################################################
os.environ["SSL_CERT_FILE"] = certifi.where()
DOWNLOAD_URL = f"https://blockhunter0007.github.io/cheathubdumpingground/main{build}"
APP_FILENAME = f"main{build}"
if getattr(sys, 'frozen', False):
    # Wenn mit PyInstaller gebaut
    APPPATH = Path(sys.executable).resolve()
else:
    # Wenn als normales Python-Skript ausgeführt
    APPPATH = Path(__file__).resolve()
APP = APPPATH / f"main{build}"
if build == ".exe":
    try:
        os.system("taskkill /f /im main.exe")
    except:
        print("Not Open")
time.sleep(1)
# Prüfen, ob der Ordner existiert
if os.path.exists(APPPATH):
    shutil.rmtree(APPPATH)
    print("Ordner und Inhalt erfolgreich gelöscht.")
else:
    print("Ordner wurde nicht gefunden.")
    exit
time.sleep(1)
if not APPPATH.exists():
    APPPATH.mkdir(parents=True, exist_ok=True)
try:
    r = requests.get(DOWNLOAD_URL, stream=True)
    r.raise_for_status()
    with open(APP, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
except Exception as e:
    print("error")
os.startfile(APP)