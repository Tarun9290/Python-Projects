#HEAP SORT CODE IMPLEMENTATION IN PYTHON


def heap_sort(arr):
    n = len(arr)

    # build a max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements from heap one by one
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)
