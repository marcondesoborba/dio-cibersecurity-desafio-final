# decryptor.py

import os
import sys
from cryptography.fernet import Fernet
from utils import list_files

def decrypt_files(folder_path, key):
    fernet = Fernet(key.encode())

    for filename in list_files(folder_path):
        #file_path = os.path.join(folder_path, filename)
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                encrypted = file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(filename, 'wb') as file:
                file.write(decrypted)

    print("Arquivos descriptografados com sucesso.")

def main():
    key = sys.argv[1]
    decrypt_files("testeFiles", key)

if __name__ == "__main__":
    main()