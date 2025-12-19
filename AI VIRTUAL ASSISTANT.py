# AI Desktop Assistant using Python and Tkinter

import tkinter as tk
from tkinter import messagebox
import webbrowser
import datetime
import os

# Function to handle commands
def run_command():
    command = entry.get().lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        result.set("Opening YouTube...")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        result.set("Opening Google...")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        result.set(f"Current time is {now}")
    elif "exit" in command:
        root.destroy()
    else:
        result.set("Sorry, I don't understand that command.")

# Tkinter GUI
root = tk.Tk()
root.title("AI Desktop Assistant")
root.geometry("500x300")
root.config(bg="#ddeeff")

# Title Label
title = tk.Label(root, text="AI Desktop Assistant", font=("Helvetica", 18, "bold"), bg="#ddeeff")
title.pack(pady=10)

# Entry for commands
entry = tk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=20)

# Button to run command
btn = tk.Button(root, text="Run Command", font=("Helvetica", 14), command=run_command)
btn.pack(pady=10)

# Label to show results
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 14), bg="#ddeeff")
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()
