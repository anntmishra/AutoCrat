import pyautogui
import time
import pyperclip
import platform
import sys
from pynput.mouse import Listener
from tkinter import Tk, Button, Label, PhotoImage, Frame


# Function to start the typing process
def autotyper(speed=0.05):
    # Delay before starting
    time.sleep(5)

    # Get the content from the clipboard
    clipboard_content = pyperclip.paste()

    # Type the content with speed control
    pyautogui.typewrite(clipboard_content, interval=speed)

# Function to handle start button click
def start_typing():
    print("Starting typing...")
    autotyper(speed=0.01)

# Function to create the main GUI
def create_gui():
    root = Tk()
    root.title("AutoCrat - Code Typer")  # Set window title
    root.geometry("400x300")  # Set the window size
    root.config(bg="#f0f0f0")  # Set background color

    # Header Frame for AutoCrat title
    header_frame = Frame(root, bg="#4CAF50", pady=20)
    header_frame.pack(fill="x")
    
    # Header Label
    title_label = Label(header_frame, text="AutoCrat", font=("Arial", 24, "bold"), fg="white", bg="#4CAF50")
    title_label.pack()

    # Start Button
    start_button = Button(root, text="Start Typing", command=start_typing, font=("Arial", 14), bg="#4CAF50", fg="white", width=20, height=2)
    start_button.pack(pady=30)

    # Stop Button
    stop_button = Button(root, text="Stop Typing", command=root.quit, font=("Arial", 14), bg="#F44336", fg="white", width=20, height=2)
    stop_button.pack(pady=10)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()


    