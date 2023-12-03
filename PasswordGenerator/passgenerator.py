import random
import string

word_length = 18
components = [string.ascii_letters, string.digits, "!@#$%&"]

# Combine characters from different components into a single list
chars = [char for clist in components for char in clist]

def generate_password():
    # Generate a password by randomly selecting characters from the combined list
    password = [random.choice(chars) for _ in range(word_length)]
    return "".join(password)

# Print the generated password
print(generate_password())

  