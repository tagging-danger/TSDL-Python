import numpy as np

# Given NumPy array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Case 1: Sort array by the second row
sorted_array_case1 = sampleArray[:, np.argsort(sampleArray[1])]

# Case 2: Sort the array by the second column
sorted_array_case2 = sampleArray[np.argsort(sampleArray[:, 1])]

# Display the results
print("Original Array:")
print(sampleArray)

print("\nCase 1: Sort array by the second row")
print(sorted_array_case1)

print("\nCase 2: Sort the array by the second column")
print(sorted_array_case2)
