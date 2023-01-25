def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

n=list(map(int,input().split()))
print(n)
print("Smallest number in the list is: ", find_smallest(n))