#program for generating random password of specified length

import random
import string

def generate_password(length):
    """Generate a random password of the specified length"""
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

length = int(input("Enter the desired password length: "))
print("Generated password: ",generate_password(length))
