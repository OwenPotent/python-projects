import random


def main():
    # Get user input
    password_length = get_password_length()
    password_type = get_password_type()
    password_count = get_password_count()

    # Generate passwords
    passwords = generate_passwords(password_length, password_type, password_count)

    # Print passwords
    print_passwords(passwords)


def get_password_length():
    # Get password length
    password_length = int(input("How long would you like your password to be? "))
    return password_length


def get_password_type():
    # Get password type
    print("Here are the types of characters you can choose from:")
    print("lowercase")
    print("uppercase")
    print("numbers")
    print("special characters")
    password_type = input("What type of characters would you like to use? ")
    return password_type


def get_password_count():
    # Get password count
    password_count = int(input("How many passwords would you like to generate? "))
    return password_count


def generate_passwords(password_length, password_type, password_count):
    # Generate passwords
    passwords = []
    for i in range(password_count):
        passwords.append(generate_password(password_length, password_type))
    return passwords


def generate_password(password_length, password_type):
    # Generate password
    password = ""
    for i in range(password_length):
        password += random.choice(password_type)
    return password


def print_passwords(passwords):
    # Print passwords
    for password in passwords:
        print(password)


if __name__ == "__main__":
    main()