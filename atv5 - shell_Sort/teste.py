import random
import time
from shell_sort import shell_sort, knuth_shell_sort, hibbard_shell_sort

# Função para medir o tempo de execução de cada algoritmo
def medir_tempo(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

# Gerando uma lista de 1000 elementos aleatórios para o teste
arr_shell = [random.randint(1, 1000) for _ in range(1000)]
arr_knuth = arr_shell.copy()
arr_hibbard = arr_shell.copy()

# Testando o tempo de execução para cada sequência de Shell Sort
tempo_shell = medir_tempo(shell_sort, arr_shell.copy())
tempo_knuth = medir_tempo(knuth_shell_sort, arr_knuth.copy())
tempo_hibbard = medir_tempo(hibbard_shell_sort, arr_hibbard.copy())

# Exibindo os tempos de execução
print(f"Tempo Shell Sort (sequência Shell): {tempo_shell:.6f} segundos")
print(f"Tempo Knuth Shell Sort (sequência Knuth): {tempo_knuth:.6f} segundos")
print(f"Tempo Hibbard Shell Sort (sequência Hibbard): {tempo_hibbard:.6f} segundos")
