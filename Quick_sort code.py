#QUICK SORT CODE IN PYTHON

def quick_sort(arr):
    """
    Sorts an array using Quick Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

my_array = list(map(int,input().split()))
sorted_array = quick_sort(my_array)
print(sorted_array)