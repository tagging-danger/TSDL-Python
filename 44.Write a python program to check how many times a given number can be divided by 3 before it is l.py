def count_divisions_by_three(number):
    count = 0

    while number > 10:
        number /= 3
        count += 1

    return count

# Example usage:
user_input = float(input("Enter a number: "))

division_count = count_divisions_by_three(user_input)

print(f"The number can be divided by 3 {division_count} times before it becomes less than or equal to 10.")
