from cryptography.fernet import Fernet
import json


with open("secret.key", "rb") as key_file:
    key = key_file.read()
    cipher = Fernet(key)


def save_data(file_path, data_dict):
    """ Save the dictionary data to a JSON file."""
    file_path = "people_data.json"
    with open(file_path, "w") as file:
        json.dump(data_dict, file, indent=4)  # Save data in JSON format


def add(data_dict, file_path):
    name = input("Name: ").lower()
    username = input("Username: ").encode()
    username = cipher.encrypt(username[1:]).hex()

    password = input("Password: ").encode()
    password = cipher.encrypt(password[1:]).hex()

    description = input("Description: ").encode()
    description = cipher.encrypt(description[1:]).hex()

    if name in data_dict:
        print(f"Error: A person with the name '{name}' already exists.")
        return

        # Add the data to the dictionary
    data_dict[name] = {
        "username": username,
        "password": password,
        "description": description
    }

    # Save the updated data to the file
    save_data(file_path, data_dict)
    print(f"Data for '{name}' has been added and saved.\n")
