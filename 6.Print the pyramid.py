def print_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="   ")
        print()

# Example usage for the pyramid pattern
print("Pyramid Pattern:")
print_pyramid(3)

 
def print_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end="   ")
        print()

# Example usage for the pattern
print("Pattern:")
print_pattern(3, 3)
