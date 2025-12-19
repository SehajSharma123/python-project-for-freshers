from tkinter import Tk
from tkinter import Label #to write
import time
root=Tk()
root.title("clock")
def present_time():
    display_time=time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)
digi_clock=Label(root,fg="red",bg="black",font=("Times New Roman ",35,"bold"))
digi_clock.pack()

present_time()



root.mainloop()
