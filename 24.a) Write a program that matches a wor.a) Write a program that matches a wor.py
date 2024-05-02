import re

def match_word_with_z(word):
    pattern = re.compile(r'\b\w*z\w*\b')
    return bool(pattern.match(word))

# Test cases
word_to_test = "zebra"
if match_word_with_z(word_to_test):
    print(f"'{word_to_test}' contains 'z'.")
else:
    print(f"'{word_to_test}' does not contain 'z'.")
    
    
    import re

def match_a_followed_by_bs(input_string):
    pattern = re.compile(r'a+b*')
    return bool(pattern.match(input_string))

# Test cases
string_to_test = "abbbb"
if match_a_followed_by_bs(string_to_test):
    print(f"'{string_to_test}' matches the pattern.")
else:
    print(f"'{string_to_test}' does not match the pattern.")

