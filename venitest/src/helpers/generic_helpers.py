import random
import string


def generate_random_email(domain='abv.bg'):
    """Generate a random email address with the given domain (default is abv.bg)."""
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    email = username + '@' + domain
    return email
def generate_random_password(length=8):
    """Generate a random password with the given length (default is 8)"""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create a list of possible characters
    possible_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Make sure we have at least one of each type of character
    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))
    password.append(random.choice(digits))
    password.append(random.choice(special_chars))

    # Add additional random characters up to the desired length
    for _ in range(length - 4):
        password.append(random.choice(possible_chars))

    # Shuffle the characters to randomize the order
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)