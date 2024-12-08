import time

# Exemplo de função para medir tempo
def medir_tempo(func, *args, **kwargs):
    start_time = time.perf_counter()  # Usando perf_counter para maior precisão
    result = func(*args, **kwargs)  # Executa a função com os parâmetros passados
    end_time = time.perf_counter()  # Captura o tempo final
    elapsed_time = end_time - start_time  # Calcula o tempo de execução
    return result, elapsed_time  # Retorna o resultado e o tempo

# Teste das funções de busca
from buscas.binary_search import binary_search
from buscas.interpolation_search import interpolation_search
from buscas.jump_search import jump_search
from buscas.exponential_search import exponential_search

# Lista de teste
arr = [1, 2, 3, 4, 5]
target = 3

# Teste do Binary Search
result, time_binary = medir_tempo(binary_search, arr, target)
print(f"Binary Search Result: {result}, Time: {time_binary:.10f} seconds")

# Teste do Interpolation Search
result, time_interpolation = medir_tempo(interpolation_search, arr, target)
print(f"Interpolation Search Result: {result}, Time: {time_interpolation:.10f} seconds")

# Teste do Jump Search
result, time_jump = medir_tempo(jump_search, arr, target)
print(f"Jump Search Result: {result}, Time: {time_jump:.10f} seconds")

# Teste do Exponential Search
result, time_exponential = medir_tempo(exponential_search, arr, target)
print(f"Exponential Search Result: {result}, Time: {time_exponential:.10f} seconds")
