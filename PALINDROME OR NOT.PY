#PROGRAM TO FIND WHETHER A GIVEN WORD IS PALINDROME OR NOT.


def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")
