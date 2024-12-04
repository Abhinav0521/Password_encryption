# Password Encryption

## Description

Password Encryption is a Python-based command line application that securely stores your passwords using encryption. 
The app leverages the cryptography module to ensure your sensitive data is protected. It allows users to:

Add new passwords with associated details.
View existing passwords securely.
Update existing password entries.
All data is stored in an encrypted format in a JSON file, ensuring that only the app can decrypt and read the information. 
The app name remains unencrypted for ease of reference.

## Features

Encryption: Protects sensitive data like usernames, passwords, and descriptions using a security key.
Security Key Management: Prompts users to create a key.key file if it does not already exist.
Flexible Options: Users can choose to:
View existing passwords.
Update passwords.
Add new password entries.
User-Friendly Storage: Stores data in a JSON file, encrypting all information except for the app name.
How It Works

## First-Time Setup:
The app checks for the presence of key.key in the directory.
If not found, the user is prompted to create a security key, which is then saved to key.key.
Adding a Password:
The user provides:
App Name
Username
Password
Description (optional)
All details except the app name are encrypted and stored in a JSON file.
Viewing Passwords:
The app decrypts and displays stored password information.
Updating Passwords:
Existing entries can be updated securely.

## Requirements
- Python 3.x
- Install dependencies from `requirements.txt`:

# Paste this command in the terminal 
pip install -r requirements.txt


# Run main.py file 
