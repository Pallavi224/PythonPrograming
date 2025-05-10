#!/bin/bash

# Check if a file was provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

FILE="$1"

# Check if file exists
if [ ! -f "$FILE" ]; then
    echo "File not found!"
    exit 1
fi

# Count lines, words, and characters
line_count=$(wc -l < "$FILE")
word_count=$(wc -w < "$FILE")
char_count=$(wc -m < "$FILE")

# Find the longest word
longest_word=$(tr -s '[:space:][:punct:]' '\n' < "$FILE" | awk '{ if (length > max) { max=length; word=$0 } } END { print word }')

# Display the results
echo "File: $FILE"
echo "------------------------"
echo "Lines      : $line_count"
echo "Words      : $word_count"
echo "Characters : $char_count"
echo "Longest word: $longest_word"
