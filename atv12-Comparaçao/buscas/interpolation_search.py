# buscas/interpolation_search.py

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1
