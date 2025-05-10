#!/bin/bash

# Input file containing usernames
USER_LIST="user_list.txt"

# Output file for credentials
CREDENTIALS_FILE="credentials.txt"

# Clear previous credentials file if it exists
> "$CREDENTIALS_FILE"

# Loop through each username in the list
while IFS= read -r username
do
    # Create the user (without prompting for password)
    sudo useradd -m "$username"

    # Generate a random password (12 characters)
    password=$(openssl rand -base64 12)

    # Set the user's password
    echo "$username:$password" | sudo chpasswd

    # Save username and password to the credentials file
    echo "$username $password" >> "$CREDENTIALS_FILE"

    echo "Created user: $username"
done < "$USER_LIST"

echo "✅ All users created and credentials saved to $CREDENTIALS_FILE."
