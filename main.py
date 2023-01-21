import tkinter as tk
import time

form = tk.Tk()

form.title("Dijital Saat")
form.geometry("750x375")
form.config(bg="blue")

def zaman():
    zaman_format=time.strftime("%H:%M:%S")
    zmn_label.config(text=zaman_format)
    zmn_label.after(200,zaman)


zmn_label=tk.Label(bg="white",font=("bold",100))
zmn_label.place(x=120,y=100)
zaman()

form.mainloop()
