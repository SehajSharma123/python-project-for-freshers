#event handling
#bind


from tkinter import *
root=Tk()

root.geometry("500x500")
def show(event):
    root.config(bg="pink")
def show1(event):
    root.config(bg="blue")
def show3(event):
    root.config(bg="red")
def show4(event):
    root.config(bg="orange")    
b=Button(root,text='click')
b.bind("<Button-1>",show)#left click
b.bind("<Button-3>",show1)#right click

root.bind("<Enter>",show3)
root.bind("<Leave>",show4)

root.bind("<Key-a>",show4)
root.bind("<Key-b>",show4)
 
root.bind("<Shift-Left>",show1)
root.bind("<Shift-Right>",show)

b.pack()
root.mainloop()
