users = {} # Dictionary to store usernames and passwords

available_pets = [
    {
        "name": "Luna",
        "type": "Dog",
        "age": 2,
        "gender": "Female",
        "breed": "Golden Retriever",
        "vaccination_status": "Up to date",
        "health_status": "Healthy",
        "personality": "Friendly and energetic",
        "description": "Luna loves to play and is great with kids.",
        "adoption_status": "Available"
    },
    {
        "name": "Milo",
        "type": "Cat",
        "age": 1,
        "gender": "Male",
        "breed": "Scottish Fold",
        "vaccination_status": "Needs vaccination",
        "health_status": "Healthy",
        "personality": "Shy but affectionate",
        "description": "Milo is calm and enjoys quiet places.",
        "adoption_status": "Available"
    }
]

adopted_pets = {}  # Dictionary to track adopted pets by username

def adopt_pet(username):
    print("\n=== Adopt a Pet ===")

    # Uygun olan evcil hayvanları filtrele
    available = [pet for pet in available_pets if pet["adoption_status"] == "Available"]

    if not available:
        print("No pets available for adoption at the moment.")
        return

    for index, pet in enumerate(available):
        print(f"\nPet #{index + 1}")
        print(f"Name: {pet['name']}")
        print(f"Type: {pet['type']}")
        print(f"Age: {pet['age']}")
        print(f"Gender: {pet['gender']}")
        print(f"Breed: {pet['breed']}")
        print(f"Vaccination Status: {pet['vaccination_status']}")
        print(f"Health Status: {pet['health_status']}")
        print(f"Personality: {pet['personality']}")
        print(f"Description: {pet['description']}")
        print(f"Adoption Status: {pet['adoption_status']}")

    choice = input("\nEnter the number of the pet you'd like to adopt (or type 'exit' to cancel): ")

    if choice.lower() == 'exit':
        print("Adoption cancelled.")
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available):
        print("Invalid selection.")
        return

    selected_pet = available[int(choice) - 1]
    selected_pet["adoption_status"] = "Adopted"

    # Kullanıcının sahiplendiği hayvanları takip et
    if username not in adopted_pets:
        adopted_pets[username] = []

    adopted_pets[username].append(selected_pet)

    print(f"You have successfully adopted {selected_pet['name']}!")


def user_dashboard(username):
    while True:
        print(f"\nWelcome to the Pet Adoption System, {username}!")
        print("1. View Available Pets")
        print("2. Adopt a Pet")
        print("3. View My Adopted Pets")
        print("4. Logout")

        choice = input("Please select an option: ")

        if choice == '1':
            print("\nAvailable Pets:")
            for pet in available_pets:
                print(f"Name: {pet['name']}")
                print(f"Type: {pet['type']}")
                print(f"Age: {pet['age']} years")
                print(f"Gender: {pet['gender']}")
                print(f"Breed: {pet['breed']}")
                print(f"Vaccination Status: {pet['vaccination_status']}")
                print(f"Health Status: {pet['health_status']}")
                print(f"Personality: {pet['personality']}")
                print(f"Description: {pet['description']}")
                print(f"Adoption Status: {pet['adoption_status']}")
                print("-" * 25)
        
        elif choice == '2':
            print("Adopting a pet... (This feature is not implemented yet)")
            ### Here I can add functionality to adopt a pet

        elif choice == '3':
            print("Viewing adopted pets... (This feature is not implemented yet)")
            ### Here I can add functionality to view adopted pets

        elif choice == '4':
            print("Logging out...")
            break

        else:
            print("Invalid option. Please try again.")    

def register_user():  # Function to register a new user
    while True:  # Username input loop
        username = input("Enter a username with at least 6 characters (or type 'exit' to go back to main menu): ")

        if username.lower() == 'exit':
            print("Returning to main menu...")
            return

        if len(username) == 0:
            print("Username cannot be empty.")
            continue

        if len(username) < 6:
            print("Username must be at least 6 characters long.")
            continue

        if not username.isalnum():
            print("Username must contain only letters and numbers.")
            continue

        if username in users:
            print("Username already exists. Please choose a different one.")
            continue

        break

    while True:  # Password input loop
        password = input("Enter a password with at least 6 characters (or type 'exit' to cancel): ")

        if password.lower() == 'exit':
            print("Registration cancelled. Returning to main menu...")
            return

        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue

        confirm = input("Confirm your password: ")

        if confirm.lower() == 'exit':
            print("Registration cancelled. Returning to main menu...")
            return

        if password != confirm:
            print("Passwords do not match. Please try again.")
            continue

        # If we reach here, password is valid and confirmed
        break

    users[username] = password
    print("Registration successful!")

def login_user():
    while True:
        
        username = input("Please enter your username: ")
        
        if username in users:
            
            password = input("Please enter your password: ")
            
            if users[username] == password:
                print(f"Welcome back, {username}!")
                user_dashboard(username)
                break
            
            else:
                print("Incorrect password. Please try again.")
        
        else:
            print("Username not found. Please register first.")        
    


# Main menu loop
while True:
    print("\n=== Pet Adoption System ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Please select an option: ")

    if choice == '1':
        login_user()
    elif choice == '2':
        register_user()
    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
