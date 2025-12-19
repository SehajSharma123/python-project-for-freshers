import webbrowser
import urllib.parse
import time

print("=== WhatsApp Message Automation (No Installation) ===")

# Input from user
number = input("Enter WhatsApp number with country code (e.g., +917626836995): ")
message = input("Enter the message: hi  ")

# Encode message for URL
encoded_msg = urllib.parse.quote(message)

# Create WhatsApp URL
url = f"https://wa.me/{+917626836995}?text={"hi"}"

print("\nOpening WhatsApp Web...")
time.sleep(1)

# Open browser with WhatsApp chat
webbrowser.open(url)

print("\nYour message is ready in WhatsApp Web.")
print("Just click SEND manually.")
