import tkinter as tk
from tkinter import filedialog
import time

# Function to load an image in GIF/PNG format
def load_image(title):
    root = tk.Tk()
    root.withdraw()  # Hide main window
    path = filedialog.askopenfilename(title=title)
    return tk.PhotoImage(file=path)

# Load main scene and weapon template (GIF/PNG only)
scene = load_image("Select Scene Image (GIF/PNG)")
template = load_image("Select Weapon Template (GIF/PNG)")

scene_width = scene.width()
scene_height = scene.height()
temp_width = template.width()
temp_height = template.height()

found = False

# Simple pixel-by-pixel matching
print("Detecting weapon... (This may take a while for large images)")

for x in range(scene_width - temp_width):
    for y in range(scene_height - temp_height):
        match = True
        for i in range(temp_width):
            for j in range(temp_height):
                if scene.get(x+i, y+j) != template.get(i, j):
                    match = False
                    break
            if not match:
                break
        if match:
            print(f"Weapon detected at coordinates: ({x}, {y})")
            found = True
            break
    if found:
        break

if not found:
    print("No weapon detected in the scene.")
