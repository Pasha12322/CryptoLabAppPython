import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class DESForm:
    def __init__(self, root):
        self.root = root
        self.root.title("AES Encryption/Decryption")  
        self.root.geometry("250x100")

        tk.Button(root, text="Encrypt File", command=self.encrypt_file).place(x=20, y=20)
        tk.Button(root, text="Decrypt File", command=self.decrypt_file).place(x=130, y=20)

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as f:
                data = f.read()
            key = b"1234567890123456"  # 16 байтів для AES-128
            iv = b"1234567890123456"   # 16 байтів
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padding_length = 16 - (len(data) % 16)  # AES використовує блок 16 байт
            padded_data = data + bytes([padding_length] * padding_length)
            encrypted = encryptor.update(padded_data) + encryptor.finalize()
            with open("encrypted.aes", "wb") as f:
                f.write(encrypted)
            messagebox.showinfo("Успіх", "Файл зашифровано успішно!")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as f:
                encrypted = f.read()
            key = b"1234567890123456"
            iv = b"1234567890123456"
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
            padding_length = decrypted_padded[-1]
            decrypted = decrypted_padded[:-padding_length]
            with open("decrypted.txt", "wb") as f:
                f.write(decrypted)
            messagebox.showinfo("Успіх", "Файл розшифровано успішно!")