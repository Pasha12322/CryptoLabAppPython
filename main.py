import tkinter as tk
from des_form import DESForm
from rsa_form import RSAForm
from random_number_form import RandomNumberForm
from hash_form import HashForm
from digital_signature_form import DigitalSignatureForm
from rsa_cryptanalysis_form import RSACryptanalysisForm
from keylogger_form import KeyloggerForm
from cryptography.hazmat.primitives.asymmetric import rsa

class MainForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Lab Application")
        self.root.geometry("400x300")

        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

        tk.Button(root, text="Task 1: DES Encryption", width=30, command=self.open_des).place(x=50, y=20)
        tk.Button(root, text="Task 2: RSA Encryption", width=30, command=self.open_rsa).place(x=50, y=60)
        tk.Button(root, text="Task 3: Random Number Generator", width=30, command=self.open_random).place(x=50, y=100)
        tk.Button(root, text="Task 4: MD5 & SHA-1 Hashing", width=30, command=self.open_hash).place(x=50, y=140)
        tk.Button(root, text="Task 5: Digital Signature (RSA)", width=30, command=self.open_signature).place(x=50, y=180)
        tk.Button(root, text="Task 6: RSA Cryptanalysis", width=30, command=self.open_cryptanalysis).place(x=50, y=220)
        tk.Button(root, text="Task 7: Keylogger & Detector", width=30, command=self.open_keylogger).place(x=50, y=260)

    def open_des(self):
        DESForm(tk.Toplevel(self.root))

    def open_rsa(self):
        RSAForm(tk.Toplevel(self.root))

    def open_random(self):
        RandomNumberForm(tk.Toplevel(self.root))

    def open_hash(self):
        HashForm(tk.Toplevel(self.root))

    def open_signature(self):
        DigitalSignatureForm(tk.Toplevel(self.root), self.private_key, self.public_key)

    def open_cryptanalysis(self):
        RSACryptanalysisForm(tk.Toplevel(self.root))

    def open_keylogger(self):
        KeyloggerForm(tk.Toplevel(self.root))

if __name__ == "__main__":
    root = tk.Tk()
    app = MainForm(root)
    root.mainloop()