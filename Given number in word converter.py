#GIVEN NUMBER IN WORDS CONVERTER IN PYTHON

def number_to_words(number):
    # convert numbers to words
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 
        9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 
        30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 
        90: "ninety", 0: ""}
    if number == 0:
        return ""
    elif number < 0:
        return "minus " + number_to_words(abs(number))
    elif number < 21:
        return words[number]
    elif number < 100:
        return words[number//10 * 10] + " " + number_to_words(number % 10)
    elif number < 1000:
        return words[number//100] + " hundred " + number_to_words(number % 100)
    else:
        return number_to_words(number // 1000) + " thousand " + number_to_words(number % 1000) 

# test
n=int(input())
print(number_to_words(n)) # one thousand