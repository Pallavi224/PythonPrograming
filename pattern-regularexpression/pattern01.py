import re


pattern = r'\d+'
text = 'There are 123 apples and 456 oranges.'

matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']
# Explanation:
# \d+ matches one or more digits
# re.findall() returns all non-overlapping matches of the pattern in the string as a list.
# In this case, it finds '123' and '456' in the text.
# The pattern \d+ matches one or more digits in the string.
# The re.findall() function returns a list of all matches found in the string.
# The output is a list of strings, each representing a sequence of digits found in the text.
# The output is a list of strings, each representing a sequence of digits found in the text.
# The output is a list of strings, each representing a sequence of digits found in the text.