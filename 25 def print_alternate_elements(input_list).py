def print_alternate_elements(input_list):
    alternate_elements = input_list[::2]
    print("Alternate Elements:", alternate_elements)

# Take a list as input from the user
user_list = input("Enter a list of elements separated by spaces: ").split()

# Convert the input to the appropriate data type (e.g., integers or strings)
user_list = [int(element) for element in user_list]

# Call the function to print alternate elements
print_alternate_elements(user_list)
