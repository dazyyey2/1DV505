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
    if lst == []:  # Handle empty list
        return lst
    if len(lst) == 1:  # Handle list with 1 element / base case
        return lst
    mid = len(lst) // 2  # Get middle with interger division
    left = lst[:mid]  # Get left part from slicing
    right = lst[mid:]  # Get right part from slicing
    # Recursion step, keep splitting list into smaller parts
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # After list has been split fully, merge it and return merged list
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = 0  # Track left position in list
    j = 0  # Track right position in list
    # While we still have values to go through on left and right
    while i < len(left) and j < len(right):
        # Compare left and right value at index to find the smallest
        # And then increment index from the side the value came from
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # If list had more on left or right side, put remaining into result
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def quick_sort_slow(lst):
    if len(lst) <= 1:  # Base case
        return lst
    else:
        # If list is larger than base case, get pivot and all values smaller
        # in left and all values larger in right
        pivot, left, right = partition_slow(lst)
        # Recursion step, keep using last value as pivot until
        # the whole list has been sorted
        sorted_left = quick_sort_slow(left)
        sorted_right = quick_sort_slow(right)
        return sorted_left + [pivot] + sorted_right


def partition_slow(lst):
    pivot = lst[len(lst)-1]  # Use last value as pivot
    left = []
    right = []
    # Go through the list (except pivot) and add any value larger
    # to the right list and any value smaller or equal to the left list
    for i in range(0, len(lst)-1):
        if lst[i] <= pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return pivot, left, right


def quick_sort_median(lst):
    if len(lst) <= 1:  # Base case
        return lst
    else:
        # If list is larger than base case, get pivot and all values smaller
        # in left and all values larger in right
        pivot, left, right = partition_median(lst)
        # Recursion step, keep using last value as pivot until
        # the whole list has been sorted
        sorted_left = quick_sort_median(left)
        sorted_right = quick_sort_median(right)
        return sorted_left + [pivot] + sorted_right


def partition_median(lst):
    first_index = 0
    mid_index = len(lst) // 2
    last_index = len(lst) - 1
    first_val = lst[first_index]
    mid_val = lst[mid_index]
    last_val = lst[last_index]
    # Find median
    if (mid_val <= first_val <= last_val) or (last_val <=
                                              first_val <= mid_val):
        pivot_index = first_index
    elif (first_val <= mid_val <= last_val) or (last_val <=
                                                mid_val <= first_val):
        pivot_index = mid_index
    else:
        pivot_index = last_index
    pivot = lst[pivot_index]  # Use median as pivot
    left = []
    right = []
    for i in range(0, len(lst)):
        # Skip the pivot
        if i != pivot_index:
            if lst[i] <= pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
    return pivot, left, right
