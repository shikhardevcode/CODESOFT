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
# import tkinter as tk
# from tkinter import messagebox

# def add_task():
#     """Adds the task from the entry box to the listbox."""
#     task = task_entry.get()
#     if task:
#         # Add the task to the end of the listbox
#         task_listbox.insert(tk.END, task)
#         # Clear the entry box after adding
#         task_entry.delete(0, tk.END)
#     else:
#         # Show a simple error pop-up if the entry is empty
#         messagebox.showwarning("Warning", "You must enter a task.")

# def delete_task():
#     """Deletes the currently selected task from the listbox."""
#     try:
#         # Get the index of the selected item
#         selected_task_index = task_listbox.curselection()[0]
#         # Delete the item at that index
#         task_listbox.delete(selected_task_index)
#     except IndexError:
#         # This error happens if the user clicks "Delete" without selecting a task
#         messagebox.showwarning("Warning", "You must select a task to delete.")

# def mark_task_complete():
#     """Marks the selected task as complete by changing its background color."""
#     try:
#         selected_task_index = task_listbox.curselection()[0]
#         # Change the background and foreground color of the selected item
#         task_listbox.itemconfig(
#             selected_task_index,
#             {'bg': '#d9d9d9', 'fg': '#888'}  # Light grey background, darker grey text
#         )
#         # We can also 'deselect' it so it's clear it's done
#         task_listbox.selection_clear(0, tk.END)
#     except IndexError:
#         messagebox.showwarning("Warning", "You must select a task to mark as complete.")

# # --- Set up the main application window ---
# root = tk.Tk()
# root.title("My To-Do List")
# root.geometry("400x500")  # Set the window size (width x height)

# # --- Create the main frame ---
# # We use a frame to hold all our other widgets
# frame = tk.Frame(root)
# frame.pack(pady=10) # pack() places the widget in the window

# # --- Create the widgets ---

# # 1. The Entry widget for new tasks
# task_entry = tk.Entry(frame, width=30, font=('Helvetica', 12))
# task_entry.pack(side=tk.LEFT, padx=(0, 10))

# # 2. The "Add Task" button
# add_button = tk.Button(
#     frame,
#     text="Add Task",
#     command=add_task,  # This links the button to our function
#     bg="#4CAF50",      # Green background
#     fg="white",        # White text
#     font=('Helvetica', 10, 'bold')
# )
# add_button.pack(side=tk.LEFT)

# # 3. The Listbox to display all tasks
# listbox_frame = tk.Frame(root)
# listbox_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# task_listbox = tk.Listbox(
#     listbox_frame,
#     height=15,
#     width=50,
#     font=('Helvetica', 12),
#     selectbackground="#a6a6a6" # Color when an item is selected
# )
# task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

# # 4. Add a Scrollbar to the listbox
# scrollbar = tk.Scrollbar(listbox_frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # Link the scrollbar to the listbox
# task_listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=task_listbox.yview)


# # 5. The action buttons (Delete, Mark Complete)
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)

# delete_button = tk.Button(
#     button_frame,
#     text="Delete Task",
#     command=delete_task,
#     bg="#f44336",  # Red background
#     fg="white",
#     font=('Helvetica', 10, 'bold')
# )
# delete_button.pack(side=tk.LEFT, padx=10)

# complete_button = tk.Button(
#     button_frame,
#     text="Mark Complete",
#     command=mark_task_complete,
#     bg="#2196F3",  # Blue background
#     fg="white",
#     font=('Helvetica', 10, 'bold')
# )
# complete_button.pack(side=tk.LEFT)


# # --- Start the application's main loop ---
# # This line keeps the window open and listening for user actions
# root.mainloop()
