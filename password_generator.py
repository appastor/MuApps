import string
import random

alpha = string.ascii_letters
numeric = string.digits
spec_chars = "!@#$%^&*()"

all_chars = list(alpha + numeric + spec_chars)

# print("chars: " + all_chars)

def generate_password():
    password_length = int(input("Length of password: "))

    random.shuffle(all_chars)

    password = []

    for x in range(password_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    password = "".join(password)

    print("Password: " + password)

option = input("Generate password? (Y/N): ")

if option == "Y":
    generate_password()
elif option == "N":
    print("End")
    quit()