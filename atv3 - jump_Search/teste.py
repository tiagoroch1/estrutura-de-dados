import time
from jump_search import jump_search

# Função Binary Search
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def testar_jump_search():
    lista = list(range(1, 100000))  # Lista maior para melhor medição
    alvo = 99999  # Elemento que queremos buscar
    
    # Testando Jump Search
    start_time = time.perf_counter()
    resultado_jump = jump_search(lista, alvo)
    jump_time = time.perf_counter() - start_time
    print(f"Jump Search: Elemento {alvo} encontrado no índice {resultado_jump} em {jump_time:.6f} segundos")
    
    # Testando Binary Search
    start_time = time.perf_counter()
    resultado_binary = binary_search(lista, alvo)
    binary_time = time.perf_counter() - start_time
    print(f"Binary Search: Elemento {alvo} encontrado no índice {resultado_binary} em {binary_time:.6f} segundos")

if __name__ == "__main__":
    testar_jump_search()
