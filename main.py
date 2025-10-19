from customtkinter import CTkImage
import customtkinter as ctk
import os
import json
import requests
from pathlib import Path
import time
import webbrowser
from PIL import Image, ImageTk
import keyring
import subprocess
import sys
import shutil
from pypresence import Presence

####################################################
#                  init                            #
#build = ".exe"                                    #
build = Path(sys.executable if getattr(sys, "frozen", False) else __file__).resolve()
build = build.suffix
print(build)
####################################################

####################################################
#                   Version                        #
version = "01.00.04"                               #
version_state = "Beta"                             #
#                                                  #
####################################################


####################################################
#                  Discord                         #
####################################################
discord_connected = False
def discord():
    global discord_connected
    if not discord_connected:
        try:
            client_id = '1426325116018495623'
            RPC = Presence(client_id)
            RPC.connect()
            start_time = time.time()
            #start_time = int(start_time) - 60000
            #start_time = start_time - start_time + 1
            RPC.update(state=f"version: {version_state} {version}", details="Premium Cheats For Free", large_image="large_image", small_image="small_image", start=start_time, buttons=[{"label": "Download", "url": "https://blockhunter0007.github.io/cheathubdumpingground/"}])
            discord_connected = True
            print("DC")
        except:
            print("No DC")
        root.after(5000, discord)


####################################################
#              App Backend comunication            #
####################################################
DOWNLOAD_URL_RESTART = f"https://blockhunter0007.github.io/cheathubdumpingground/restart{build}"
DOWNLOAD_URL_UPDATE = f"https://blockhunter0007.github.io/cheathubdumpingground/update{build}"
default_fg = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
default_hover = ctk.ThemeManager.theme["CTkButton"]["hover_color"]
default_text = ctk.ThemeManager.theme["CTkButton"]["text_color"]
if getattr(sys, 'frozen', False):
    # Wenn mit PyInstaller gebaut
    apppath = Path(sys.executable).resolve().parent
else:
    # Wenn als normales Python-Skript ausgeführt
    apppath = Path(__file__).resolve().parent
print(apppath)
downloadfolderpath = apppath / "downloads"
datapath = apppath / "data"
assets_path = apppath / "assets"
theme_path = apppath / "themes"
update_path = apppath / f"update{build}"
restart_path = apppath / f"restart{build}"
main_exe = apppath / f"main{build}"
if not update_path.exists():
    try:
        r = requests.get(DOWNLOAD_URL_UPDATE, stream=True)
        r.raise_for_status()
        with open(update_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as e:
        print("error")
if not restart_path.exists():
    try:
        r = requests.get(DOWNLOAD_URL_RESTART, stream=True)
        r.raise_for_status()
        with open(update_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as e:
        print("error")
if not theme_path.exists():
    theme_path.mkdir()
if not downloadfolderpath.exists():
    downloadfolderpath.mkdir()
downloadjsonpath = apppath / "downloads" / "downloads.json"
if not downloadjsonpath.exists():
    with open(downloadjsonpath, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)
downloadsfolder = apppath / "downloads"
login_infos = 0
assets_path = apppath / "assets"
if not assets_path.exists():
    assets_path.mkdir()
runadsscan = 0
bilder = [
    assets_path / "ad1.png",
    assets_path / "ad2.png",
    assets_path / "ad3.png"
]
downloadjson = {}
links = [
    "https://pinguinbrowser-660h.onrender.com",
    "https://pinguinbrowser-660h.onrender.com",
    "https://pinguinbrowser-660h.onrender.com"
]
aktuell = 0
response = None
daten = {}
json_load = False
dateipfad = apppath / "data" / "server.json"
url = 'https://blockhunter0007.github.io/cheathubdumpingground/server.json'
root = ctk.CTk()
root.title("Cheats")
root.geometry("600x400")
icon_path = assets_path / "icon.ico"
if not icon_path.exists():
    picture_url2 = "https://raw.githubusercontent.com/blockhunter0007/cheathubdumpingground/refs/heads/main/assets/icon.ico"
    print(picture_url2)
    if not icon_path.exists():
        print(f"Datei nicht gefunden: {icon_path}")
        try:
            response = requests.get(picture_url2)
            with open(icon_path, "wb") as file:
                file.write(response.content)
            print(f"{icon_path} wurde heruntergeladen.")
            root.iconbitmap(icon_path)
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Herunterladen von {icon_path}: {e}")
            #time.sleep(5)
if icon_path.exists():
    root.iconbitmap(icon_path)
    print("i hate my life")
ctk.set_appearance_mode("dark")  # Dunkelmodus
ads_visible = True  # True = Ads werden angezeigt, False = Ads werden ausgeblendet

def auswahl_gedrueckt(wert):
    settings_json = apppath / "data" / "settings.json"

    # Vorhandene Daten laden (falls Datei existiert)
    if settings_json.exists():
        with open(settings_json, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    # Wert ggf. anpassen
    if wert not in standard_themes:
        wert = wert + ".json"

    # Nur den Key "theme" ergänzen oder überschreiben
    data["theme"] = wert

    # Datei zurückschreiben
    with open(settings_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    restart()

#dropdown.pack(pady=20, padx=0)
def update_button_click():
    os.startfile(update_path)
    root.destroy()
    sys.exit()


def update_message():
    update_window = ctk.CTkToplevel(root)
    update_window.title("Update verfügbar")
    update_window.geometry("400x200")
    update_window.grab_set()

    label = ctk.CTkLabel(update_window, text="Ein Update ist verfügbar!\nBitte lade die neueste Version herunter.")
    label.pack(pady=20, padx=20)

    download_button = ctk.CTkButton(
        update_window,
        text="Update jetzt installieren",
        command=lambda: update_button_click()  # HIER richtig mit Parametern
    )
    download_button.pack(pady=10)

    close_button = ctk.CTkButton(
        update_window,
        text="Später",
        command=update_window.destroy
    )
    close_button.pack(pady=10)

settings_json="settings.json"
settings_json=datapath / settings_json
def check_saved_login():
    if not settings_json.exists:
        with open(dateipfad, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
    saved_username = keyring.get_password("CheatAppUsername", "username")
    if saved_username:
        saved_password = keyring.get_password("CheatAppPassword", saved_username)
        if saved_password:
            # Automatischer Login
            print("Gefundene gespeicherte Login-Daten. Versuche automatischen Login...")
            login_with_credentials(saved_username, saved_password)

try:
    response = requests.get(url)
    #print("HTTP Status:", response.status_code)
    #print("Rohdaten (erste 500 Zeichen):", response.text[:1000])
    if response.status_code == 200:
        daten = response.json()  # JSON direkt parsen
        if not dateipfad.parent.exists():
           datapath.mkdir()
        with open(dateipfad, "w", encoding="utf-8") as f:
            json.dump(daten, f, ensure_ascii=False, indent=4)
        json_load = True
    else:
        print("Fehler beim Abrufen:", response.status_code)
        json_load = False
        print(response)
except requests.exceptions.RequestException as e:
    print("Fehler beim Abrufen der URL:", e)
    json_load = False

#json_string = ''
#daten = json.loads(json_string)
#print(daten["Hund"])   # Hund

# Pfad zur server.json im Unterordner "data"
if json_load == False:
    if not dateipfad.exists():
        print(f"Datei nicht gefunden: {dateipfad}")
        exit(1)
    try:
        with open(dateipfad, "r", encoding="utf-8") as f:
            daten = json.load(f)
        #print("Geladene Daten:")
        #print(daten)
    except json.JSONDecodeError:
        print('failed finding jsnversion (initialisationcheck) please turn on your wifi to install our programm')
        print('we only need wifi to see what cheats we have and download them.')
        print('after turning on the wifi once you can use our product completly offline')
        time.sleep(10)
        exit(1)

if "version" in daten["cheathub"]:
    if daten["cheathub"]["version"] != version:
        update_message()
        print('update')
        print('your version', version, 'is not the newest its', daten["cheathub"]["version"])
else:
    print('failed finding jsnversion (initialisationcheck) please turn on your wifi to install our programm')
    print('we only need wifi to see what cheats we have and download them.')
    print('after turning on the wifi once you can use our product completly offline')
    time.sleep(10)
    exit(1)
  # Blaue Akzentfarbe
themen_liste = list(daten["cheathub"]["themes"].keys())
standard_themes = ["blue", "green", "dark-blue"]
themen_liste.extend(standard_themes)
#for i, theme in enumerate(daten["themes"]):
for theme in daten["cheathub"]["themes"]:
    main_theme = daten["cheathub"]["themes"][theme]
    #print(main_theme)
    json_file =main_theme["filename"]
    theme_json=theme_path / json_file
    #print(theme_json)
    if not theme_json.exists():
        try:
            downloadthemeurl = main_theme["downloadurl"]
            theme_download = requests.get(downloadthemeurl)
            theme_downloaded = theme_download.json()
            if theme_download.status_code == 200:
                with open(theme_json, "w", encoding="utf-8") as f:
                    json.dump(theme_downloaded, f, ensure_ascii=False, indent=4)
        except requests.exceptions.RequestException as e:
            print("Fehler beim Abrufen der URL:", e) 
    else:
        pass

dropdown = ctk.CTkOptionMenu(
    master=root,
    values=themen_liste,                # Aus JSON geladen!
    command=auswahl_gedrueckt,
    text_color="white"
)
print(theme)

theme = theme.split(".")[0]
dropdown_current = themen_liste.index(theme)
dropdown.set(themen_liste[dropdown_current])



# Label zur Anzeige
dropdown.pack(side="top", anchor="w", padx=10, pady=10)


####################################################
#                        CTK                       #
####################################################

button_frame = ctk.CTkFrame(root)
button_frame.pack(padx=20, pady=20, fill="both", expand=True)
def button_click_start(name):
    print(f"Button {name} wurde geklickt! und gestartet")
    product = daten["cheathub"]["products"][name]
    id = product["id"]
    cheat_path = downloadsfolder / id / product["start_program"]
    p = Path(cheat_path).resolve()

    if not p.exists():
        print(f"Datei nicht gefunden: {p}")
        return
    # Dateiendung prüfen
    ext = p.suffix.lower()
    if ext == ".py" or ext == ".pyw":
        # Python-Datei im neuen Terminal starten
        subprocess.Popen(
            ["start", "cmd", "/k", "python", f"{cheat_path}"],
            shell=True
        )
    elif ext == ".exe":
        # EXE im neuen Terminal starten
        subprocess.Popen(
            ["start", "cmd", "/k", f'"{p}"'],
            shell=True
        )
    else:
        # Fallback für andere Dateitypen
        subprocess.Popen(
            ["start", "cmd", "/k", f'"{p}"'],
            shell=True
        )


def update_button_click(name):
    button_click_uninstall(name)
    button_click(name)

def button_click_uninstall(name):
    if downloadjsonpath.exists():
        with open(downloadjsonpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if name in data:
            del data[name]

        with open(downloadjsonpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # UI nur für dieses Produkt aktualisieren
    btns = product_buttons[name]

    # Starten-Button zurück zu Download
    btns["start"].configure(text="Download", command=lambda n=name: button_click(n))

    # Deinstallieren-Button entfernen
    if btns.get("uninstall"):
        btns["uninstall"].destroy()
        btns["uninstall"] = None
    ordner_pfad = downloadsfolder / daten["cheathub"]["products"][name]["id"]
    shutil.rmtree(ordner_pfad)

# Funktion, die beim Klick ausgeführt wird
def button_click(name):
    # JSON aktualisieren
    if downloadjsonpath.exists():
        with open(downloadjsonpath, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    data[name] = daten["cheathub"]["products"][name]

    with open(downloadjsonpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    # UI aktualisieren nur für dieses Produkt
    btns = product_buttons[name]

    # Download-Button zu Starten ändern
    #btns["start"].configure(text="Starten", command=lambda n=name: button_click_start(n), fg_color=None, hover_color=None, text_color=None)

    btns["start"].configure(text="Starten", command=lambda n=product_name: button_click_start(n), fg_color=default_fg, hover_color=default_hover, text_color=default_text)
    # Deinstallieren-Button erstellen, falls noch nicht vorhanden
    if not btns.get("uninstall"):
        i = list(daten["cheathub"]["products"]).index(name)
        uninstall_btn = ctk.CTkButton(button_frame, text="Deinstallieren", fg_color="red", hover_color="#ff4d4d",
                                      command=lambda n=name: button_click_uninstall(n))
        uninstall_btn.grid(row=i, column=2, padx=10, pady=5, sticky="ew")
        btns["uninstall"] = uninstall_btn
    download_url = daten["cheathub"]["products"][name]["download_url"]
    dateinameundpfad = apppath / "downloads" / daten["cheathub"]["products"][name]["id"] / daten["cheathub"]["products"][name]["start_program"]
    response2 = requests.get(download_url)
    if not dateinameundpfad.parent.exists():
        dateinameundpfad.parent.mkdir(parents=True, exist_ok=True)
    print (f"Starte Download von {download_url} nach {dateinameundpfad}")
    with open(dateinameundpfad, "wb") as file:
        file.write(response2.content)

def open_login_window():
    global login_infos
    # 1. Neues Toplevel-Fenster erstellen
    login_window = ctk.CTkToplevel(root)
    login_window.title("Benutzer-Anmeldung")
    login_window.geometry("350x300")  # etwas mehr Platz für Fehlermeldung
    
    # Sorgt dafür, dass das Login-Fenster im Vordergrund bleibt
    login_window.grab_set()

    # 2. Widgets für das Login-Fenster erstellen
    
    # Benutzername Label und Eingabefeld
    username_label = ctk.CTkLabel(login_window, text="Benutzername")
    username_label.pack(pady=(20, 5), padx=30)

    username_entry = ctk.CTkEntry(login_window, width=200, placeholder_text="Benutzername eingeben")
    username_entry.pack(pady=5, padx=30)

    # Passwort Label und Eingabefeld
    password_label = ctk.CTkLabel(login_window, text="Passwort")
    password_label.pack(pady=(10, 5), padx=30)

    password_entry = ctk.CTkEntry(login_window, width=200, placeholder_text="Passwort eingeben", show="*")
    password_entry.pack(pady=5, padx=30)

    # Platz für Fehlermeldungen (initial leer, wird bei Fehler sichtbar gemacht)
    # Wir speichern das Label als Attribut des Fensters, damit login_api_call es updaten kann
    login_window.error_label = ctk.CTkLabel(login_window, text="", text_color="red")
    login_window.error_label.pack(pady=(5, 5), padx=30)

    # Anmelden-Button
    login_button = ctk.CTkButton(
        login_window,
        text="Anmelden",
        command=lambda: login_api_call(username_entry, password_entry, login_window)
    )
    login_button.pack(pady=10, padx=30)



def login_with_credentials(username, password):
    url = f"https://pinguinbrowser.pythonanywhere.com/accountapi/{username}/{password}"
    try:
        response = requests.get(url)
        result = response.json()
        if result.get("success"):
            # Benutzer automatisch anmelden
            anmelden_button.configure(text=username, command=lambda: show_logout_popup(username))
            if result.get("is_pro"):
                info_label.configure(text="(Pro)")
            else:
                info_label.configure(text="Pro kaufen")
            global ads_visible
            ads_visible = not result.get("is_pro")
        else:
            print("Gespeicherte Daten ungültig.")
    except:
        print("Fehler beim automatischen Login")


def login_api_call(username_entry, password_entry, login_window):
    global ads_visible
    global login_infos
    username = username_entry.get()
    password = password_entry.get()
    print(f"Anmelden mit Benutzername: {username} und Passwort: {password}")
    url = f"https://pinguinbrowser.pythonanywhere.com/accountapi/{username}/{password}"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        # Netzwerkfehler → Meldung anzeigen
        msg = f"Netzwerkfehler: {e}"
        print(msg)
        login_window.error_label.configure(text=msg)
        return

    # Wenn wir hier sind, haben wir eine HTTP-Antwort
    if response.status_code == 200:
        try:
            result = response.json()
        except ValueError:
            login_window.error_label.configure(text="Ungültige Server-Antwort.")
            return

        if result.get('success') == True:
            print("Erfolgreich angemeldet!")
            keyring.set_password("CheatAppUsername", "username", username)
            keyring.set_password("CheatAppPassword", username, password)
            # Login-Fenster schließen
            login_window.destroy()

            # Button in Label mit Benutzernamen ändern
            anmelden_button.configure(text=username, command=lambda: show_logout_popup(username))

            # PRO-Status prüfen
            if result.get("is_pro") == True:
                info_label.configure(text=f"(Pro)")
                ads_visible = False
                bild_label.configure(image=None, text="")
                bild_label.update_idletasks()

                # Ads sofort ausblenden (UI aktualisieren)
                bild_label.configure(image=None, text="")
                bild_label.update_idletasks()
            else:
                info_label.configure(text="Pro kaufen")
                info_label.bind("<Button-1>", open_pro_website)
                ads_visible = True

            print("is pro:", result.get("is_pro"))

        elif result.get("success") == False:
            # Anmeldedaten falsch — Meldung im Login-Fenster anzeigen
            msg = result.get("message", "Anmeldung fehlgeschlagen. Benutzername/Passwort falsch.")
            print("Anmeldung fehlgeschlagen:", msg)
            login_window.error_label.configure(text=msg)
        else:
            # Unerwartete Antwortstruktur
            msg = "Unerwartete Server-Antwort."
            print(msg, result)
            login_window.error_label.configure(text=msg)
    elif response.status_code == 401:
        # HTTP 401 = Unauthorized (falsche Anmeldedaten)
        msg = "Ungültiger Benutzername oder Passwort."
        print(msg)
        login_window.error_label.configure(text=msg)
    else:
        # andere HTTP-Fehlercodes anzeigen
        msg = f"Fehler beim Abrufen: {response.status_code}"
        print(msg)
        login_infos = response.status_code
        login_window.error_label.configure(text=msg)


def show_logout_popup(username):
    logout_window = ctk.CTkToplevel(root)
    logout_window.title("Abmelden")
    logout_window.geometry("300x150")
    logout_window.grab_set()  # sorgt dafür, dass das Fenster im Vordergrund bleibt

    label = ctk.CTkLabel(logout_window, text=f"Angemeldet als {username}")
    label.pack(pady=20)

    logout_button = ctk.CTkButton(
        logout_window,
        text="Abmelden",
        fg_color="red",  # rote Farbe
        hover_color="#ff4d4d",
        command=lambda: logout(logout_window)
    )
    logout_button.pack(pady=10)

def open_pro_website(event=None):
    webbrowser.open("https://pinguinbrowser.pythonanywhere.com/")

def logout(logout_window):
    global ads_visible
    global anmelden_button
    # Popup schließen
    logout_window.destroy()
    # Button wieder auf "Anmelden" setzen
    anmelden_button.configure(text="Anmelden", command=open_login_window)
    info_label.configure(text="Anmelden")
    info_label.unbind("<Button-1>")
    ads_visible = True

    # Gespeicherte Login-Daten löschen
    saved_username = keyring.get_password("CheatAppUsername", "username")
    if saved_username:
        keyring.delete_password("CheatAppUsername", "username")
        keyring.delete_password("CheatAppPassword", saved_username)


def click_cheat_lable(product):
    def inner(event):
        # Neues Fenster erstellen
        info_window = ctk.CTkToplevel(root)
        info_window.title(product["name"])
        info_window.geometry("400x300")
        info_window.grab_set()

        # Produktinfos anzeigen
        name_label = ctk.CTkLabel(info_window, text=f"Name: {product['name']}")
        name_label.pack(pady=5, padx=10, anchor="w")

        id_label = ctk.CTkLabel(info_window, text=f"ID: {product['id']}")
        id_label.pack(pady=5, padx=10, anchor="w")

        cheat_version_label = ctk.CTkLabel(info_window, text=f"Cheat Version: {product['version']}")
        cheat_version_label.pack(pady=5, padx=10, anchor="w")

        updated_label = ctk.CTkLabel(info_window, text=f"Last Updated: {product['last_updated']}")
        updated_label.pack(pady=5, padx=10, anchor="w")

        keywords_label = ctk.CTkLabel(info_window, text=f"Keywords: {product['keywords']}", wraplength=380)
        keywords_label.pack(pady=5, padx=10, anchor="w")
    return inner



bilder_cache = []
def wechsel_bild():
    global bilder
    global aktuell
    global runadsscan
    for bild in bilder:
        picture_url = "https://blockhunter0007.github.io/cheathubdumpingground/assets/" + bild.name
        #print(bild)
        #print(picture_url)
        if not bild.exists():
            if runadsscan == 3:
                print("User is not pro and ads are missing please turn on your wifi to download the ads")
                sys.exit(1)
            print(f"Datei nicht gefunden: {bild}")
            try:
                response = requests.get(picture_url)
                with open(bild, "wb") as file:
                    file.write(response.content)
                print(f"{bild} wurde heruntergeladen.")
                runadsscan += 1
            except requests.exceptions.RequestException as e:
                print(f"Fehler beim Herunterladen von {bild}: {e}")
    if ads_visible:
        try:
            if not bild_label.winfo_ismapped():
                bild_label.pack(pady=10)

            # Bild laden
            img = Image.open(bilder[aktuell])
            img = img.resize((400, 100), Image.LANCZOS)
            ctk_img = CTkImage(img, size=(img.width, img.height))

            # Referenz speichern (nicht nur in Label!)
            bilder_cache.append(ctk_img)
            bild_label.configure(image=ctk_img, text="")
            bild_label.image = ctk_img

            aktuell = (aktuell + 1) % len(bilder)
        except:
            print("Error Loading Pics")
    else:
        try:
            if hasattr(bild_label, "image"):
                del bild_label.image
            if bild_label.winfo_ismapped():
                bild_label.pack_forget()
        except:
            print("Error Loading Pics")
    root.after(5000, wechsel_bild)


# Funktion zum Öffnen des Links
def open_link(event):
    link_index = (aktuell - 1) % len(links)  # vorheriges Bild
    webbrowser.open(links[link_index])

# Label erstellen
bild_label = ctk.CTkLabel(root, text="")
bild_label.pack(pady=20)
bild_label.bind("<Button-1>", open_link)

# Start
anmelden_button = ctk.CTkButton(root, text="Anmelden", command=open_login_window)
anmelden_button.place(relx=1.0, rely=0, anchor="ne", x=-10, y=10)
info_label = ctk.CTkLabel(root, text="Not logged in")
info_label.place(relx=1.0, rely=0, anchor="ne", x=-10, y=50)
# Buttons dynamisch aus JSON erstellen




# globales Dictionary für Buttons
product_buttons = {}  # key = Produktname, value = {"start": Button, "uninstall": Button}
product_labels = {}


# Buttons dynamisch erstellen
for i, product_name in enumerate(daten["cheathub"]["products"]):
    product = daten["cheathub"]["products"][product_name]
    print(product)
    label = ctk.CTkLabel(button_frame, text=product_name)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    label.bind("<Button-1>", click_cheat_lable(product))

    # Prüfen, ob Produkt bereits heruntergeladen
    with open(downloadjsonpath, "r", encoding="utf-8") as f:
        downloadjson = json.load(f)

    if product_name in downloadjson:
        # Starten-Button
        if daten["products"][product_name]["version"] != downloadjson[product_name]["version"]:
            start_btn = ctk.CTkButton(button_frame, text="Update", command=lambda n=product_name: update_button_click(n), fg_color="yellow", hover_color="#e6e600", text_color="black"); start_btn.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            start_btn.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            # Hier
        else:
            start_btn = ctk.CTkButton(button_frame, text="Starten", command=lambda n=product_name: button_click_start(n))
            start_btn.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

        # Deinstallieren-Button
        uninstall_btn = ctk.CTkButton(button_frame, text="Deinstallieren", fg_color="red", hover_color="#ff4d4d",
                                      command=lambda n=product_name: button_click_uninstall(n))
        uninstall_btn.grid(row=i, column=2, padx=10, pady=5, sticky="ew")
    else:
        # Download-Button
        start_btn = ctk.CTkButton(button_frame, text="Download", command=lambda n=product_name: button_click(n))
        start_btn.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

        uninstall_btn = None  # noch kein Deinstallieren-Button

    # Buttons speichern
    product_buttons[product_name] = {"start": start_btn, "uninstall": uninstall_btn}

def restart():
    global root
    restart_file = apppath / f"restart{build}"
    os.startfile(restart_file)
    root.destroy()

discord()
check_saved_login()
wechsel_bild()
#root.destroy()
root.mainloop()
