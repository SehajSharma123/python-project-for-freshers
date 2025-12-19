import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Scissor Paper")
root.geometry("900x400")
root.configure(bg="black")
root.resizable(False, False)

computer_score = 0
user_score = 0
choices = ["Rock", "Paper", "Scissor"]

# ---------- FUNCTIONS ----------
def play(user_choice):
    global computer_score, user_score

    computer_choice = random.choice(choices)

    comp_choice_label.config(text=computer_choice.upper())
    user_choice_label.config(text=user_choice.upper())

    if user_choice == computer_choice:
        result_label.config(text="TIE", fg="yellow")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        user_score += 1
        result_label.config(text="YOU WIN", fg="green")
    else:
        computer_score += 1
        result_label.config(text="COMPUTER WINS", fg="red")

    comp_score_label.config(text=str(computer_score))
    user_score_label.config(text=str(user_score))


# ---------- TOP LABELS ----------
tk.Label(root, text="COMPUTER", bg="orange", fg="blue",
         font=("Arial", 16, "bold"), width=15).place(x=50, y=20)

tk.Label(root, text="USER", bg="orange", fg="blue",
         font=("Arial", 16, "bold"), width=15).place(x=650, y=20)

# ---------- CHOICE DISPLAY ----------
comp_choice_label = tk.Label(root, text="?", bg="white",
                             font=("Arial", 24, "bold"), width=10)
comp_choice_label.place(x=50, y=80)

user_choice_label = tk.Label(root, text="?", bg="white",
                             font=("Arial", 24, "bold"), width=10)
user_choice_label.place(x=650, y=80)

# ---------- SCORE ----------
comp_score_label = tk.Label(root, text="0", fg="red",
                            bg="black", font=("Arial", 24, "bold"))
comp_score_label.place(x=260, y=120)

user_score_label = tk.Label(root, text="0", fg="red",
                            bg="black", font=("Arial", 24, "bold"))
user_score_label.place(x=560, y=120)

# ---------- RESULT ----------
result_label = tk.Label(root, text="", bg="black",
                        font=("Arial", 20, "bold"))
result_label.place(x=350, y=80)

# ---------- BUTTONS ----------
btn_style = {
    "font": ("Arial", 14, "bold"),
    "bg": "yellow",
    "fg": "red",
    "width": 12,
    "height": 2
}

tk.Button(root, text="ROCK",
          command=lambda: play("Rock"), **btn_style).place(x=200, y=260)

tk.Button(root, text="PAPER",
          command=lambda: play("Paper"), **btn_style).place(x=380, y=260)

tk.Button(root, text="SCISSOR",
          command=lambda: play("Scissor"), **btn_style).place(x=560, y=260)

root.mainloop()
