# Define the searched words
searched_words = ["fox", "dog", "horse"]

# Read the text from a file (assuming the file is named 'sample_text.txt')
try:
    with open('sample_text.txt', 'r') as file:
        text = file.read()

        # Search for each word in the text
        for word in searched_words:
            if word in text:
                print(f"{word} is found in the text.")
            else:
                print(f"{word} is not found in the text.")

except FileNotFoundError:
    print("Error: File 'sample_text.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
