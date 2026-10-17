#!/usr/bin/env python3

from getpass import getpass


# Create a function to check password strength.
# Check length, uppercase, lowercase, digits,
# and special characters.
def check_password(password):

    # Check length
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."
    
    return "Password is strong."    


if __name__ == "__main__":
    password = getpass("Enter a password to check: ")
    print(check_password(password))