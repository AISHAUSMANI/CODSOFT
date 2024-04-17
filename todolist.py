import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List GUI")
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.entry = tk.Entry(self.root, width=48)
        self.entry.pack(pady=10)
        
        self.addButton = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.addButton.pack(pady=5)
        
        self.deleteButton = tk.Button(self.root, text="Delete Selected Task", command=self.delete_task)
        self.deleteButton.pack(pady=5)
    
    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except:
            messagebox.showwarning("Warning", "You must select a task to delete.")

def main():
    root = tk.Tk()
    app = ToDoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
