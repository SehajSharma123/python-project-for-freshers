#clock


from tkinter import *
from tkinter import strftime

def clk():
    data=strftime('%d.%m.%Y  %I:%M:%S %p')
    l.config(text=data)
    root.after(1000,clk)
root=Tk()
l=label(root,fg="red",bg="black",font=("Times New Roman ",35,"bold"))
l.pack()
clk()
root.mainloop()
