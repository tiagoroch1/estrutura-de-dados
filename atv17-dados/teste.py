from algoritmos.bucket_sort_notas import bucket_sort_notas
from algoritmos.interpolation_search_notas import interpolation_search_notas
import time

# Notas dos alunos
notas = [45, 82, 78, 92, 56, 35, 68, 89, 23, 41, 100, 50]

# Ordenando as notas
start_sort = time.time()
notas_ordenadas = bucket_sort_notas(notas)
sort_time = time.time() - start_sort

print(f"Notas originais: {notas}")
print(f"Notas ordenadas: {notas_ordenadas}")
print(f"Tempo de ordenação: {sort_time:.6f} segundos")

# Busca por uma nota específica
nota_procurada = 78
start_search = time.time()
posicao = interpolation_search_notas(notas_ordenadas, nota_procurada)
search_time = time.time() - start_search

if posicao != -1:
    print(f"A nota {nota_procurada} foi encontrada na posição {posicao}.")
else:
    print(f"A nota {nota_procurada} não foi encontrada.")
print(f"Tempo de busca: {search_time:.6f} segundos")
