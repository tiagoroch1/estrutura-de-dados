# merge_sort.py

def merge_sort(arr):
    comparisons = 0

    def _merge_sort(arr):
        nonlocal comparisons
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            _merge_sort(left)
            _merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                comparisons += 1
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    _merge_sort(arr)
    return comparisons
