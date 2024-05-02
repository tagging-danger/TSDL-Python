def count_words(sentence):
    words = sentence.split()
    return len(words)

# Take a sentence as input from the user
user_sentence = input("Enter a sentence: ")

# Call the function to count words
word_count = count_words(user_sentence)

# Display the result
print(f"\nThe number of words in the sentence is: {word_count}")
