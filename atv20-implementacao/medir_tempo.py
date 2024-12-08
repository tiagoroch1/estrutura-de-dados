import random
import time

# Algoritmo de busca - Interpolation Search
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and x >= arr[low] and x <= arr[high]:
        # Interpolação para estimar a posição
        pos = low + int(((x - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        # Caso o elemento seja encontrado
        if arr[pos] == x:
            return pos
        # Se o elemento for maior, ignore a metade inferior
        elif arr[pos] < x:
            low = pos + 1
        # Se o elemento for menor, ignore a metade superior
        else:
            high = pos - 1
    
    return -1  # Elemento não encontrado

# Função para medir o tempo de execução
def medir_tempo(func, arr, x, num_runs=100):
    total_time = 0.0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        result = func(arr, x)  # Chama a função de busca
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    
    avg_time = total_time / num_runs  # Tempo médio de execução
    return avg_time

# Gerando uma lista de números aleatórios e ordenando
arr = sorted([random.randint(1, 1000) for _ in range(10000)])  # Lista ordenada de 10.000 números aleatórios

# Elemento a ser buscado
x = random.randint(1, 1000)

# Medindo o tempo de execução do Interpolation Search
tempo_interp = medir_tempo(interpolation_search, arr, x)
print(f"Tempo médio de execução do Interpolation Search: {tempo_interp:.6f} segundos")
