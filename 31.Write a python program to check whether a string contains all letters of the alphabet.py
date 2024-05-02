import string

def contains_all_alphabets(input_string):
    # Get a string of all alphabets
    all_alphabets = set(string.ascii_lowercase)

    # Check if each alphabet is present in the input string
    return set(input_string.lower()) >= all_alphabets

# Take a string as input from the user
user_input = input("Enter a string: ")

# Check if the string contains all letters of the alphabet
if contains_all_alphabets(user_input):
    print("The string contains all letters of the alphabet.")
else:
    print("The string does not contain all letters of the alphabet.")
