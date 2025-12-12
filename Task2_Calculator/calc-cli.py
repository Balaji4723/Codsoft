#!/usr/bin/env python3
"""
Simple CLI Calculator
Supports: +, -, *, /, %, power, and simple history.
"""

import math

history = []

def calc(a, op, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Invalid number"
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a / b
        if op == "%":
            return a % b
        if op == "^" or op.lower() == "pow":
            return math.pow(a, b)
        return "Unsupported operator"
    except Exception as e:
        return f"Error: {e}"

def show_help():
    print("""
Simple CLI Calculator
Usage: <number> <operator> <number>
Operators: +  -  *  /  %  ^ (power)
Commands:
  history  - show past results
  clear    - clear history
  help     - this message
  exit     - quit
Examples:
  3 + 4
  5.2 * 3
  2 ^ 8
""")

def main():
    show_help()
    while True:
        s = input("calc> ").strip()
        if not s:
            continue
        if s.lower() in ("exit","quit"):
            break
        if s.lower() == "help":
            show_help()
            continue
        if s.lower() == "history":
            for i, h in enumerate(history, 1):
                print(f"{i}. {h}")
            continue
        if s.lower() == "clear":
            history.clear()
            print("History cleared.")
            continue
        parts = s.split()
        if len(parts) != 3:
            print("Type 'help' for usage.")
            continue
        a, op, b = parts
        res = calc(a, op, b)
        print("=>", res)
        history.append(f"{a} {op} {b} = {res}")

if __name__ == "__main__":
    main()
