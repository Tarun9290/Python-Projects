def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

#numbers = [1, 4, 2, 6, 9, 11, 8]
n=input()
n=list(map(int,input().split()))
print(n)
print("Largest number in the list is: ", find_largest(n))
