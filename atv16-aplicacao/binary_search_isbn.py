def binary_search_isbn(arr, target):
    """
    Busca um ISBN em uma lista ordenada usando o Binary Search.

    Args:
        arr (list): Lista ordenada de ISBNs.
        target (str): ISBN a ser buscado.

    Returns:
        int: Índice do ISBN na lista, ou -1 se não encontrado.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
