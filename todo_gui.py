#!/usr/bin/env python3
"""
Simple To-Do GUI using Tkinter. Stores tasks in data/todos.json.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import json, os
from datetime import datetime

BASE = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE, "data")
DATA_FILE = os.path.join(DATA_DIR, "todos.json")

def ensure():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def load():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

class App:
    def __init__(self, root):
        ensure()
        self.root = root
        root.title("Simple To-Do (CODSOFT)")
        self.todos = load()
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        self.listbox = tk.Listbox(self.frame, width=60, height=12)
        self.listbox.pack(side=tk.LEFT, padx=(0,10))
        self.scroll = tk.Scrollbar(self.frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Add", command=self.add).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit", command=self.edit).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Mark Done/Undone", command=self.toggle_done).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=5)
        self.refresh()

    def refresh(self):
        self.todos = load()
        self.listbox.delete(0, tk.END)
        for t in self.todos:
            status = "✔" if t.get("done") else " "
            display = f"[{status}] {t['title']} ({t.get('due','-')}) - {t.get('description','')}"
            self.listbox.insert(tk.END, display)

    def add(self):
        title = simpledialog.askstring("Title", "Task title:")
        if not title:
            return
        desc = simpledialog.askstring("Description", "Description (optional):") or ""
        due = simpledialog.askstring("Due", "Due date YYYY-MM-DD (optional):") or ""
        task = {
            "id": int(datetime.now().timestamp()*1000),
            "title": title,
            "description": desc,
            "due": due,
            "done": False,
            "created_at": datetime.now().isoformat()
        }
        self.todos.append(task)
        save(self.todos)
        self.refresh()

    def get_selected(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showinfo("Select", "Please select a task.")
            return None
        return idx[0]

    def edit(self):
        idx = self.get_selected()
        if idx is None: return
        t = self.todos[idx]
        new_title = simpledialog.askstring("Title", "Task title:", initialvalue=t['title'])
        if not new_title: return
        new_desc = simpledialog.askstring("Description", "Description:", initialvalue=t.get('description','')) or ""
        new_due = simpledialog.askstring("Due", "Due date:", initialvalue=t.get('due','')) or ""
        t['title'] = new_title
        t['description'] = new_desc
        t['due'] = new_due
        save(self.todos)
        self.refresh()

    def delete(self):
        idx = self.get_selected()
        if idx is None: return
        if messagebox.askyesno("Delete", "Delete selected task?"):
            self.todos.pop(idx)
            save(self.todos)
            self.refresh()

    def toggle_done(self):
        idx = self.get_selected()
        if idx is None: return
        t = self.todos[idx]
        t['done'] = not t.get('done', False)
        save(self.todos)
        self.refresh()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

