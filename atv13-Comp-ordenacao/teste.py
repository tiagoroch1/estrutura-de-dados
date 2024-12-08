# teste.py

import time
from algoritmos.quick_sort import quick_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.shell_sort import shell_sort
from algoritmos.selection_sort import selection_sort
from algoritmos.bucket_sort import bucket_sort
from algoritmos.radix_sort import radix_sort

# Função para medir o tempo
def medir_tempo(func, arr):
    start_time = time.perf_counter()
    comparisons = func(arr)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time, comparisons

# Testar os algoritmos com uma lista
arr = [64, 25, 12, 22, 11]

# Quick Sort
time_taken, comparisons = medir_tempo(quick_sort, arr.copy())
print(f"Quick Sort - Time: {time_taken:.10f}s, Comparisons: {comparisons}")

# Merge Sort
time_taken, comparisons = medir_tempo(merge_sort, arr.copy())
print(f"Merge Sort - Time: {time_taken:.10f}s, Comparisons: {comparisons}")

# Shell Sort
time_taken, comparisons = medir_tempo(shell_sort, arr.copy())
print(f"Shell Sort - Time: {time_taken:.10f}s, Comparisons: {comparisons}")

# Selection Sort
time_taken, comparisons = medir_tempo(selection_sort, arr.copy())
print(f"Selection Sort - Time: {time_taken:.10f}s, Comparisons: {comparisons}")

# Bucket Sort
time_taken, comparisons = medir_tempo(bucket_sort, arr.copy())
print(f"Bucket Sort - Time: {time_taken:.10f}s, Comparisons: {comparisons}")

# Radix Sort
time_taken, comparisons = medir_tempo(radix_sort, arr.copy())
print(f"Radix Sort - Time: {time_taken:.10f}s, Comparisons: {comparisons}")
