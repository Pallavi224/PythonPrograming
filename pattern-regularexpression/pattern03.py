import re 

text ="contact at me email@gmail.com"
pattern= r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

email = re.findall(pattern, text)
print(email)
# Output: ['email@gmail.com']

# Explanation:
# [a-zA-Z0-9._%+-]+ matches one or more alphanumeric characters, dots, underscores, percent signs, plus signs, or hyphens before the @ symbol.
# [a-zA-Z0-9.-]+ matches one or more alphanumeric characters, dots, or hyphens after the @ symbol and before the dot.
# \.[a-zA-Z]{2,} matches a dot followed by two or more alphabetic characters (the domain extension).
# re.findall() returns all non-overlapping matches of the pattern in the string as a list.
# In this case, it finds 'email@gmail.com' in the text.     
# The pattern [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} is a regular expression that matches email addresses.
# The re.findall() function returns a list of all matches found in the string.
# The output is a list of strings, each representing a valid email address found in the text.