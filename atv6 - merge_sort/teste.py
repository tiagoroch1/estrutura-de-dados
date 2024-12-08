import random
import time
from merge_sort import merge_sort, merge_sort_strings

# Função para medir o tempo de execução
def medir_tempo(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

# Teste com números inteiros
arr_numeros = [random.randint(1, 1000) for _ in range(1000)]  # Lista de 1000 números aleatórios
arr_numeros_copy = arr_numeros.copy()  # Fazemos uma cópia para garantir que a lista original não seja alterada

# Teste com strings
arr_strings = ["banana", "apple", "cherry", "date", "elderberry", "fig", "grape"]
arr_strings_copy = arr_strings.copy()

# Teste de tempo para números inteiros
tempo_numeros = medir_tempo(merge_sort, arr_numeros_copy)

# Teste de tempo para strings
tempo_strings = medir_tempo(merge_sort_strings, arr_strings_copy)

# Exibindo os resultados
print(f"Tempo Merge Sort para números inteiros: {tempo_numeros:.6f} segundos")
print(f"Tempo Merge Sort para strings: {tempo_strings:.6f} segundos")

# Exibindo os resultados de ordenação
print(f"Lista ordenada de números inteiros: {arr_numeros_copy}")
print(f"Lista ordenada de strings: {arr_strings_copy}")
