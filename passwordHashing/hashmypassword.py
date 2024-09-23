import hashlib
import os
import random
import string
def generate_salt():
    # Generates a random salt using a secure random number generator.

    return os.urandom(16)

def hash_password(password, salty=None):
    # Hashes a password using SHA-256 with an optional salt. If no salt is provided,
    # a new salt is generated.

    # Args:
    #     password (str): The password to hash.
    #     salty (str, optional): Hexadecimal string representation of the salt.
    #                            If None, a new salt is generated.

    # Returns:
    #     tuple: A tuple containing the hexadecimal string of the hash and the salt.
    
    if salty is None:
        # Generate a new salt if none is provided
        salty = generate_salt()
    else:
        # Convert the hexadecimal salt string back to bytes if provided
        salty = bytes.fromhex(salty)
    
    # Combine the password (as bytes) with the salt (also bytes)
    pwd_salt = password.encode() + salty
    hash1 = hashlib.sha256(pwd_salt).hexdigest()
    
    # Return the hash and the hex representation of the salt
    return hash1, salty.hex()


def generate_password(lenght, hasCapital, hasNumbers, hasSpecialChar):
    char_pool = string.ascii_lowercase #atleast lower case required

    if hasCapital:
        char_pool += string.ascii_uppercase #if capital is toggled
    
    if hasNumbers:
        char_pool += string.digits
    
    if hasSpecialChar:
        char_pool += string.punctuation
    password = ""
    for i in range(0, lenght):
        password += char_pool[random.randrange(0, len(char_pool))]

    return password

print(generate_password(16, True, True, True))