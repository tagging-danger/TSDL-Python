def count_repeated_characters(input_string):
    char_count = {}
    
    # Count occurrences of each character
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Display repeated characters and their counts
    for char, count in char_count.items():
        if count > 1:
            print(f"{char}  {count}")

# Example usage:
sample_string = "thequickbrownfoxjumpsoverthelazydog"
print("Sample String:", sample_string)

print("\nRepeated Characters and their Counts:")
count_repeated_characters(sample_string)
