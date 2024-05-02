def print_pattern_R(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if j == 0 or (i == 0 or i == rows - 1) and j < cols - 1 or j == cols - 1 and i <= rows // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_pattern_O(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if (j == 0 or j == cols - 1) and (i != 0 and i != rows - 1) or (i == 0 or i == rows - 1) and (j > 0 and j < cols - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage:
rows_R = 7
cols_R = 5
rows_O = 7
cols_O = 5

print("Pattern 'R':")
print_pattern_R(rows_R, cols_R)

print("\nPattern 'O':")
print_pattern_O(rows_O, cols_O)
