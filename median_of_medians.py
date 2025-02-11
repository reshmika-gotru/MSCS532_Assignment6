def median_of_medians(arr):
    # Base case: if the list has 5 or fewer elements, return the median
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    # Step 1: Divide arr into sublists of at most 5 elements each
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    
    # Step 2: Find the median of each sublist and create a new list of medians
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    # Step 3: Recursively call the median_of_medians function to find the median of medians
    return median_of_medians(medians)

def divide(arr, pivot):
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return left, right

def deterministic_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Step 1: Find the median of medians as a pivot
    pivot = median_of_medians(arr)

    # Step 2: Partition the array around the pivot
    left, right = divide(arr, pivot)
    
    # Step 3: Determine the rank of the pivot
    if k < len(left):
        return deterministic_select(left, k)
    elif k < len(left) + 1:
        return pivot
    else:
        return deterministic_select(right, k - len(left) - 1)

# Example usage:
arr = [100888, -65000, 8002, 185, 0.00059, 799990, 10, 875, 1000]
k = 4  # Find the 4th smallest element (index 3 in sorted array)
print(f"The 4th smallest element is: {deterministic_select(arr, k)}")
