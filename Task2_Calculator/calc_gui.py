#!/usr/bin/env python3
"""
Simple Calculator GUI (Tkinter).
Basic arithmetic + clear + backspace + decimal.
"""

import tkinter as tk

class CalcApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator (CODSOFT)")
        self.expr = ""
        self.entry = tk.Entry(root, font=("Arial", 20), bd=4, relief=tk.RIDGE, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, ipady=8)
        btns = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
        ]
        for (text,r,c) in btns:
            tk.Button(root, text=text, width=6, height=2, font=("Arial",14),
                      command=lambda t=text: self.on_click(t)).grid(row=r, column=c, padx=4, pady=4)
        tk.Button(root, text="C", width=6, height=1, font=("Arial",12), command=self.clear).grid(row=5, column=0, pady=6)
        tk.Button(root, text="⌫", width=6, height=1, font=("Arial",12), command=self.backspace).grid(row=5, column=1, pady=6)
        tk.Button(root, text="±", width=6, height=1, font=("Arial",12), command=self.plusminus).grid(row=5, column=2, pady=6)
        tk.Button(root, text="%", width=6, height=1, font=("Arial",12), command=lambda: self.on_click('%')).grid(row=5, column=3, pady=6)

    def on_click(self, ch):
        if ch == "=":
            try:
                # safely evaluate basic math
                expr = self.expr.replace('^', '**')
                result = eval(expr, {"__builtins__":None}, {})
                self.expr = str(result)
            except Exception:
                self.expr = "Error"
        else:
            self.expr += ch
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expr)

    def clear(self):
        self.expr = ""
        self.entry.delete(0, tk.END)

    def backspace(self):
        self.expr = self.expr[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expr)

    def plusminus(self):
        # toggle sign for current expression if possible
        try:
            if self.expr.startswith('-'):
                self.expr = self.expr[1:]
            else:
                self.expr = '-' + self.expr
        except Exception:
            pass
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expr)

if __name__ == "__main__":
    root = tk.Tk()
    CalcApp(root)
    root.mainloop()
