import tkinter as tk
import random

# ---------- CONSTANTS ----------
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
SPEED = 120

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="red")
canvas.pack()

score = 0
direction = "Right"

# ---------- SCORE TEXT ----------
score_text = canvas.create_text(
    WIDTH // 2, 15,
    text="Enjoy the snake game .... Your Score: 0",
    fill="yellow",
    font=("Arial", 14, "bold")
)

# ---------- SNAKE ----------
snake = [(100, 100), (80, 100), (60, 100)]
snake_body = []

for x, y in snake:
    snake_body.append(
        canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="black")
    )

# ---------- FOOD ----------
food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
food_y = random.randrange(30, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
food = canvas.create_oval(
    food_x, food_y,
    food_x + SNAKE_SIZE, food_y + SNAKE_SIZE,
    fill="green"
)

# ---------- FUNCTIONS ----------
def change_direction(event):
    global direction
    if event.keysym in ["Up", "Down", "Left", "Right"]:
        direction = event.keysym

def move_snake():
    global score

    head_x, head_y = snake[0]

    if direction == "Up":
        new_head = (head_x, head_y - SNAKE_SIZE)
    elif direction == "Down":
        new_head = (head_x, head_y + SNAKE_SIZE)
    elif direction == "Left":
        new_head = (head_x - SNAKE_SIZE, head_y)
    else:
        new_head = (head_x + SNAKE_SIZE, head_y)

    # Game over conditions
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 30 or new_head[1] >= HEIGHT):
        canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 30, "bold")
        )
        return

    snake.insert(0, new_head)

    # Check food collision
    if new_head == (food_x, food_y):
        score += 1
        canvas.itemconfig(score_text, text=f"Enjoy the snake game .... Your Score: {score}")
        create_food()
    else:
        snake.pop()

    redraw_snake()
    root.after(SPEED, move_snake)

def redraw_snake():
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(
            x, y, x + SNAKE_SIZE, y + SNAKE_SIZE,
            fill="black", tags="snake"
        )

def create_food():
    global food_x, food_y
    canvas.delete(food)
    food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
    food_y = random.randrange(30, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
    canvas.create_oval(
        food_x, food_y,
        food_x + SNAKE_SIZE, food_y + SNAKE_SIZE,
        fill="green"
    )

# ---------- KEY BINDINGS ----------
root.bind("<KeyPress>", change_direction)

# ---------- START GAME ----------
move_snake()
root.mainloop()
