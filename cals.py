import tkinter as tk
from tkinter import messagebox
from datetime import date
import math

#  Common UI Styles 
BG_COLOR = "#e04f4f"  # red background
BTN_COLOR = "#f3b14c"  # orange-golden
FONT_TITLE = ("Times New Roman", 22, "bold", "underline")
FONT_LABEL = ("Times New Roman", 16)
FONT_BUTTON = ("Times New Roman", 14, "bold")

root = tk.Tk()
root.title("Calculation Tool")
root.geometry("600x400")
root.config(bg=BG_COLOR)

#  Helper Function to Open New Window -
def open_window(title):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("600x400")
    win.config(bg=BG_COLOR)
    return win

# ---------- 1. Age Calculator ----------
def age_calculator():
    win = open_window("Age Calculator")
    tk.Label(win, text="Age Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Day:", font=FONT_LABEL, bg=BG_COLOR).pack()
    day_entry = tk.Entry(win, font=FONT_LABEL)
    day_entry.pack()

    tk.Label(win, text="Month:", font=FONT_LABEL, bg=BG_COLOR).pack()
    month_entry = tk.Entry(win, font=FONT_LABEL)
    month_entry.pack()

    tk.Label(win, text="Year:", font=FONT_LABEL, bg=BG_COLOR).pack()
    year_entry = tk.Entry(win, font=FONT_LABEL)
    year_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_age():
        try:
            day = int(day_entry.get())
            month = int(month_entry.get())
            year = int(year_entry.get())
            today = date.today()
            age = today.year - year - ((today.month, today.day) < (month, day))
            result_label.config(text=f"Your age is {age}")
        except:
            messagebox.showerror("Error", "Please enter valid date!")

    tk.Button(win, text="Calculate Age", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_age).pack(pady=10)

# ---------- 2. Percentage Calculator ----------
def percentage_calculator():
    win = open_window("Percentage Calculator")
    tk.Label(win, text="Percentage Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Base Value:", font=FONT_LABEL, bg=BG_COLOR).pack()
    base_entry = tk.Entry(win, font=FONT_LABEL)
    base_entry.pack()

    tk.Label(win, text="Percentage (%):", font=FONT_LABEL, bg=BG_COLOR).pack()
    percent_entry = tk.Entry(win, font=FONT_LABEL)
    percent_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_percent():
        try:
            base = float(base_entry.get())
            percent = float(percent_entry.get())
            result = (base * percent) / 100
            result_label.config(text=f"Result: {result:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_percent).pack(pady=10)

# ---------- 3. Loan Calculator ----------
def loan_calculator():
    win = open_window("Loan Calculator")
    tk.Label(win, text="Loan Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Loan Amount ($):", font=FONT_LABEL, bg=BG_COLOR).pack()
    loan_entry = tk.Entry(win, font=FONT_LABEL)
    loan_entry.pack()

    tk.Label(win, text="Interest Rate (%):", font=FONT_LABEL, bg=BG_COLOR).pack()
    rate_entry = tk.Entry(win, font=FONT_LABEL)
    rate_entry.pack()

    tk.Label(win, text="Loan Term (years):", font=FONT_LABEL, bg=BG_COLOR).pack()
    term_entry = tk.Entry(win, font=FONT_LABEL)
    term_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_loan():
        try:
            P = float(loan_entry.get())
            r = float(rate_entry.get()) / 100 / 12
            n = int(term_entry.get()) * 12
            EMI = (P * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
            result_label.config(text=f"Monthly Payment: ${EMI:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_loan).pack(pady=10)

# ---------- 4. Sales Tax Calculator ----------
def sales_tax_calculator():
    win = open_window("Sales Tax Calculator")
    tk.Label(win, text="Sales Tax Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Purchase Amount ($):", font=FONT_LABEL, bg=BG_COLOR).pack()
    purchase_entry = tk.Entry(win, font=FONT_LABEL)
    purchase_entry.pack()

    tk.Label(win, text="Tax Rate (%):", font=FONT_LABEL, bg=BG_COLOR).pack()
    tax_entry = tk.Entry(win, font=FONT_LABEL)
    tax_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_tax():
        try:
            amount = float(purchase_entry.get())
            rate = float(tax_entry.get())
            total = amount + (amount * rate / 100)
            result_label.config(text=f"Total Amount: ${total:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_tax).pack(pady=10)

# ---------- 5. Probability Calculator ----------
def probability_calculator():
    win = open_window("Probability Calculator")
    tk.Label(win, text="Probability Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Total Outcomes:", font=FONT_LABEL, bg=BG_COLOR).pack()
    total_entry = tk.Entry(win, font=FONT_LABEL)
    total_entry.pack()

    tk.Label(win, text="Favorable Outcomes:", font=FONT_LABEL, bg=BG_COLOR).pack()
    fav_entry = tk.Entry(win, font=FONT_LABEL)
    fav_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_prob():
        try:
            total = float(total_entry.get())
            fav = float(fav_entry.get())
            prob = fav / total
            result_label.config(text=f"Probability: {prob:.4f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_prob).pack(pady=10)

# ---------- 6. BMI Calculator ----------
def bmi_calculator():
    win = open_window("BMI Calculator")
    tk.Label(win, text="BMI Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Height (m):", font=FONT_LABEL, bg=BG_COLOR).pack()
    height_entry = tk.Entry(win, font=FONT_LABEL)
    height_entry.pack()

    tk.Label(win, text="Weight (kg):", font=FONT_LABEL, bg=BG_COLOR).pack()
    weight_entry = tk.Entry(win, font=FONT_LABEL)
    weight_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_bmi():
        try:
            h = float(height_entry.get())
            w = float(weight_entry.get())
            bmi = w / (h ** 2)
            result_label.config(text=f"BMI: {bmi:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_bmi).pack(pady=10)

# ---------- 7. GST Calculator ----------
def gst_calculator():
    win = open_window("GST Calculator")
    tk.Label(win, text="GST Calculator", font=FONT_TITLE, bg=BG_COLOR).pack(pady=15)

    tk.Label(win, text="Amount (₹):", font=FONT_LABEL, bg=BG_COLOR).pack()
    amount_entry = tk.Entry(win, font=FONT_LABEL)
    amount_entry.pack()

    tk.Label(win, text="GST Rate (%):", font=FONT_LABEL, bg=BG_COLOR).pack()
    gst_entry = tk.Entry(win, font=FONT_LABEL)
    gst_entry.pack()

    result_label = tk.Label(win, text="", font=FONT_LABEL, bg=BG_COLOR)
    result_label.pack(pady=10)

    def calc_gst():
        try:
            amount = float(amount_entry.get())
            rate = float(gst_entry.get())
            total = amount + (amount * rate / 100)
            result_label.config(text=f"Total Amount (with GST): ₹{total:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", bg=BTN_COLOR, font=FONT_BUTTON, command=calc_gst).pack(pady=10)

# ---------- Main Menu ----------
tk.Label(root, text="Calculation Tool", font=("Times New Roman", 24, "bold"), bg=BG_COLOR).pack(pady=20)

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

buttons = [
    #("Simple Calculator", lambda: messagebox.showinfo("Info", "Feature Coming Soon!")),
    ("Age Calculator", age_calculator),
    ("Percentage Calculator", percentage_calculator),
    ("Loan Calculator", loan_calculator),
    #("Paypal Calculator", lambda: messagebox.showinfo("Info", "Feature Coming Soon!")),
    ("Sales Tax Calculator", sales_tax_calculator),
    ("Probability Calculator", probability_calculator),
    ("BMI Calculator", bmi_calculator),
    ("GST Calculator", gst_calculator),
]

r, c = 0, 0
for text, cmd in buttons:
    btn = tk.Button(frame, text=text, width=20, height=2, bg=BTN_COLOR, font=FONT_BUTTON, command=cmd)
    btn.grid(row=r, column=c, padx=20, pady=10)
    c += 1
    if c > 1:
        c = 0
        r += 1

root.mainloop()
