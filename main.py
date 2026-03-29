import tkinter as tk

def add():
    listbox.insert(tk.END, entry.get())
    entry.delete(0, tk.END)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

listbox = tk.Listbox(root)
listbox.pack()

btn = tk.Button(root, text="추가",command=add)
btn.pack()

root.title("Todo List")
root.mainloop()

#chatgpt 확인하고 계속 만들기