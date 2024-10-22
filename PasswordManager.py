import random
import string


def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Create a pool of characters based on user preferences
    character_pool = ''

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # Ensure the character pool is not empty
    if not character_pool:
        raise ValueError("No character types selected for password generation.")

    # Generate a random password by choosing 'length' characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))

    return password


# Get user input for password preferences
length = int(input("Enter the password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
print("Generated Password:", password)
