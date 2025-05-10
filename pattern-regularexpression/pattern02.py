import re

pattern =r"\d{3}-\d{3}-\d{4}"
text = "My phone number is 123-456-7890 and my friend's number is 987-654-3210."
matches = re.findall(pattern, text)
print(matches)  # Output: ['123-456-7890', '987-654-3210']
