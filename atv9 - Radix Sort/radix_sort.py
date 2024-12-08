def counting_sort(arr, exp):
    """Função auxiliar para fazer Counting Sort baseado no dígito específico (exp)"""
    n = len(arr)
    output = [0] * n  # Lista para armazenar a saída
    count = [0] * 10  # Contador para dígitos de 0 a 9

    # Armazenar a contagem de ocorrências dos dígitos
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Alterar count[i] para que count[i] agora contenha a posição real no output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir o array de saída
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiar o array de saída para arr[], para que arr[] agora tenha os números ordenados
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """Função principal para realizar o Radix Sort"""
    # Encontrar o número máximo para determinar o número de dígitos
    max_val = max(arr)

    # Aplicar counting sort para cada dígito (começando do menos significativo)
    exp = 1  # Aumenta a base exponencial a cada iteração
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Multiplica exp por 10 para mover para o próximo dígito

    return arr

if __name__ == "__main__":
    # Teste 1: Números com 2 dígitos
    arr_2_digits = [29, 17, 35, 72, 51, 64]
    print("Lista original (2 dígitos):", arr_2_digits)
    sorted_arr_2_digits = radix_sort(arr_2_digits)
    print("Lista ordenada (2 dígitos):", sorted_arr_2_digits)
    print()

    # Teste 2: Números com 5 dígitos
    arr_5_digits = [12234, 56789, 98765, 34567, 12345]
    print("Lista original (5 dígitos):", arr_5_digits)
    sorted_arr_5_digits = radix_sort(arr_5_digits)
    print("Lista ordenada (5 dígitos):", sorted_arr_5_digits)
    print()

    # Teste 3: Números com 10 dígitos
    arr_10_digits = [1234567890, 9876543210, 1357924680, 2468013579]
    print("Lista original (10 dígitos):", arr_10_digits)
    sorted_arr_10_digits = radix_sort(arr_10_digits)
    print("Lista ordenada (10 dígitos):", sorted_arr_10_digits)
