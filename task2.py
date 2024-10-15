import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    # Create a pool of characters based on user preferences
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    # Ensure that at least one character type is selected
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    # Get user input for password criteria
    length = int(input("Enter the desired length of the password (minimum 6 characters): "))
    
    if length < 6:
        print("Password length should be at least 6 characters.")
        return
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()