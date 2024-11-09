import tkinter as tk
from tkinter import messagebox
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")
        self.root.config(bg="#f5f5f5")

        self.tasks = []
        self.load_tasks()

        # Title Label
        title = tk.Label(self.root, text="To-Do List Application", font=("Helvetica", 16), bg="#f5f5f5")
        title.pack(pady=10)

        # Task Entry Frame
        entry_frame = tk.Frame(self.root, bg="#f5f5f5")
        entry_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(entry_frame, width=35, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10)
        
        add_task_button = tk.Button(entry_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        add_task_button.grid(row=0, column=1)

        # Task List Frame
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg="#f5f5f5")
        buttons_frame.pack(pady=10)

        delete_button = tk.Button(buttons_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=("Helvetica", 12))
        delete_button.grid(row=0, column=0, padx=10)
        
        mark_button = tk.Button(buttons_frame, text="Mark as Completed", command=self.mark_completed, bg="#2196F3", fg="white", font=("Helvetica", 12))
        mark_button.grid(row=0, column=1, padx=10)
        
        save_button = tk.Button(buttons_frame, text="Save Tasks", command=self.save_tasks, bg="#FFC107", fg="black", font=("Helvetica", 12))
        save_button.grid(row=0, column=2, padx=10)

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to delete.")

    def mark_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to mark as completed.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            task_text = task["task"]
            if task["completed"]:
                task_text += " ✔"  # Mark completed tasks with a checkmark
            self.task_listbox.insert(tk.END, task_text)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Save Successful", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
