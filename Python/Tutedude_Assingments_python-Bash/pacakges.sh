#!/bin/bash

PACKAGE_FILE="packages.txt"
LOG_FILE="install_log.txt"

# Detect the package manager
if command -v apt > /dev/null; then
    INSTALL_CMD="sudo apt install -y"
    UPDATE_CMD="sudo apt update"
elif command -v yum > /dev/null; then
    INSTALL_CMD="sudo yum install -y"
    UPDATE_CMD="sudo yum update"
else
    echo "No supported package manager found (apt or yum). Exiting."
    exit 1
fi

# Update package lists
echo "Updating package lists..."
$UPDATE_CMD

# Make sure the log file is fresh
> "$LOG_FILE"

# Install packages from the file
while IFS= read -r package || [ -n "$package" ]; do
    if [[ -n "$package" ]]; then
        echo "Installing $package..."
        if $INSTALL_CMD "$package"; then
            echo "$(date): SUCCESS installing $package" >> "$LOG_FILE"
            echo "$package installed successfully!"
        else
            echo "$(date): FAILED installing $package" >> "$LOG_FILE"
            echo "Failed to install $package."
        fi
    fi
done < "$PACKAGE_FILE"

echo "Installation process complete. Check $LOG_FILE for details."
