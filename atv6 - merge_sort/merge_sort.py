# Função para ordenar números inteiros usando Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2  # encontra o meio da lista
        esquerda = arr[:meio]  # divide a lista em duas partes
        direita = arr[meio:]

        merge_sort(esquerda)  # ordena a metade esquerda
        merge_sort(direita)  # ordena a metade direita

        i = j = k = 0

        # Mescla as duas metades ordenadas
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        # Verifica se algum elemento da metade esquerda ou direita ainda não foi copiado
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

# Função para ordenar strings em ordem alfabética com Merge Sort
def merge_sort_strings(arr):
    if len(arr) > 1:
        meio = len(arr) // 2  # encontra o meio da lista
        esquerda = arr[:meio]  # divide a lista em duas partes
        direita = arr[meio:]

        merge_sort_strings(esquerda)  # ordena a metade esquerda
        merge_sort_strings(direita)  # ordena a metade direita

        i = j = k = 0

        # Mescla as duas metades ordenadas
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        # Verifica se algum elemento da metade esquerda ou direita ainda não foi copiado
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1
