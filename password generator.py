import random
import string

def generate_password(length=12):
    # Defining the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password length is at least 6
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    # Randomly select characters from the set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        password = generate_password(length)
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
