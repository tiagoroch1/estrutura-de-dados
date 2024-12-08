def binary_search(arr, target):
    """
    Implementação do algoritmo Binary Search.
    :param arr: Lista ordenada onde a busca será realizada.
    :param target: Elemento a ser encontrado.
    :return: Índice do elemento encontrado ou -1 se não estiver presente.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Calcula o índice do meio
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Ajusta a busca para a direita
        else:
            right = mid - 1  # Ajusta a busca para a esquerda

    return -1  # Elemento não encontrado