def swap_elements(input_list, index1, index2):
    # Check if the indices are valid
    if 0 <= index1 < len(input_list) and 0 <= index2 < len(input_list):
        # Swap the elements
        input_list[index1], input_list[index2] = input_list[index2], input_list[index1]
        return True
    else:
        print("Invalid indices. Please enter valid indices.")
        return False

# Take a list as input from the user
user_list = input("Enter a list of elements separated by spaces: ").split()

# Convert the input to the appropriate data type (e.g., integers or strings)
user_list = [int(element) for element in user_list]

# Take user input for swap indices
index1 = int(input("Enter the index of the first element to swap: "))
index2 = int(input("Enter the index of the second element to swap: "))

# Call the function to swap elements
if swap_elements(user_list, index1, index2):
    print("\nList after swapping elements:")
    print(user_list)
