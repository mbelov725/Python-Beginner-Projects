'''
This program locks all saved paswords behind one master password
Only somebody who knows the master password can unlock them

The program does this in three stages.

(1) Key derivation

In this process, the program creates a cryptographic key.
The master password is passed through a key-derivation function
This results in a fixed-sized, random encryption key

(2) Adding a salt

A salt is random data that gets added to the password before the key is created.
This prevents attackers from pre-computing passwords.
It also ensures that the same password on two systems produces different keys.
The salt is generated once, stored openly, and is not hidden.

(3) Encryption

Once the key exists, passwords are encrypted before being stored.
Encrypted data looks like nonsense text, and without a key, it cannot be reversed.
When viewing passwords, the program makes a copy of the key from the master password
If the key is the same, the passowrds can be assecced.
If it isn't, the decryption fails immediately.

Most importantly, the program doesn't store the master password or encryption key.
It only stores the encrypted data and salt.

Note: this project is for educational purposes only.
This is not a fully secure password manager.
Do not use it to store any sensitive or personal information.

Required dependency: install the cryptography package before running this program.

Windows / macOS / Linux: python -m pip install cryptography

If that fails on Windows, try: py -m pip install cryptography
'''

# Fernet handles encryption and decryption
# InvalidToken is raised when the password is wrong and decryption fails
from cryptography.fernet import Fernet, InvalidToken

# PBKDF2HMAC is used to derive a secure key from a password
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# SHA256 is the hash function used by PBKDF2
from cryptography.hazmat.primitives import hashes

# base64 is required since Fernet keys must be base64-encoded
import base64

# os is used for file checks and generating random bytes
import os

# sys is used to control the program execution
import sys

# (1) Salt handling
def write_salt():
    # Generate 16 random bytes
    salt = os.urandom(16)

    # Save the salt to disk
    with open("salt.key", "wb") as f:
        f.write(salt)

def load_salt():
    # Load the existing salt from disk
    with open("salt.key", "rb") as f:
        return f.read()
    
# If this is the first run, create a salt
if not os.path.exists("salt.key"):
    write_salt()

# (2) Key derivation
def derive_key(password: bytes, salt: bytes) -> bytes:
    # PBKDF2 repeatedly hashes the password
    kdf = PBKDF2HMAC(
        algorithm  = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100_100
    )

    # Fernet required the key to be URL-safe base64 encoded
    return base64.urlsafe_b64encode(kdf.derive(password))

# (3) Setup
master_password = input("What is the master password? ").encode()
salt = load_salt()
key = derive_key(master_password, salt)
fer = Fernet(key)

# (4) Master password verification
def verify_master_password():
    # If no paswords exist yet, allow first-time setup
    if not os.path.exists("passwords.txt"):
        return True
    
    try:
        # Try decrypting the first stored password
        with open("passwords.txt", "r") as f:
            first_line = f.readline().rstrip()
            
            # If file exists but is empty, allow access
            if not first_line:
                return True
            
            _, encrypted = first_line.split("|")
            fer.decrypt(encrypted.encode())
            return True
    except InvalidToken:
        return False

if not verify_master_password():
    print("Wrong master password. Exiting.")
    sys.exit(1)

# (5) Features
def view():
    # If no passwords exist, file cannot be viewed
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.")
        return

    with open("passwords.txt", "r") as f:
        for line in f:
            username, password = line.rstrip().split("|")
            decrypted = fer.decrypt(password.encode()).decode()
            print(f"Username: {username} | Password: {decrypted}")

def add():
    username = input("Account Name: ")
    password = input("Password: ")

    encrypted = fer.encrypt(password.encode()).decode()
    
    # Append encrypted password to file
    with open("passwords.txt", "a") as f:
        f.write(f"{username} | {encrypted} \n")

    print("Password added.")

# (6) Command-line interface for program
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