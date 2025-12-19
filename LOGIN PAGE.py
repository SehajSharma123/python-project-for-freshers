import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# Pre-defined username and password
USER_CREDENTIALS = {"admin": "12345", "user": "password"}

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Labels
tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=10)

# Run the GUI
root.mainloop()
