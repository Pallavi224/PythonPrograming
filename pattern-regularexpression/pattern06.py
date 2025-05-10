import re

# Example function to find all matches of a pattern in a string
def find_matches(pattern, text):
    matches = re.findall(pattern, text)
    return matches

# Example function to check if a pattern exists in a string
def contains_pattern(pattern, text):
    return bool(re.search(pattern, text))

# Example function to replace a pattern in a string
def replace_pattern(pattern, replacement, text):
    return re.sub(pattern, replacement, text)

# Example usage
if __name__ == "__main__":
    sample_text = "The rain in Spain falls mainly in the plain."
    pattern = r"\bin\b"

    print("Matches:", find_matches(pattern, sample_text))
    print("Contains 'in':", contains_pattern(pattern, sample_text))
    print("Replaced text:", replace_pattern(pattern, "on", sample_text))