import tkinter as tk
import random

messages = [
    "YOU WON 1000$!!!",
    "Ваш ПК заражён!",
    "Скачайте антивирус!",
    "FREE ROBUX!!!"
]

def create_popup():
    popup = tk.Toplevel(root)

    width = 250
    height = 100

    x = random.randint(0, 800)
    y = random.randint(0, 500)

    popup.geometry(f"{width}x{height}+{x}+{y}")
    popup.title("Advertisement")

    label = tk.Label(
        popup,
        text=random.choice(messages),
        font=("Arial", 14)
    )

    label.pack(expand=True)

    button = tk.Button(
        popup,
        text="Close",
        command=popup.destroy
    )

    button.pack()

    root.after(1000, create_popup)

root = tk.Tk()
root.withdraw()

create_popup()

root.mainloop()
