from cryptography.fernet import Fernet


def setup():
    # Generate a key
    key = Fernet.generate_key()

    # Save the key securely
    with open(f"secret.key", "wb") as key_file:
        key_file.write(key)
