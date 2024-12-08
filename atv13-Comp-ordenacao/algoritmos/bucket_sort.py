# bucket_sort.py

def bucket_sort(arr):
    comparisons = 0
    if len(arr) == 0:
        return comparisons

    min_value, max_value = min(arr), max(arr)
    bucket_count = len(arr)

    # Se todos os números forem iguais, não haverá necessidade de mais baldes.
    if min_value == max_value:
        return comparisons

    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        # Corrigido: Garantindo que o índice não ultrapasse o número de baldes
        index = int(bucket_count * (num - min_value) / (max_value - min_value))
        index = min(index, bucket_count - 1)  # Garantir que o índice está no intervalo válido
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()
        comparisons += len(bucket) * (len(bucket) - 1) // 2

    arr[:] = [item for bucket in buckets for item in bucket]
    return comparisons
