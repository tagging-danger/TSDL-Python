def print_pattern_O(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (i == 0 or i == rows - 1) and (j > 0 and j < cols - 1):
                print("*", end=" ")
            elif (i > 0 and i < rows - 1) and (j == 0 or j == cols - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage for pattern 'O'
print("Pattern 'O':")
print_pattern_O(7, 5)



def print_pattern_P(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (j == 0) or ((i == 0 or i == rows - 1) and j < cols - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage for pattern 'P'
print("\nPattern 'P':")
print_pattern_P(7, 5)



