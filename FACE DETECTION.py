from tkinter import *
from tkinter import filedialog

def open_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("PNG Images", ".png"), ("JPEG Images", ".jpg")])
    if img_path:
        canvas.delete("all")
        img = PhotoImage(file=img_path)
        canvas.image = img  # Keep reference
        canvas.create_image(0, 0, anchor=NW, image=img)

def draw_rectangle(event):
    x1, y1 = event.x - 20, event.y - 20
    x2, y2 = event.x + 20, event.y + 20
    canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2)

root = Tk()
root.title("Face Detection Demo")
root.geometry("500x500")

btn = Button(root, text="Open Image", command=open_image)
btn.pack(pady=10)

canvas = Canvas(root, width=480, height=400)
canvas.pack()

canvas.bind("<Button-1>", draw_rectangle)  # Click to mark face

root.mainloop()
