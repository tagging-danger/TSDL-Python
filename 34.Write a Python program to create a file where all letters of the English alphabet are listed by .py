import string

def create_alphabet_file(file_path, letters_per_line):
    alphabet = string.ascii_uppercase  # Get the uppercase English alphabet
    with open(file_path, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i + letters_per_line]
            file.write(line + '\n')

# Specify the file path and the number of letters per line
file_path = 'alphabet_file.txt'
letters_per_line = 5

# Call the function to create the file
create_alphabet_file(file_path, letters_per_line)

print(f"The file '{file_path}' has been created with {letters_per_line} letters per line.")
