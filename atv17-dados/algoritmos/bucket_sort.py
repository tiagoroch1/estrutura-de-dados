# bucket_sort.py

def bucket_sort(arr):
    # Definindo o número de baldes
    n = len(arr)
    if n <= 1:
        return arr
    
    # Encontrando o valor mínimo e máximo na lista
    min_val = min(arr)
    max_val = max(arr)
    
    # Calculando o intervalo de cada balde
    bucket_range = (max_val - min_val) / n + 1
    
    # Inicializando os baldes
    buckets = [[] for _ in range(n)]
    
    # Distribuindo os elementos nos baldes
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)
    
    # Ordenando os baldes e concatenando os resultados
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))
    
    return result
