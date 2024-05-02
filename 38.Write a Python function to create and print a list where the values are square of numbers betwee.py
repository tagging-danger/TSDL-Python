def create_and_print_squares():
    # Using a list comprehension to create a list of squares
    squares_list = [i ** 2 for i in range(1, 31)]

    # Print the created list
    print("List of squares of numbers between 1 and 30:")
    print(squares_list)

# Call the function
create_and_print_squares()
