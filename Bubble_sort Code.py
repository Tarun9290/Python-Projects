#BUBBLE SORT CODE IN PYTHON

def bubble_sort(arr):
    """
    Sorts an array using Bubble Sort algorithm.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

my_array = list(map(int,input().split()))
sorted_array = bubble_sort(my_array)
print(sorted_array) 
