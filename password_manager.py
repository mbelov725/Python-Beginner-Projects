from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

def write_salt():
    salt = os.urandom(16)
    with open("salt.key", "wb") as f:
        f.write(salt)

def load_salt():
    with open("salt.key", "rb") as f:
        return f.read()
    
if not os.path.exists("key.key"):
    write_salt()

def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm  = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100_100
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

master_password = input("What is the master password? ").encode()
salt = load_salt()
key = derive_key(master_password, salt)
fer = Fernet(key)

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.")
        return

    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                username, password = line.rstrip().split("|")
                decrypted = fer.decrypt(password.encode()).decode()
                print(f"Username: {username} | Password: {decrypted}")
    except InvalidToken:
        print("Wrong master password.")

def add():
    username = input("Account Name: ")
    password = input("Password: ")

    encrypted = fer.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(f"{username} | {encrypted} \n")

    print("Password added.")

while True:
    mode = input("Would you like to add a new password, view exisiting ones, or stop? (add, view, quit): ").lower()
    
    if mode == "quit":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue