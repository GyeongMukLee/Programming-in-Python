import tkinter as tk

window = tk.Tk()

photo1 = tk.PhotoImage(file="Chapter10/GIF/cat.gif")
photo2 = tk.PhotoImage(file="Chapter10/GIF/cat2.gif")

label1 = tk.Label(window, image=photo1)
label2 = tk.Label(window, image=photo2)
label1.pack(side="left")
label2.pack(side="left")

window.mainloop()
