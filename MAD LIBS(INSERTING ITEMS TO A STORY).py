#Mad Libs: 
#
#Create a program that prompts the user for various words (such as nouns, verbs, and adjectives) 
#and inserts them into a pre-written story.


noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")

story = f"Once upon a time, there was a {noun1} that loved to {verb}. It was very {adjective}. One day, the {noun1} met a {noun2} and they lived happily ever after."
print(story)
