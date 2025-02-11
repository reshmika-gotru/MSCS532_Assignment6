import random

def divide(arr, pivot):
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return left, right

def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Step 1: Randomly choose a pivot
    pivot = random.choice(arr)
    
    # Step 2: Partition the array around the pivot
    left, right = divide(arr, pivot)
    
    # Step 3: Determine the rank of the pivot
    if k < len(left):
        return randomized_quickselect(left, k)
    elif k < len(left) + 1:
        return pivot
    else:
        return randomized_quickselect(right, k - len(left) - 1)

# Example usage:
arr = [100, 65, 82, 18, 59, 70, 10, 875, 1000]
k = 3  # Find the 3rd smallest element (index 2 in sorted array)
print(f"The 3rd smallest element is: {randomized_quickselect(arr, k)}")
