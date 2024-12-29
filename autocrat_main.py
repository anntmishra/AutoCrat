import pyautogui
import time
import tkinter as tk
from tkinter import ttk, messagebox
import threading

class AutoTyper:
    def __init__(self):
        self.typing_active = False
        self.current_thread = None

    def type_text(self, start_delay, write_delay):
        text_to_type = text_area.get("1.0", tk.END).rstrip()

        if not text_to_type:
            messagebox.showwarning("Warning", "Text area is empty!")
            return

        try:
            time.sleep(start_delay)
            status_label.config(text="Typing in progress...")

            pyautogui.write(text_to_type, interval=write_delay)
            
            status_label.config(text="Typing completed!")
            self.typing_active = False

        except pyautogui.FailSafeException:
            messagebox.showwarning("Warning", "Failsafe triggered! Move mouse to corner to stop.")
            self.typing_active = False
            status_label.config(text="Typing stopped (Failsafe)")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.typing_active = False
            status_label.config(text="Error occurred")

    def start_typing(self):
        if self.typing_active:
            messagebox.showinfo("Info", "Typing is already in progress!")
            return

        try:
            start_delay = float(delay_entry.get())
            write_delay = float(write_delay_entry.get())

            if start_delay < 0 or write_delay < 0:
                raise ValueError("Delays must be positive numbers")
            
            self.typing_active = True
            self.current_thread = threading.Thread(
                target=self.type_text, 
                args=(start_delay, write_delay)
            )
            self.current_thread.daemon = True
            self.current_thread.start()
            
            stop_button.config(state="normal")
            start_button.config(state="disabled")

        except ValueError as ve:
            messagebox.showerror("Error", "Please enter valid positive numbers for delays")

    def stop_typing(self):
        if self.typing_active:
            self.typing_active = False
            status_label.config(text="Stopping...")
            start_button.config(state="normal")
            stop_button.config(state="disabled")

def create_gui():
    root = tk.Tk()
    root.title("AutoCrat - Code Typer")

    style = ttk.Style()
    style.theme_create("autocrat_theme", parent="alt", settings={
        ".": {"configure": {"background": "#282c34", "foreground": "#abb2bf", "font": ("Consolas", 10)}},
        "TLabel": {"configure": {"foreground": "#e06c75", "font": ("Consolas", 16, "bold")}},
        "TButton": {"configure": {"padding": [10, 5], "relief": "flat", "background": "#3e4451", 
                                "foreground": "#abb2bf", "borderwidth": 0}},
        "TButton.hover": {"configure": {"background": "#5c6370"}},
        "TFrame": {"configure": {"background": "#282c34"}}
    })
    style.theme_use("autocrat_theme")

    mainframe = ttk.Frame(root, padding="20")
    mainframe.pack(fill=tk.BOTH, expand=True)

    title_label = ttk.Label(mainframe, text="AutoCrat")
    title_label.pack(pady=(0, 20))

    global text_area
    text_area = tk.Text(mainframe, wrap=tk.WORD, font=("Consolas", 10))
    text_area.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

    delay_label = ttk.Label(mainframe, text="Start Delay (seconds):")
    delay_label.pack()
    
    global delay_entry
    delay_entry = ttk.Entry(mainframe)
    delay_entry.insert(0, "0")
    delay_entry.pack(pady=(0, 10))

    write_delay_label = ttk.Label(mainframe, text="Write Delay (seconds):")
    write_delay_label.pack()
    
    global write_delay_entry
    write_delay_entry = ttk.Entry(mainframe)
    write_delay_entry.insert(0, "0.001")
    write_delay_entry.pack(pady=(0, 10))

    global status_label
    status_label = ttk.Label(mainframe, text="Ready", font=("Consolas", 10))
    status_label.pack(pady=(0, 10))

    auto_typer = AutoTyper()
    
    global start_button, stop_button
    start_button = ttk.Button(mainframe, text="Start Typing", 
                             command=auto_typer.start_typing)
    start_button.pack(pady=(0, 5), fill=tk.X)

    stop_button = ttk.Button(mainframe, text="Stop Typing", 
                            command=auto_typer.stop_typing, state="disabled")
    stop_button.pack(fill=tk.X)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.minsize(400, 400)
    
    failsafe_label = ttk.Label(mainframe, 
                              text="Move mouse to corner to trigger failsafe", 
                              font=("Consolas", 8))
    failsafe_label.pack(pady=(10, 0))

    root.mainloop()

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1
    
    create_gui()