import tkinter as tk

def add():
    listbox.insert(tk.END, entry.get())
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Todo List")
root.geometry("300x300")
root.configure(bg="#ffe1f9")

frame = tk.Frame(root,bg="#ffecfb")
frame.pack(fill="both", padx=10, pady=5)

entry = tk.Entry(frame)
entry.pack(expand=True)

listbox = tk.Listbox(frame)
listbox.pack(
    fill="both", 
    expand=True, 
    padx=10, 
    pady=10
)

btn = tk.Button(
    frame,
    bg="#ffecfb",
    fg="#ff89e5",
    text="추가",
    activeforeground="white",
    command=add,
    relief="flat", 
    bd=0
)
btn.pack()

root.mainloop()
