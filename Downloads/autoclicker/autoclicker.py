import os
import json
import customtkinter as ctk
import pyautogui
import threading
import time
import keyboard

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "data.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as fp:
        json.dump({"cps": 10, "button": "left", "trigger": "f8"}, fp)

with open(DATA_FILE, "r") as fp:
    settings = json.load(fp)

class AutoClickerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Autoclicker GUI")
        self.geometry("800x400")
        self.running = False
        self.thread = None

        self.cps_label = ctk.CTkLabel(self, text="Klicks pro Sekunde (CPS):")
        self.cps_label.pack()
        self.cps_entry = ctk.CTkEntry(self)
        self.cps_entry.insert(0, str(settings.get("cps", 10)))
        self.cps_entry.pack()

        self.button_label = ctk.CTkLabel(self, text="Maustaste:")
        self.button_label.pack()
        self.button_var = ctk.StringVar(value=settings.get("button", "left"))
        self.left_radio = ctk.CTkRadioButton(self, text="Links", variable=self.button_var, value="left")
        self.left_radio.pack(side="left", padx=20)
        self.right_radio = ctk.CTkRadioButton(self, text="Rechts", variable=self.button_var, value="right")
        self.right_radio.pack(side="left", padx=20)

        self.trigger_label = ctk.CTkLabel(self, text="Trigger-Taste (z. B. 'f8'):")
        self.trigger_label.pack()
        self.trigger_entry = ctk.CTkEntry(self)
        self.trigger_entry.insert(0, settings.get("trigger", "f8"))
        self.trigger_entry.pack()

        self.save_btn = ctk.CTkButton(self, text="Einstellungen Speichern", command=self.save_settings)
        self.save_btn.pack(pady=(10, 5))

        self.status_label = ctk.CTkLabel(self, text="Status: gestoppt")
        self.status_label.pack(pady=(5, 0))

        self.toggle_btn = ctk.CTkButton(self, text="Manuell starten", command=self.toggle_clicker)
        self.toggle_btn.pack(pady=(5, 10))

        # Start trigger key monitor thread
        self.monitor_thread = threading.Thread(target=self.monitor_trigger, daemon=True)
        self.monitor_thread.start()

    def save_settings(self):
        cps_value = max(1, int(self.cps_entry.get()))
        button_value = self.button_var.get()
        trigger_value = self.trigger_entry.get()
        with open(DATA_FILE, "w") as fp:
            json.dump({"cps": cps_value, "button": button_value, "trigger": trigger_value}, fp)
        settings["cps"] = cps_value
        settings["button"] = button_value
        settings["trigger"] = trigger_value

    def toggle_clicker(self):
        if self.running:
            self.running = False
            self.status_label.configure(text="Status: gestoppt")
            self.toggle_btn.configure(text="Manuell starten")
        else:
            self.running = True
            self.status_label.configure(text="Status: läuft")
            self.toggle_btn.configure(text="Manuell stoppen")
            self.thread = threading.Thread(target=self.run_clicker)
            self.thread.start()

    def monitor_trigger(self):
        while True:
            if keyboard.is_pressed(settings["trigger"]):
                self.toggle_clicker()
                time.sleep(0.5)  # debounce so toggling isn't instant
            time.sleep(0.05)

    def run_clicker(self):
        while self.running:
            pyautogui.click(button=settings["button"])
            time.sleep(1 / settings["cps"])
        self.thread = None

if __name__ == "__main__":
    app = AutoClickerGUI()
    app.mainloop()