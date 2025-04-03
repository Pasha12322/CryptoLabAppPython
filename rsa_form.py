import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import time
import os

class RSAForm:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption/Decryption")
        self.root.geometry("250x100")
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

        tk.Button(root, text="Encrypt File", command=self.encrypt_file).place(x=20, y=20)
        tk.Button(root, text="Decrypt File", command=self.decrypt_file).place(x=130, y=20)

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as f:
                data = f.read()
            rsa_data = data[:200]  # Обмежуємо розмір для RSA

            start_time = time.time()
            encrypted = self.public_key.encrypt(rsa_data, padding.PKCS1v15())
            rsa_time = (time.time() - start_time) * 1000  # у мілісекундах
            with open("encrypted.rsa", "wb") as f:
                f.write(encrypted)

            key = b"1234567890123456"  # 16 байтів для AES-128
            iv = b"1234567890123456"   # 16 байтів
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padding_length = 16 - (len(data) % 16)  # AES використовує блок 16 байт
            padded_data = data + bytes([padding_length] * padding_length)
            start_time = time.time()
            encryptor.update(padded_data) + encryptor.finalize()
            aes_time = (time.time() - start_time) * 1000

            messagebox.showinfo("Час", f"RSA (200 байт): {rsa_time:.2f} мс\nAES (весь файл): {aes_time:.2f} мс")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as f:
                encrypted = f.read()
            decrypted = self.private_key.decrypt(encrypted, padding.PKCS1v15())
            with open("decrypted.txt", "wb") as f:
                f.write(decrypted)
            messagebox.showinfo("Успіх", "Файл розшифровано успішно!")