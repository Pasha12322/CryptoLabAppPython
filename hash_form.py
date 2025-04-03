import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import time

class HashForm:
    def __init__(self, root):
        self.root = root
        self.root.title("MD5 & SHA-1 Hashing")
        self.root.geometry("150x100")

        tk.Button(root, text="Hash File", command=self.hash_file).place(x=20, y=20)

    def hash_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as f:
                data = f.read()

            start_time = time.time()
            md5_hash = hashlib.md5(data).hexdigest()
            md5_time = (time.time() - start_time) * 1000

            start_time = time.time()
            sha1_hash = hashlib.sha1(data).hexdigest()
            sha1_time = (time.time() - start_time) * 1000

            messagebox.showinfo("Хеші", f"MD5: {md5_hash}\nЧас: {md5_time:.2f} мс\nSHA-1: {sha1_hash}\nЧас: {sha1_time:.2f} мс")