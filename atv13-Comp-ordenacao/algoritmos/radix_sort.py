# radix_sort.py

def radix_sort(arr):
    comparisons = 0
    max_value = max(arr)
    exp = 1
    n = len(arr)

    while max_value // exp > 0:
        output = [0] * n
        count = [0] * 10

        for num in arr:
            index = num // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            num = arr[i]
            index = num // exp
            output[count[index % 10] - 1] = num
            count[index % 10] -= 1

        for i in range(n):
            arr[i] = output[i]

        exp *= 10
        comparisons += n
    return comparisons
