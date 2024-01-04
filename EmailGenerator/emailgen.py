import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 12)))
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com', 'domain.com']
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email

if __name__ == "__main__":
    random_email = generate_random_email()
    print(f"Random Email Address: {random_email}")

