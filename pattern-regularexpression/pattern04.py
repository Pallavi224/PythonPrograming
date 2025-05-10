import re

def is_valid_password(password):
    # Define the regex pattern for a valid password
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    # Match the pattern with the input password
    if re.match(pattern, password):
        return True
    return False

# Test the function
password = input("Enter a password to validate: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.")