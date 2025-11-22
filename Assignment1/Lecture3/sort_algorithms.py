def selection_sort(lst):
    if lst == []:  # Handle empty list
        return lst
    if len(lst) == 1:  # Handle list with 1 element
        return lst
    for i in range(len(lst) - 1):
        # Start with i as smallest value, save its index
        min_index = i
        for j in range(i+1, len(lst)):
            # If this value is smaller than current smallest, this is smallest
            if lst[j] < lst[min_index]:
                min_index = j
        # If we found smaller, flip them in the list
        if min_index != i:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst


def bubble_sort(lst):
    if lst == []:  # Handle empty list
        return lst
    if len(lst) == 1:  # Handle list with 1 element
        return lst
    changes = 1
    # If no changes are made = sorted list
    while changes > 0:
        changes = 0
        # Go through list and check if neighbour is smaller
        # If smaller --> swap place
        for i in range(len(lst) - 1):
            if lst[i+1] < lst[i]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i + 1] = temp
                changes += 1
    return lst


def insertion_sort(lst):
    if lst == []:  # Handle empty list
        return lst
    if len(lst) == 1:  # Handle list with 1 element
        return lst
    for i in range(1, len(lst)):
        # Go through from i backwards
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j - 1] = temp
            else:  # If j is larger than sorted part, skip shifting of j
                break
    return lst


def merge_sort(lst):
    return lst


def quick_sort_slow(lst):
    return


def quick_sort_optimized(lst):
    return
