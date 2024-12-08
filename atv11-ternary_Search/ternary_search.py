def ternary_search(arr, left, right, x):
    """
    Implementa o Ternary Search em uma lista ordenada.
    :param arr: Lista ordenada onde será realizada a busca.
    :param left: Índice inicial da lista.
    :param right: Índice final da lista.
    :param x: Elemento a ser buscado.
    :return: Índice do elemento encontrado ou -1 se não existir.
    """
    if left > right:
        return -1

    # Dividindo a lista em 3 partes
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # Comparando o elemento com as duas posições intermediárias
    if arr[mid1] == x:
        return mid1
    if arr[mid2] == x:
        return mid2

    # Decidindo em qual parte continuar a busca
    if x < arr[mid1]:
        return ternary_search(arr, left, mid1 - 1, x)
    elif x > arr[mid2]:
        return ternary_search(arr, mid2 + 1, right, x)
    else:
        return ternary_search(arr, mid1 + 1, mid2 - 1, x)
