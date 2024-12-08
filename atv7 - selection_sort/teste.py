import time
from selection_sort import selection_sort

def test_selection_sort():
    small_list = [64, 25, 12, 22, 11]
    medium_list = [64, 25, 12, 22, 11, 45, 33, 20, 18, 37]
    large_list = [64, 25, 12, 22, 11, 45, 33, 20, 18, 37, 88, 13, 42, 7, 95, 53, 29]

    # Testando a lista pequena
    start_time = time.time()
    print("Testando a lista pequena:")
    selection_sort(small_list)
    print("Tempo de execução: %.6f segundos" % (time.time() - start_time))
    print("\n")

    # Testando a lista média
    start_time = time.time()
    print("Testando a lista média:")
    selection_sort(medium_list)
    print("Tempo de execução: %.6f segundos" % (time.time() - start_time))
    print("\n")

    # Testando a lista grande
    start_time = time.time()
    print("Testando a lista grande:")
    selection_sort(large_list)
    print("Tempo de execução: %.6f segundos" % (time.time() - start_time))
    print("\n")

if __name__ == "__main__":
    test_selection_sort()
