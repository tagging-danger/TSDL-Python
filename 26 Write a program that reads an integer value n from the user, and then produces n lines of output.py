# Read an integer value n from the user
n = int(input("Enter a size: "))

# Use a single loop to print the lines with increasing stars
for i in range(1, n + 1):
    print('+' * i)
