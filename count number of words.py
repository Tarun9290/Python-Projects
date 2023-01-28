#A program that takes a sentence as input and counts the number of words in it

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = sentence.count(' ') + 1
print("The sentence has", word_count, "words.")
