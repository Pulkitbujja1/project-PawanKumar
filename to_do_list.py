import tkinter as tk 
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk,END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning('warning','task cannot be empty!')
    
def remove_task():
    try:
        selected = listbox.courseselection()[0]
        listbox.delelte(selected)
    except IndexError:
        messagebox.showwarning('warning','please select a task to remove!')


def update_task():
    try:
        selected = listbox.curseselection()[0]
        new_task = entry.get()
        if new_task !=  '':
            listbox.delete(selected)
            listbox.insert(selected,new_task)
            entry.delete(0,tk.END)
        else:
            messagebox.showwarning('warning','update task cannot be empty!')
    except IndexError:
        messagebox.showwarning('warning','please select a task to update!')

def Exit_app():
    root.destroy()


root = tk.Tk()
root.title('To-Do List App')
root.geometry('400x400')
root.config(bg = '#f5f5f5')

entry = tk.Entry(root,width = 30 , font = {"Aria",14})
entry.pack(pady = 10)

btn_frame = tk.Frame(root,bg = "#f5f5f5")
btn_frame.pack(pady = 5)

tk.Button(btn_frame, text = "Add Task",width = 10, command = add_task).grid(row = 0,column = 0,padx = 5)
tk.Button(btn_frame, text = "Removal Task",width = 10, command = add_task).grid(row = 0,column = 1,padx = 5)
tk.Button(btn_frame, text = "Update Task",width = 10, command = add_task).grid(row = 0,column = 2,padx = 5)

tk.Button(root,text = 'Exit',width = 10,command = Exit_app).pack(pady = 5)

listbox = tk.Listbox(root, width =40,height = 10,font = {'Arial',12})
listbox.pack(pady = 10)

root.mainloop()