def interpolation_search(arr, target):
    """
    Implementação do algoritmo Interpolation Search.
    :param arr: Lista ordenada onde a busca será realizada.
    :param target: Elemento a ser encontrado.
    :return: Índice do elemento encontrado ou -1 se não estiver presente.
    """
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
        if pos < 0 or pos >= len(arr):
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
