#BINARY SEARCH IMPLEMENTATION IN PYTHON:

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
arr = [1, 3, 5, 7, 9]
target = 5

index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found in array")
