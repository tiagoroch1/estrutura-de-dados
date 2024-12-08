import time
from bisect import bisect_left

# Função de busca binária utilizando bisect_left
def binary_search(arr, x):
    idx = bisect_left(arr, x)
    if idx != len(arr) and arr[idx] == x:
        return idx
    return -1

# Função de busca binária
def binary_search_impl(arr, low, high, x):
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
    # Caso base, se o primeiro elemento for o que estamos procurando
    if arr[0] == x:
        return 0

    # Encontre o maior índice que é menor que o elemento
    n = len(arr)
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Faça a busca binária no intervalo identificado
    return binary_search_impl(arr, i // 2, min(i, n - 1), x)

# Função de geração de listas para testes
def generate_list(size):
    return list(range(size))

# Função de teste de desempenho
def performance_test():
    # Listas pequenas e grandes
    small_list = generate_list(1000)
    large_list = generate_list(1000000)

    # Elemento a ser buscado
    x = 999

    # Teste com lista pequena
    start_time = time.time()
    for _ in range(1000):  # Executar múltiplas vezes para ter um tempo medido mais preciso
        result_small = exponential_search(small_list, x)
    time_small = (time.time() - start_time) / 1000  # Média do tempo
    print(f"Exponential Search (pequena lista): {x} encontrado no índice {result_small} em {time_small:.6f} segundos")

    # Teste com lista grande
    start_time = time.time()
    for _ in range(100):  # Executar múltiplas vezes para ter um tempo medido mais preciso
        result_large = exponential_search(large_list, x)
    time_large = (time.time() - start_time) / 100  # Média do tempo
    print(f"Exponential Search (grande lista): {x} encontrado no índice {result_large} em {time_large:.6f} segundos")

# Função para comparar os dois algoritmos
def compare_search_algorithms():
    small_list = generate_list(1000)
    large_list = generate_list(1000000)
    x = 999
    
    # Teste Exponential Search (pequena lista)
    start_time = time.time()
    for _ in range(1000):
        result_exp_small = exponential_search(small_list, x)
    time_exp_small = (time.time() - start_time) / 1000

    # Teste Binary Search (pequena lista)
    start_time = time.time()
    for _ in range(1000):
        result_bin_small = binary_search(small_list, x)
    time_bin_small = (time.time() - start_time) / 1000

    # Teste Exponential Search (grande lista)
    start_time = time.time()
    for _ in range(100):
        result_exp_large = exponential_search(large_list, x)
    time_exp_large = (time.time() - start_time) / 100

    # Teste Binary Search (grande lista)
    start_time = time.time()
    for _ in range(100):
        result_bin_large = binary_search(large_list, x)
    time_bin_large = (time.time() - start_time) / 100

    print(f"Exponential Search (pequena lista): {time_exp_small:.6f} segundos")
    print(f"Binary Search (pequena lista): {time_bin_small:.6f} segundos")
    print(f"Exponential Search (grande lista): {time_exp_large:.6f} segundos")
    print(f"Binary Search (grande lista): {time_bin_large:.6f} segundos")

# Executar os testes de desempenho
if __name__ == "__main__":
    performance_test()
    compare_search_algorithms()
