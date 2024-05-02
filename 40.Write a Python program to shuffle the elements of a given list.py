import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()  # Create a copy to avoid modifying the original list
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", original_list)

shuffled_result = shuffle_list(original_list)
print("Shuffled List:", shuffled_result)
