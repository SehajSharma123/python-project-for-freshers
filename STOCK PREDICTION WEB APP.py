import tkinter as tk

# ---------- Sample stock data ----------
# Simulated last 10 days closing prices
stock_data = [150, 152, 153, 151, 154, 155, 156, 158, 157, 159]

# ---------- Function to predict ----------
def predict_stock():
    try:
        n = int(days_entry.get())
        if n <= 0:
            result_label.config(text="Enter positive number of days")
            return
    except:
        result_label.config(text="Enter valid number")
        return

    # Simple prediction using moving average of last 3 days
    predictions = []
    data = stock_data.copy()
    for _ in range(n):
        avg = sum(data[-3:]) / 3  # average of last 3 days
        predictions.append(round(avg, 2))
        data.append(avg)  # append prediction for next iteration

    # Display prediction
    result_text = "Predicted prices for next {} days:\n".format(n)
    for i, price in enumerate(predictions, 1):
        result_text += "Day {}: ${}\n".format(i, price)

    result_label.config(text=result_text)

# ---------- GUI ----------
root = tk.Tk()
root.title("Stock Prediction App")
root.geometry("500x400")
root.configure(bg="#1e1e2f")

# Heading
tk.Label(root, text="Stock Prediction Web App", font=("Arial", 18, "bold"),
         fg="yellow", bg="#1e1e2f").pack(pady=20)

# Show last stock prices
tk.Label(root, text="Last 10 days prices: " + ", ".join(map(str, stock_data)),
         fg="white", bg="#1e1e2f", font=("Arial", 12)).pack(pady=10)

# Input
tk.Label(root, text="Enter number of days to predict:", fg="white",
         bg="#1e1e2f", font=("Arial", 12)).pack(pady=5)
days_entry = tk.Entry(root, font=("Arial", 12))
days_entry.pack(pady=5)

# Predict button
tk.Button(root, text="Predict", font=("Arial", 12, "bold"), bg="yellow", fg="black",
          command=predict_stock).pack(pady=10)

# Result
result_label = tk.Label(root, text="", fg="lightgreen", bg="#1e1e2f",
                        font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
