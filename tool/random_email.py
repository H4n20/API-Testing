import random
import string

def create_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range (email_length))
    email = random_string + "@" + domain
    return email
