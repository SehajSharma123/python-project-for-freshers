import tkinter as tk
from tkinter import messagebox
import sqlite3


con = sqlite3.connect("sehajaaadyvanshi.db")
cur = con.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT PRIMARY KEY,
    password TEXT
)
""")
con.commit()


#  Register Window
def register_window():
    reg = tk.Toplevel(root)
    reg.title("User Register Form")
    reg.config(bg="indianred")
    reg.geometry("600x350")

    # Heading
    tk.Label(
        reg,
        text="User Register Form",
        bg="indianred",
        fg="black",
        font=("Times New Roman", 20, "bold", "underline")
    ).pack(pady=10)

    # Labels
    tk.Label(reg, text="Name:", bg="indianred", fg="black", font=("Arial", 12, "bold")).place(x=100, y=80)
    tk.Label(reg, text="Email:", bg="indianred", fg="black", font=("Arial", 12, "bold")).place(x=100, y=120)
    tk.Label(reg, text="Password:", bg="indianred", fg="black", font=("Arial", 12, "bold")).place(x=100, y=160)
    tk.Label(reg, text="Confirm Password:", bg="indianred", fg="black", font=("Arial", 12, "bold")).place(x=100, y=200)

    # Entries
    name_entry = tk.Entry(reg, width=30)
    email_entry = tk.Entry(reg, width=30)
    pass_entry = tk.Entry(reg, width=30, show="*")
    conf_entry = tk.Entry(reg, width=30, show="*")

    name_entry.place(x=280, y=80)
    email_entry.place(x=280, y=120)
    pass_entry.place(x=280, y=160)
    conf_entry.place(x=280, y=200)

    # Submit function
    def submit():
        name = name_entry.get()
        email = email_entry.get()
        password = pass_entry.get()
        confirm = conf_entry.get()

        if not (name and email and password and confirm):
            messagebox.showerror("Error", "All fields are required")
            return

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            con.commit()
            messagebox.showinfo("Success", "Registration Successful")
            reg.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists")

    # Button
    tk.Button(
        reg,
        text="Submit",
        bg="gold",
        fg="black",
        font=("Arial", 12, "bold"),
        width=10,
        command=submit
    ).place(x=250, y=250)


#  Login Window 
def login_window():
    log = tk.Toplevel(root)
    log.title("Calculation Tool")
    log.config(bg="indianred")
    log.geometry("500x250")

    # Heading
    tk.Label(
        log,
        text="Login",
        bg="indianred",
        fg="black",
        font=("Times New Roman", 20, "bold", "underline")
    ).pack(pady=10)

    # Labels
    tk.Label(log, text="Email Id:", bg="indianred", fg="black", font=("Arial", 12, "bold")).place(x=100, y=80)
    tk.Label(log, text="Password:", bg="indianred", fg="black", font=("Arial", 12, "bold")).place(x=100, y=120)

    # Entries
    email_entry = tk.Entry(log, width=30)
    pass_entry = tk.Entry(log, width=30, show="*")

    email_entry.place(x=220, y=80)
    pass_entry.place(x=220, y=120)

    # Login function
    def login():
        email = email_entry.get()
        password = pass_entry.get()

        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        row = cur.fetchone()

        if row:
            print("Successful")   # Prints in Python shell
            messagebox.showinfo("Success", f"Welcome, {row[0]}!")
            log.destroy()
        else:
            print("Try Again")    # Prints in Python shell
            messagebox.showerror("Error", "Invalid Email or Password")

    # Button
    tk.Button(
        log,
        text="login",
        bg="gold",
        fg="black",
        font=("Arial", 12, "bold"),
        width=10,
        command=login
    ).place(x=210, y=170)


#  Main Root Window 
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")
root.config(bg="navy")

tk.Button(
    root,
    text="Register",
    bg="gold",
    fg="black",
    font=("Arial", 12, "bold"),
    width=12,
    command=register_window
).pack(pady=25)

tk.Button(
    root,
    text="Login",
    bg="gold",
    fg="black",
    font=("Arial", 12, "bold"),
    width=12,
    command=login_window
).pack(pady=10)

root.mainloop()
