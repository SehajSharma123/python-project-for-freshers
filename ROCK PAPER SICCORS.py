import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="Your Choice: " + user_choice)
    comp_label.config(text="Computer Choice: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)

# Heading
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=20)

# Labels
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_label.pack()

comp_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=20)

# Buttons
tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

root.mainloop()
