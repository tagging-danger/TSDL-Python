import re

def match_word_with_z(word):
    # Match a word containing 'z', not at the start or end
    pattern = re.compile(r'\b[^zZ]\w*z\w*[^zZ]\b')
    return bool(pattern.match(word))

def match_valid_string(input_string):
    # Match a string that contains only upper and lowercase letters, numbers, and underscores
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return bool(pattern.match(input_string))

# Test cases
word_to_test = "python"
if match_word_with_z(word_to_test):
    print(f"'{word_to_test}' contains 'z' not at the start or end.")
else:
    print(f"'{word_to_test}' does not meet the criteria.")

string_to_test = "Valid_String_123"
if match_valid_string(string_to_test):
    print(f"'{string_to_test}' is a valid string.")
else:
    print(f"'{string_to_test}' is not a valid string.")
