#Here's an example of how you could merge two lists into a new list
#using the bubble sort algorithm in Python:

def merge_sort(list1, list2):
    # Combine the two lists into a new list
    merged_list = list1 + list2
    n = len(merged_list)

    # Sort the new list using bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            if merged_list[j] > merged_list[j+1]:
                merged_list[j], merged_list[j+1] = merged_list[j+1], merged_list[j]

    return merged_list

# Example usage:
list1 = [3, 4, 1, 5]
list2 = [6, 2, 7, 8]

print(merge_sort(list1, list2))
