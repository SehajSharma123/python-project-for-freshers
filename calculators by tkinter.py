from tkinter import *
import math

    
root=Tk()
root.title('Calculator')


def btnClick(number):
    global operator
    operator=operator + str(number)
    textvalue.set(operator)
def btnclear():
    global operator
    operator=""
    textvalue.set("")

def btnequal():
    global operator
    result=str(eval(operator))
    textvalue.set(result)


    
root.config(bg="#fecd53")
operator=""
#-------------color= powder blue, #fecd53 ,burlywood,------------s
textvalue=StringVar()
textentry=Entry(root,font="arial 20 bold" ,bg="#fecd53",textvariable=textvalue,bd=25, justify="right").grid(columnspan=4)

btn7=Button(root,text="7", padx=15,bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(root,text="8", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,text="9", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold", command=lambda:btnClick(9)).grid(row=1,column=2)
addition=Button(root,text="+", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick("+")).grid(row=1,column=3)

btn4=Button(root,text="4", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold", command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(root,text="5", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(root,text="6", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold", command=lambda:btnClick(6)).grid(row=2,column=2)
subtraction=Button(root,text="-", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick("-")).grid(row=2,column=3)

btn1=Button(root,text="1", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(root,text="2", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(root,text="3", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(3)).grid(row=3,column=2)
multiplay=Button(root,text="*", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick("*")).grid(row=3,column=3)

btn0=Button(root,text="0", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick(0)).grid(row=4,column=0)
clear=Button(root,text="C", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold", command=btnclear).grid(row=4,column=1)
equal=Button(root,text="=", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=btnequal).grid(row=4,column=2)
divide=Button(root,text="/", padx=15, bd=5,fg="black", bg="#fecd53",font="arial 20 bold",command=lambda:btnClick("/")).grid(row=4,column=3)






root.mainloop()
