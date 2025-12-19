import tkinter as tk
from tkinter.filedialog import askopenfile , asksaveasfilename
def savefile():
    fileloc=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("text files","*.txt"),["all files","*"]])
    if not fileloc:
        return
    with open(fileloc,"w")as fileoutput:
        text=textedit.get(1.0,tk.END)
        fileoutput.write(text)
    root.title(f"my notepad-{fileloc}")
def openfile():
    fileloc=askfilenamefilename(
       filetypes=[("text files","*.txt"),["all files","*"]])
    if not fileloc:
        return
    textedit.delete(1.0,tk.END)
    with open(fileloc,"r")as fileintput:
        text=fileinput.read()
        textedit.insert(tk.END,text)
    root.title(f"my notepad-{fileloc}")   

root=tk.Tk()
root.title("my notepad")
root.rowconfigure(0,minsize=800)
root.columnconfigure(1,minsize=800)

textedit=tk.Text(root)
textedit.grid(row=0,column=1,sticky="nsew")

framebutton=tk.Frame(root,relief=tk.RAISED,bd=3)
framebutton.grid(row=0,column=0,sticky="ns")

buttonopen=tk.Button(framebutton, text="open file",command=openfile)
buttonopen.grid(row=0,column=0,padx=5,pady=5)


buttonsave=tk.Button(framebutton, text="save file",command=savefile)
buttonsave.grid(row=1,column=0,padx=5,pady=5)



root.mainloop()
