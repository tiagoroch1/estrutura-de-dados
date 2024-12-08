# Exponential Search Implementation

# Função de busca binária
def binary_search(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Função de busca exponencial
def exponential_search(arr, x):
    # Se o primeiro elemento for o que procuramos
    if arr[0] == x:
        return 0

    # Encontre o maior índice que é menor que o elemento
    n = len(arr)
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Faça a busca binária no intervalo encontrado
    return binary_search(arr, i // 2, min(i, n - 1), x)
