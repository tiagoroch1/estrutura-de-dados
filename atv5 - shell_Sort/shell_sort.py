# Função para o Shell Sort com a sequência de intervalo de Shell
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Começamos com a sequência de Shell (dividir por 2)
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# Função para o Shell Sort com a sequência de Knuth
def knuth_shell_sort(arr):
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1  # Sequência de Knuth
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3
    return arr


# Função para o Shell Sort com a sequência de Hibbard
def hibbard_shell_sort(arr):
    n = len(arr)
    gap = 1
    while gap <= n // 3:
        gap = 2 * gap + 1  # Sequência de Hibbard
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = (gap - 1) // 2  # Diminuindo o gap usando a sequência de Hibbard
    return arr
