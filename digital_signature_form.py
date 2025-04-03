import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import hashlib

class DigitalSignatureForm:
    def __init__(self, root, private_key, public_key):
        self.root = root
        self.root.title("Digital Signature (RSA)")
        self.root.geometry("250x100")
        self.private_key = private_key  
        self.public_key = public_key

        tk.Button(root, text="Sign File", command=self.sign_file).place(x=20, y=20)
        tk.Button(root, text="Verify Signature", command=self.verify_signature).place(x=130, y=20)

    def sign_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "rb") as f:
                    data = f.read()
                file_hash = hashlib.sha256(data).digest()

                signature = self.private_key.sign(
                    file_hash,
                    padding.PKCS1v15(),
                    hashes.SHA256()
                )

                with open("signature.sig", "wb") as f:
                    f.write(signature)
                messagebox.showinfo("Успіх", "Файл підписано успішно!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося підписати файл: {str(e)}")

    def verify_signature(self):
        file_path = filedialog.askopenfilename(title="Вибери оригінальний файл")
        if file_path:
            sig_path = filedialog.askopenfilename(title="Вибери файл підпису")
            if sig_path:
                try:
                    with open(file_path, "rb") as f:
                        data = f.read()
                    file_hash = hashlib.sha256(data).digest()

                    with open(sig_path, "rb") as f:
                        signature = f.read()

                    self.public_key.verify(
                        signature,
                        file_hash,
                        padding.PKCS1v15(),
                        hashes.SHA256()
                    )
                    messagebox.showinfo("Результат", "Підпис перевірено: True")
                except Exception as e:
                    messagebox.showinfo("Результат", f"Підпис перевірено: False\nПомилка: {str(e)}")