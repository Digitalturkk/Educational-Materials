import webbrowser
import time
import random

sites = [
    "https://three-edu.com"
]

print("Adware simulator started...")

while True:
    site = random.choice(sites)

    webbrowser.open(site)

    print(f"Opened: {site}")

    time.sleep(10)  # каждые 10 секунд
