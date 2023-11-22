import os
import secrets
import string
import hashlib

class PasswordManager:
    def __init__(self, file_path="passwords.txt"):
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)

    def generate_password(self, length=16):
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(characters) for _ in range(length))

    def hash_password(self, password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode("utf-8"))
        return sha256.hexdigest()

    def store_password(self, service, username, password):
        hashed_password = self.hash_password(password)
        with open(self.file_path, "a") as file:
            file.write(f"{service},{username},{hashed_password}\n")

    def get_password(self, service, username, password):
        hashed_password = self.hash_password(password)
        try:
            with open(self.file_path) as file:
                for line in file:
                    stored_service, stored_username, stored_hashed_password = line.strip().split(",")
                    if service == stored_service and username == stored_username and hashed_password == stored_hashed_password:
                        return password
            return None
        except Exception as e:
            print(f"Error reading from file: {e}")
            return None

# Example usage
pm = PasswordManager()

service = "example_service"
username = "example_user"
password = pm.generate_password()

pm.store_password(service, username, password)
retrieved_password = pm.get_password(service, username, password)

print(f"Generated Password: {password}")
print(f"Retrieved Password: {retrieved_password}")


