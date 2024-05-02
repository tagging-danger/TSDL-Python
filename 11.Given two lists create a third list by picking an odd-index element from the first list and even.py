def create_third_list(list1, list2):
    # Select odd-index elements from the first list
    odd_indices_list1 = list1[1::2]

    # Select even-index elements from the second list
    even_indices_list2 = list2[0::2]

    # Combine the two selected lists to create the third list
    third_list = odd_indices_list1 + even_indices_list2

    return third_list

# Function to take input for a list
def get_list_input():
    input_str = input("Enter elements of the list separated by spaces: ")
    return [int(x) for x in input_str.split()]

# Example usage:
list1 = get_list_input()
list2 = get_list_input()

result_list = create_third_list(list1, list2)

print("\nList 1:", list1)
print("List 2:", list2)
print("Third List:", result_list)
