import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store data
FILE_NAME = "todo_data.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                tasks = json.load(file)
                for task in tasks:
                    listbox.insert(tk.END, task)
            except:
                pass

# Save tasks
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        json.dump(list(tasks), file)

# Add task
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Mark as done
def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        if not task.startswith("✔ "):
            listbox.delete(selected)
            listbox.insert(tk.END, "✔ " + task)
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Clear all tasks
def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

# UI Setup
root = tk.Tk()
root.title("Smart To-Do Manager")
root.geometry("420x520")
root.config(bg="#1e272e")

title = tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#1e272e", fg="white")
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=15, font=("Arial", 12), bg="#d2dae2")
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e272e")
btn_frame.pack()

tk.Button(btn_frame, text="Add", width=12, command=add_task, bg="#05c46b", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_task, bg="#ff3f34", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Done", width=12, command=mark_done, bg="#0fbcf9", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Clear All", width=12, command=clear_all, bg="#ffa801", fg="white").grid(row=1, column=1, padx=5, pady=5)

# Load saved tasks
load_tasks()

root.mainloop()