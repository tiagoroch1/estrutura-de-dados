import random
import time
from bucket_sort import bucket_sort

# Função para gerar uma lista de números flutuantes aleatórios no intervalo [0, 1)
def generate_float_list(size):
    return [random.random() for _ in range(size)]

# Função para gerar uma lista de números inteiros aleatórios em um intervalo [0, 100)
def generate_int_list(size):
    return [random.randint(0, 100) for _ in range(size)]

# Teste 1: Ordenação de números flutuantes no intervalo [0, 1)
float_list = generate_float_list(1000)

print("Teste 1: Ordenação de números flutuantes no intervalo [0, 1)")
print("Lista original:", float_list[:10])  # Exibe apenas os primeiros 10 elementos para visualização
start_time = time.time()
sorted_float_list = bucket_sort(float_list)
end_time = time.time()
print("Lista ordenada:", sorted_float_list[:10])  # Exibe os primeiros 10 elementos da lista ordenada
print("Tempo de execução:", end_time - start_time, "segundos")
print()

# Teste 2: Ordenação de números inteiros no intervalo [0, 100)
int_list = generate_int_list(1000)

print("Teste 2: Ordenação de números inteiros no intervalo [0, 100)")
print("Lista original:", int_list[:10])  # Exibe apenas os primeiros 10 elementos para visualização
start_time = time.time()
sorted_int_list = bucket_sort(int_list)
end_time = time.time()
print("Lista ordenada:", sorted_int_list[:10])  # Exibe os primeiros 10 elementos da lista ordenada
print("Tempo de execução:", end_time - start_time, "segundos")
print()

# Teste 3: Ordenação de números inteiros em uma lista maior
int_list_large = generate_int_list(10000)

print("Teste 3: Ordenação de números inteiros em uma lista maior")
start_time = time.time()
sorted_int_list_large = bucket_sort(int_list_large)
end_time = time.time()
print("Tempo de execução para lista grande:", end_time - start_time, "segundos")
print()

# Teste 4: Comparação com outro algoritmo de ordenação (exemplo: Python's sorted)
print("Comparação com o algoritmo sorted do Python")
start_time = time.time()
sorted_int_list_python = sorted(int_list)
end_time = time.time()
print("Tempo de execução do sorted:", end_time - start_time, "segundos")
