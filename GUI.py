#tkinter GUI
def greet():
    print("i am just a girl")

from tkinter import *
root=Tk()

root.maxsize(700,500)
root.minsize(150,200)
root.geometry("500x500")
root.resizable(0,0)
root.config(bg='pink')
root.title("GUI;)")

l=Label(root, text="I am learning GUI on python", fg='blue',bg='beige',
                font=("Times New Roman", 14, 'bold', 'underline',
                      'italic'))
l.pack()                
l=Label(root,text="hi hello", fg='blue',bg='beige',
                font=("Times New Roman", 14, 'bold','underline',
                      'italic'),width=20,bd=15,relief='sunken')
                
l.pack(pady=20,padx=20,side="left")
root.mainloop()

e=Entry(root,width=10,font=("Times New Roman", 25, 'bold','underline',
                      'italic'),bd=15,relief='sunken')
e.pack()
b=Button(root,text='submit',font=("bold", 25, 'bold','underline',
                      'italic'),width=10,bd=5,relief='sunken',command=greet)
b.pack()
