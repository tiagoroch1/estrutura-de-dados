import random
import time
from radix_sort import radix_sort

# Teste 1: Números com 2 dígitos
arr_2_digits = [29, 17, 35, 72, 51, 64]
print("Teste 1: Ordenação de números com 2 dígitos")
start_time = time.time()
sorted_arr_2_digits = radix_sort(arr_2_digits)
end_time = time.time()
print("Lista ordenada (2 dígitos):", sorted_arr_2_digits)
print("Tempo de execução:", end_time - start_time, "segundos")
print()

# Teste 2: Números com 5 dígitos
arr_5_digits = [12234, 56789, 98765, 34567, 12345]
print("Teste 2: Ordenação de números com 5 dígitos")
start_time = time.time()
sorted_arr_5_digits = radix_sort(arr_5_digits)
end_time = time.time()
print("Lista ordenada (5 dígitos):", sorted_arr_5_digits)
print("Tempo de execução:", end_time - start_time, "segundos")
print()

# Teste 3: Números com 10 dígitos
arr_10_digits = [1234567890, 9876543210, 1357924680, 2468013579]
print("Teste 3: Ordenação de números com 10 dígitos")
start_time = time.time()
sorted_arr_10_digits = radix_sort(arr_10_digits)
end_time = time.time()
print("Lista ordenada (10 dígitos):", sorted_arr_10_digits)
print("Tempo de execução:", end_time - start_time, "segundos")
print()
