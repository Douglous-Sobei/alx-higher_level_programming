def find_peak_optimized(lst):
    """
    Find a peak in an unsorted list of integers
    """
    length = len(lst)

    # Edge cases
    if length == 0:
        return None
    if length == 1:
        return lst[0]
    if length == 2:
        return max(lst)

    # Check if first or last element is a peak
    if lst[0] > lst[1]:
        return lst[0]
    if lst[length - 1] > lst[length - 2]:
        return lst[length - 1]

    # Initialize variables for binary search
    left = 1
    right = length - 2

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            # Found a peak
            return lst[mid]
        elif lst[mid - 1] > lst[mid]:
            # Search left half
            right = mid - 1
        else:
            # Search right half
            left = mid + 1

    return None
