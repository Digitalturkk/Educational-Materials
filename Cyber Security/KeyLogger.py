from pynput import keyboard

pressed = set() #you may also use list

def on_press(key):
    pressed.add(str(key)) #if you have choosed list over set, change it to .append
    print("Сейчас нажаты:", pressed)

def on_release(key):
    pressed.discard(str(key)) #the same here .discard -> .remove

    if key == keyboard.Key.esc: #using escep as button to stop our keylogger
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
