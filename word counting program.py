print("Welcome to the Word Counting Machine Mania!!!")

sentence = input("Please enter a sentence: ")   # Takes yo input.

words = sentence.split()    # This splits the words into a list of words.

words_count = len(words) # This counts the number of words in the list.

print(f"Your sentence has {words_count} words.") # Prints the number of words.
