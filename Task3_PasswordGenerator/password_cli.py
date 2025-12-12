#!/usr/bin/env python3
"""
Simple Password Generator (CLI)
Allows user to select:
- Length
- Include uppercase
- Include digits
- Include symbols
"""

import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]{}<>?/|" if use_symbols else ""

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "Error: No character sets selected."

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator (CLI) ===")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid length.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    pwd = generate_password(length, use_upper, use_digits, use_symbols)
    print("\nGenerated Password:")
    print(pwd)

if __name__ == "__main__":
    main()
