import tkinter as tk
from tkinter import messagebox
import random

class RandomNumberForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Generator")
        self.root.geometry("200x100")

        tk.Button(root, text="Generate & Check Prime", command=self.generate).place(x=20, y=20)

    def generate(self):
        number = self.generate_random_number()
        is_prime = self.is_prime_rabin_miller(number)
        messagebox.showinfo("Результат", f"Згенеровано: {number}\nЧи є простим: {is_prime}")

    def generate_random_number(self):
        return random.randint(1000, 1000000) | 1  # Непарне число

    def is_prime_rabin_miller(self, n, k=5):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False

        d, s = n - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1

        for _ in range(k):
            a = random.randrange(2, min(n - 2, float('inf')))
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True