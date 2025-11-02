import tkinter as tk
from tkinter import messagebox

# store tasks here
todo_items = []

def refresh_list():
    task_box.delete(0, tk.END)
    for t in todo_items:
        task_box.insert(tk.END, t)

def add_item():
    entry_text = input_field.get()
    if entry_text.strip() != "":
        todo_items.append(entry_text)
        refresh_list()
        input_field.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please type something to add!")

def remove_item():
    try:
        selected = task_box.curselection()[0]
        todo_items.pop(selected)
        refresh_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def edit_item():
    try:
        selected = task_box.curselection()[0]
        new_text = input_field.get()
        if new_text.strip() != "":
            todo_items[selected] = new_text
            refresh_list()
            input_field.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to update!")

# GUI setup
window = tk.Tk()
window.title("To-Do List")

frame = tk.Frame(window)
frame.pack(pady=10)

task_box = tk.Listbox(frame, width=40, height=10, selectmode=tk.SINGLE)
task_box.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

task_box.config(yscrollcommand=scroll.set)
scroll.config(command=task_box.yview)

input_field = tk.Entry(window, width=40)
input_field.pack(pady=5)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=edit_item).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=remove_item).grid(row=0, column=2, padx=5)

window.mainloop()
