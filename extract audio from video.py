import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Function to extract audio
def extract_audio():
    # Get the file paths
    video_file = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", ".mp4;.mkv;*.avi")])
    
    if not video_file:
        return
    
    # Ask user for output audio file path
    audio_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    
    if not audio_file:
        return
    
    try:
        # Path for FFmpeg executable (keep the ffmpeg.exe in the same directory as this script)
        ffmpeg_path = "./ffmpeg"  # Or specify full path like "C:/ffmpeg/bin/ffmpeg.exe"

        # Run the FFmpeg command to extract audio
        command = [ffmpeg_path, "-i", video_file, "-vn", "-acodec", "mp3", audio_file]
        subprocess.run(command, check=True)

        # Success message
        messagebox.showinfo("Success", "Audio extracted successfully!")
    
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "An error occurred while extracting audio.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create Tkinter window
root = tk.Tk()
root.title("Audio Extractor")
root.geometry("300x150")

# Create a button to extract audio
extract_button = tk.Button(root, text="Extract Audio from Video", command=extract_audio)
extract_button.pack(pady=40)

# Run the Tkinter event loop
root.mainloop()
