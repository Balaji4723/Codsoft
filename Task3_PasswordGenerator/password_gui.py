#!/usr/bin/env python3
"""
Password Generator GUI (Tkinter)
"""

import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_label.config(text="Invalid length")
        return

    use_upper = upper_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]{}<>?/|" if use_symbols else ""

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        result_label.config(text="Select at least one option!")
        return

    password = "".join(random.choice(all_chars) for _ in range(length))
    result_label.config(text=password)

root = tk.Tk()
root.title("Password Generator (CODSOFT)")
root.geometry("380x280")

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack()

upper_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
