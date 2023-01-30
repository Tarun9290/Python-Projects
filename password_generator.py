#Password Generator:
#Create a program that generates strong, random passwords for the user.

import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
