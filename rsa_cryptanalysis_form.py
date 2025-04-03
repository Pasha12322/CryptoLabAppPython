import tkinter as tk
from tkinter import messagebox

class RSACryptanalysisForm:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Cryptanalysis")
        self.root.geometry("200x100")

        tk.Button(root, text="Analyze Ciphertext", command=self.analyze).place(x=20, y=20)

    def analyze(self):
        e, n, C = 5, 119, 95
        M = self.keyless_reading_rsa(C, e, n)
        messagebox.showinfo("Результат", f"Розшифроване повідомлення: {M}")

    def keyless_reading_rsa(self, C, e, n):
        Ce = C
        for j in range(1, 10):
            Ce = pow(Ce, e, n)
            if Ce == C:
                return pow(C, pow(e, j - 1), n)
        return -1