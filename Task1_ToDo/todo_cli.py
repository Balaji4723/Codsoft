#!/usr/bin/env python3
"""
Simple To-Do CLI app (stores tasks in data/todos.json).
Features: add, list, update, delete, search, mark done.
"""

import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATA_FILE = os.path.join(DATA_DIR, "todos.json")

def ensure_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def load_todos():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_task():
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    desc = input("Description (optional): ").strip()
    due = input("Due date (YYYY-MM-DD, optional): ").strip()
    task = {
        "id": int(datetime.now().timestamp()*1000),
        "title": title,
        "description": desc,
        "due": due,
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print("Task added.")

def list_tasks(show_all=True):
    todos = load_todos()
    if not todos:
        print("No tasks.")
        return
    for t in todos:
        if not show_all and t.get("done"):
            continue
        status = "✔" if t.get("done") else " "
        print(f"[{status}] {t['id']} - {t['title']} (due: {t.get('due','-')})")
        if t.get("description"):
            print("    ", t["description"])

def find_task_by_id(task_id):
    todos = load_todos()
    for t in todos:
        if str(t["id"]) == str(task_id):
            return t
    return None

def delete_task():
    task_id = input("Enter task id to delete: ").strip()
    todos = load_todos()
    new = [t for t in todos if str(t["id"]) != task_id]
    if len(new) == len(todos):
        print("Task not found.")
    else:
        save_todos(new)
        print("Deleted.")

def mark_done(mark=True):
    task_id = input("Enter task id: ").strip()
    todos = load_todos()
    changed = False
    for t in todos:
        if str(t["id"]) == task_id:
            t["done"] = bool(mark)
            changed = True
            break
    if changed:
        save_todos(todos)
        print("Updated.")
    else:
        print("Task not found.")

def update_task():
    task_id = input("Enter task id to update: ").strip()
    todos = load_todos()
    for t in todos:
        if str(t["id"]) == task_id:
            print("Leave blank to keep current value.")
            new_title = input(f"Title [{t['title']}]: ").strip()
            new_desc = input(f"Description [{t.get('description','')}]: ").strip()
            new_due = input(f"Due [{t.get('due','')}]: ").strip()
            if new_title:
                t['title'] = new_title
            if new_desc:
                t['description'] = new_desc
            if new_due:
                t['due'] = new_due
            save_todos(todos)
            print("Updated.")
            return
    print("Task not found.")

def search_tasks():
    q = input("Search query: ").strip().lower()
    todos = load_todos()
    results = [t for t in todos if q in t['title'].lower() or q in t.get('description','').lower()]
    if not results:
        print("No matches.")
        return
    for t in results:
        print(f"{t['id']} - {t['title']} (done: {t['done']})")

def show_help():
    print("""
Commands:
 add      - add new task
 list     - list all tasks
 list-pending - list only pending tasks
 update   - update task by id
 delete   - delete task by id
 done     - mark task done
 undone   - mark task undone
 search   - search tasks by keyword
 help     - show this help
 exit     - quit
""")

def main():
    ensure_data()
    show_help()
    while True:
        cmd = input("cmd> ").strip().lower()
        if cmd == "add":
            add_task()
        elif cmd == "list":
            list_tasks(show_all=True)
        elif cmd == "list-pending":
            list_tasks(show_all=False)
        elif cmd == "update":
            update_task()
        elif cmd == "delete":
            delete_task()
        elif cmd == "done":
            mark_done(True)
        elif cmd == "undone":
            mark_done(False)
        elif cmd == "search":
            search_tasks()
        elif cmd == "help":
            show_help()
        elif cmd in ("exit","quit"):
            break
        else:
            print("Unknown command. Type help.")

if __name__ == "__main__":
    main()
