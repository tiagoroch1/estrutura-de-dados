def bucket_sort_notas(notas):
    """Ordena notas entre 0 e 100 usando Bucket Sort."""
    buckets = [[] for _ in range(11)]  # 10 intervalos: [0-10), [10-20), ..., [90-100]
    
    for nota in notas:
        index = min(10, nota // 10)  # Nota de 0 a 100 -> índice de 0 a 10
        buckets[index].append(nota)
    
    for bucket in buckets:
        bucket.sort()  # Ordena cada balde individualmente
    
    sorted_notas = []
    for bucket in buckets:
        sorted_notas.extend(bucket)
    
    return sorted_notas
