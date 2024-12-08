import time
from ternary_search import ternary_search

def binary_search(arr, left, right, x):
    """
    Implementa o Binary Search para comparação.
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Teste com diferentes tamanhos de lista
tamanhos = [10, 100, 1000, 10000, 100000]
resultados = []

for tamanho in tamanhos:
    lista = list(range(tamanho))
    elemento = tamanho - 1  # Buscar o último elemento

    # Teste com Ternary Search
    inicio = time.perf_counter()
    index_ternary = ternary_search(lista, 0, len(lista) - 1, elemento)
    tempo_ternary = time.perf_counter() - inicio

    # Teste com Binary Search
    inicio = time.perf_counter()
    index_binary = binary_search(lista, 0, len(lista) - 1, elemento)
    tempo_binary = time.perf_counter() - inicio

    resultados.append((tamanho, tempo_ternary, tempo_binary))

# Exibindo os resultados
print("Tamanho da Lista | Tempo Ternary Search | Tempo Binary Search")
for tamanho, tempo_ternary, tempo_binary in resultados:
    print(f"{tamanho:<17} | {tempo_ternary:<19.6f} | {tempo_binary:<18.6f}")
