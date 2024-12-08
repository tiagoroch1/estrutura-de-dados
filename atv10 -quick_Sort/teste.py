import time
from quick_sort import quick_sort

def measure_time(arr, pivot_choice):
    start_time = time.perf_counter()  # Usando perf_counter para maior precisão
    sorted_arr = quick_sort(arr, pivot_choice)
    end_time = time.perf_counter()  # Usando perf_counter para maior precisão
    return sorted_arr, end_time - start_time

def generate_tests():
    # Teste 1: Lista desordenada
    arr_unsorted = [12, 3, 5, 7, 19, 1, 10, 9, 2]
    
    # Teste 2: Lista quase ordenada (pequenos ajustes)
    arr_almost_sorted = [1, 2, 3, 5, 7, 10, 9, 12, 19]
    
    return arr_unsorted, arr_almost_sorted

if __name__ == "__main__":
    arr_unsorted, arr_almost_sorted = generate_tests()

    print("Teste com lista desordenada:")
    
    for pivot in ['first', 'last', 'middle']:
        sorted_arr, elapsed_time = measure_time(arr_unsorted, pivot)
        print(f"\nCritério de pivô '{pivot}':")
        print(f"Lista ordenada: {sorted_arr}")
        print(f"Tempo de execução: {elapsed_time:.6f} segundos")
    
    print("\nTeste com lista quase ordenada:")
    
    for pivot in ['first', 'last', 'middle']:
        sorted_arr, elapsed_time = measure_time(arr_almost_sorted, pivot)
        print(f"\nCritério de pivô '{pivot}':")
        print(f"Lista ordenada: {sorted_arr}")
        print(f"Tempo de execução: {elapsed_time:.6f} segundos")
