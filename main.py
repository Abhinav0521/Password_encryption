import os
import setup,add,view
import json

file_name = "secret.key"  # Replace with the file you are checking for

if os.path.isfile(file_name):
    file_path = "people_data.json"

    def load_data(file_path):
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:  # File exists and is not empty
            with open(file_path, "r") as file:
                try:
                    return json.load(file)  # Attempt to load JSON
                except json.JSONDecodeError as e:
                    print(f"Error loading JSON: {e}")
                    return {}
        else:
            print("File is empty or does not exist. Initializing empty data.")
            return {}


    data_dict = load_data(file_path)


    while True:
        print("---------- MODE ----------")
        print("Select a mode:\nClick 1 To add new password\nClick 2 To view old password\nClick 3 To quit")
        mode = input("Mode: ").lower()

        if mode == "3":
            break
        elif mode == "1":
            print("Add mode")
            add.add(data_dict, file_path)
        elif mode == "2":
            print("View mode")
            view.view(data_dict)
else:
    print("Let's setup the key first:")
    setup.setup()
