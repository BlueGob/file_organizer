import tkinter as tk
from tkinter import messagebox
import file_organizer as f
x=""
window = tk.Tk()
#window.iconphoto(False, tk.PhotoImage(file='ico.png'))
window.title("path")
def get_input():
    x= inputtxt.get(1.0, "end-1c")
    if(x != ""):
        p1 = f.Organize()
        p1.set_path(x)
        if(p1.check_path() == True):
            p1.CreateDirectory()
            p1.organize()
            tk.messagebox.showinfo(title="job done", message="you folder has been well organized !")
            window.destroy()
        else:
             tk.messagebox.showinfo(title="Error", message="incorrect path !")
    else:
        tk.messagebox.showinfo(title="Error", message="path no specified !")
    

message = tk.Label(text = "please specify the path of the folder", font=("Arial", 14))
inputtxt = tk.Text(window, height = 3,
                width = 40,
                bg = "white")

message.pack(padx=6, pady=20)
inputtxt.pack(padx=6, pady=30)
button = tk.Button(
    text="Organize now !",
    width=40,
    height=2,
    bg="green",
    fg="yellow",
    command=get_input
)
button.pack(padx=6, pady=10)

window.mainloop()
