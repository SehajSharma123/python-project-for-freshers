'''
from tkinter import*
import calendar

def calendarsee():
    window=Tk()
    window.config(bg="pink")
    window.title("year calendar")
    window.geometry("570x620")
    getyear=int(yearentry.get())
    windowcontent=calendar.calendar(getyear)
    yearcal=Label(window,text=windowcontent,font=("Arial",12,"bold"))
    yearcal.grid(row=5,column=1)
    window.mainloop()
    

if  __name__ =="__main__":
    root=Tk()
    root.config(bg="yellow")
    root.title("GUI CALENDAR")
    root.geometry("280x170")
    
    name=Label(root,text="CALENDAR",bg="light pink",font=("Arial",20,"bold"))
    name.grid(row=1,column=1)
    
    year=Label(root,text="enter year",bg="light blue",font=("Arial",15,"bold"))
    year.grid(row=2,column=1)

    yearentry=Entry(root,font=("Arial",15,"bold"))
    yearentry.grid(row=3,column=1)

    
    showbutton= Button(root,text="show calendar",
    fg="red",bg="black",font=("Arial",15,"bold"),command=calendarsee())
    showbutton.grid(row=4,colomn=1)
    
    root.mainloop()
'''
from tkinter import *
import calendar

def calendarsee():
    # create new window
    window = Tk()
    window.config(bg="pink")
    window.title("Calendar")
    
    # get year from entry box
    getyear = int(yearentry.get())
    windowcontent = calendar.calendar(getyear)

    # label to show calendar
    yearcal = Label(window, text=windowcontent, font=("Arial", 12, "bold"), bg="pink")
    yearcal.grid(row=5, column=1)

    window.mainloop()

# main window
root = Tk()
root.config(bg="light yellow")
root.title("CALENDAR")
root.geometry("280x170")

# title label
namelabel = Label(root, text="CALENDAR", bg="light pink", font=("Arial", 20, "bold"))
namelabel.grid(row=1, column=1)

# year label & entry
yearlabel = Label(root, text="Enter Year", bg="light blue", font=("Arial", 15, "bold"))
yearlabel.grid(row=2, column=1)

yearentry = Entry(root, font=("Arial", 15, "bold"))
yearentry.grid(row=3, column=1)

# button
showbutton = Button(root, text="Show Calendar", fg="red", bg="black",
                    font=("Arial", 15, "bold"), command=calendarsee)
showbutton.grid(row=4, column=1)

root.mainloop()





















