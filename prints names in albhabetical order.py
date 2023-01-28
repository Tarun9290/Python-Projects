#A program that takes a list of names as input and prints out the names in alphabetical order

names = input("Enter a list of names separated by commas: ").split(',')
sorted_names = sorted(names)
print("The names in alphabetical order:")
for name in sorted_names:
    print(name)
