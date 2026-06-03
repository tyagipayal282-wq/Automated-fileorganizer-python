from cryptography.fernet import Fernet
import json
import os
import random
import string

# =========================
# GENERATE KEY (FIRST TIME)
# =========================

def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Generate key if not exists
if not os.path.exists("key.key"):
    generate_key()

# =========================
# LOAD KEY
# =========================

with open("key.key", "rb") as key_file:
    key = key_file.read()

fer = Fernet(key)

# =========================
# LOAD PASSWORD DATA
# =========================

if os.path.exists("passwords.json"):

    with open("passwords.json", "r") as file:
        data = json.load(file)

else:
    data = {}

# =========================
# SAVE PASSWORDS
# =========================

def save_data():

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

# =========================
# ADD PASSWORD
# =========================

def add_password():

    website = input("Enter website/app name: ")
    username = input("Enter username/email: ")
    password = input("Enter password: ")

    encrypted_password = fer.encrypt(password.encode()).decode()

    data[website] = {
        "username": username,
        "password": encrypted_password
    }

    save_data()

    print("\nPassword saved successfully!")

# =========================
# VIEW PASSWORD
# =========================

def view_password():

    website = input("Enter website name: ")

    if website in data:

        encrypted_password = data[website]["password"]

        decrypted_password = fer.decrypt(
            encrypted_password.encode()
        ).decode()

        print("\n===== DETAILS =====")
        print("Username:", data[website]["username"])
        print("Password:", decrypted_password)

    else:
        print("\nNo data found!")

# =========================
# GENERATE STRONG PASSWORD
# =========================

def generate_password():

    length = 12

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for i in range(length)
    )

    print("\nGenerated Password:", password)

# =========================
# MAIN MENU
# =========================

while True:

    print("\n====== PASSWORD MANAGER ======")
    print("1. Add Password")
    print("2. View Password")
    print("3. Generate Strong Password")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_password()

    elif choice == "3":
        generate_password()

    elif choice == "4":
        print("\nExiting Password Manager...")
        break

    else:
        print("\nInvalid choice!")