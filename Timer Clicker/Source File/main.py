import tkinter as tk
import threading, pyautogui, time, random

running = False
mode = None

INTERVAL = 240  # 4 minutes

def worker():
    global running

    while running:
        if mode == "click":
            pyautogui.click()
            print("Clicked")

        elif mode == "right_click":
            pyautogui.rightClick()
            print("Right Clicked")
        
        elif mode == "move":
            pyautogui.moveTo(500, 300, duration=0.5)
            print("Moved to (500, 300)")

        elif mode == "random":
            width, height = pyautogui.size()
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pyautogui.moveTo(x, y, duration=0.5)
            print(f"Moved randomly to ({x}, {y})")

        time.sleep(INTERVAL)


def start(selected_mode):
    global running, mode

    if running:
        return

    mode = selected_mode
    running = True

    threading.Thread(target=worker, daemon=True).start()


def stop():
    global running
    running = False


def exit_app():
    stop()
    root.destroy()


root = tk.Tk()
root.title("Auto Mouse Tool")
root.geometry("300x400")
root.resizable(True, True)

tk.Label(root, text="Choose an action", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(root, text="Click", width=20, command=lambda: start("click")).pack(pady=5)
tk.Button(root, text="Right Click", width=20, command=lambda: start("right_click")).pack(pady=5)
tk.Button(root, text="Move Cursor (500, 300)", width=20, command=lambda: start("move")).pack(pady=5)
tk.Button(root, text="Move Cursor Randomly", width=20, command=lambda: start("random")).pack(pady=5)
tk.Button(root, text="Stop", width=20, command=stop).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=exit_app).pack(pady=5)

root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()