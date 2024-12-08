# quick_sort.py

def quick_sort(arr):
    comparisons = 0

    def _quick_sort(arr, low, high):
        nonlocal comparisons
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                comparisons += 1
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pi = i + 1
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
    return comparisons
