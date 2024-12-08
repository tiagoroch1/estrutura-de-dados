import time
from ordenacao import bubble_sort, quick_sort
from buscas import binary_search, interpolation_search

# Função para medir o tempo de execução de um algoritmo
def medir_tempo(func, arr, target=None):
    start_time = time.time()
    if target is not None:
        result = func(arr, target)
    else:
        result = func(arr)
    end_time = time.time()
    return end_time - start_time, result

# Função para comparar os tempos de execução de diferentes algoritmos de busca e ordenação
def comparar_algoritmos(arr, target):
    print("Comparando algoritmos de busca:")
    tempo, result = medir_tempo(binary_search, arr, target)
    print(f"Binary Search: {tempo:.6f}s, Resultado: {result}")

    tempo, result = medir_tempo(interpolation_search, arr, target)
    print(f"Interpolation Search: {tempo:.6f}s, Resultado: {result}")

    print("\nComparando algoritmos de ordenação:")
    tempo, result = medir_tempo(bubble_sort, arr)
    print(f"Bubble Sort: {tempo:.6f}s")

    tempo, result = medir_tempo(quick_sort, arr)
    print(f"Quick Sort: {tempo:.6f}s")
