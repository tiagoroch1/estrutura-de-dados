def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Encontrar o valor máximo e o valor mínimo
    min_val = min(arr)
    max_val = max(arr)

    # Definir o número de baldes
    bucket_count = 10
    bucket_range = (max_val - min_val) / bucket_count

    # Inicializar os baldes como listas vazias
    buckets = [[] for _ in range(bucket_count)]

    # Preencher os baldes
    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index == bucket_count:  # Garantir que o número máximo vá para o último balde
            index -= 1
        buckets[index].append(num)

    # Ordenar os baldes e concatenar os resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

# Teste com uma lista de números flutuantes
if __name__ == "__main__":
    arr = [0.42, 0.32, 0.12, 0.53, 0.11, 0.22, 0.41, 0.34, 0.28]
    print("Lista original:", arr)
    sorted_arr = bucket_sort(arr)
    print("Lista ordenada:", sorted_arr)
