import threading
import time
from plyer import notification
import pygame
import tkinter as tk

# Initialize pygame mixer for sound
pygame.mixer.init()

# Flag to control the notification loop
running = True

# Function to display notification and play sound
def notify_user():
    while running:  # Keep running until the stop button is pressed
        # Display notification
        notification.notify(
            title="Reminder",
            message="This is your notification alert!",
            timeout=5  # Notification stays for 5 seconds
        )

        # Play sound using pygame
        pygame.mixer.music.load('Python Basics/OH_MY_GOD.mp3')  # Load the sound file
        pygame.mixer.music.play()  # Play the sound

        # Wait for 10 seconds before next notification
        time.sleep(3)

# Function to stop the notification
def stop_notifications():
    global running
    running = False
    root.quit()  # Close the GUI window

# Creating the GUI window
root = tk.Tk()
root.title("Notification App")

# Create a label in the window
label = tk.Label(root, text="Notification App Running...")
label.pack(pady=20)

# Create a stop button to stop the notifications
stop_button = tk.Button(root, text="Stop", command=stop_notifications, width=20)
stop_button.pack(pady=10)

# Run the notification in a separate thread so that the GUI remains responsive
notification_thread = threading.Thread(target=notify_user)
notification_thread.start()

# Start the GUI event loop
root.mainloop()

# Stop pygame mixer when the program exits
pygame.mixer.quit()








#  Made this small app out of fun with chatgpt :)