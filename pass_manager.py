import random
import string

passwords = {}

# Generate Password
def generate_password():

    length = int(input("Enter password length: "))

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


while True:

    print("\n====== PASSWORD MANAGER ======")

    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Search Password")
    print("5. Delete Password")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Save Password
    if choice == "1":

        website = input("Enter website/app name: ")
        username = input("Enter username/email: ")
        password = input("Enter password: ")

        passwords[website] = {
            "username": username,
            "password": password
        }

        print(f"{website} password saved successfully!")



    # View Passwords
    elif choice == "2":

        if not passwords:
            print("No passwords saved!")

        else:

            print("\n--- SAVED PASSWORDS ---")

            for website, details in passwords.items():

                print(f"\nWebsite : {website}")
                print(f"Username: {details['username']}")
                print(f"Password: {details['password']}")



    # Generate Password
    elif choice == "3":

        new_password = generate_password()

        print("\nGenerated Password:")
        print(new_password)



    # Search Password
    elif choice == "4":

        website = input("Enter website/app name to search: ")

        if website in passwords:

            print("\nPassword Found!")

            print("Username:",
                  passwords[website]["username"])

            print("Password:",
                  passwords[website]["password"])

        else:
            print("No password found!")



    # Delete Password
    elif choice == "5":

        website = input("Enter website/app name to delete: ")

        if website in passwords:

            del passwords[website]

            print("Password deleted successfully!")

        else:
            print("Website not found!")



    # Exit
    elif choice == "6":

        print("Exiting Password Manager...")

        break



    # Invalid Input
    else:

        print("Invalid choice! Please try again.")