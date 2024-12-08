# stability_check.py

def stable_sort_example(arr):
    # Usando um algoritmo estável como Merge Sort
    return sorted(arr, key=lambda x: x[1])  # Ordenando pelo segundo elemento

def unstable_sort_example(arr):
    # Usando um algoritmo instável como Selection Sort
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Troca direta
    return arr
