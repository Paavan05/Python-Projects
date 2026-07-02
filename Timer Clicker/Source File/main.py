import tkinter as tk
import threading, pyautogui, time, random, os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

running = False
mode = None

INTERVAL = 5
KEYS = ["ctrl", "shift", "up", "down", "left", "right"]

def worker():
    global running

    while running:
        if mode == "mouse":
            pyautogui.click()
            print("Mouse Clicked")

        elif mode == "keyboard":
            key = random.choice(KEYS)
            
            if key == "up" or key == "down":
                for _ in range(40):
                    pyautogui.press(key)
                    # time.sleep(0.1)
                
            elif key == "left" or key == "right":
                for _ in range(12):
                    pyautogui.press(key)
                    # time.sleep(0.1)
            else:
                pyautogui.press(key)
    
            print(f"Pressed: {key}")

        elif mode == "both":
            pyautogui.click()
            key = random.choice(KEYS)
            pyautogui.press(key)
            print(f"Mouse Clicked + Pressed: {key}")

        # Sleep in small intervals so Stop works immediately
        for _ in range(INTERVAL):
            if not running:
                break
            time.sleep(1)


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
root.iconbitmap(resource_path("icon.ico"))
root.title("Auto Mouse & Keyboard Clicker")
root.geometry("300x350")
root.resizable(True, True)

tk.Label(root, text="Choose an Action", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(root, text="🖱 Mouse", width=20, command=lambda: start("mouse")).pack(pady=5)
tk.Button(root, text="⌨ Keyboard", width=20, command=lambda: start("keyboard")).pack(pady=5)
tk.Button(root, text="🖱 + ⌨ Both", width=20, command=lambda: start("both")).pack(pady=5)
tk.Button(root, text="Stop", width=20, command=stop).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=exit_app).pack(pady=5)

root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()