rows = 5

# Upper part of the pattern
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end="   ")
    print()

# Lower part of the pattern
for i in range(rows - 2, -1, -1):
    for j in range(0, i + 1):
        print("*", end="   ")
    print()
