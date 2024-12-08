# Exponential Search

## Descrição
O **Exponential Search** é um algoritmo de busca eficiente usado para encontrar um elemento em uma lista ordenada. Ele combina a ideia de pesquisa exponencial para localizar uma faixa onde o elemento pode estar e, em seguida, utiliza **Binary Search** para realizar a busca dentro dessa faixa.

Este algoritmo é particularmente útil quando a lista é muito grande, mas os elementos estão distribuídos de maneira a permitir uma busca exponencial inicial eficaz.

## Como Funciona
1. **Busca Exponencial**: Inicialmente, o algoritmo verifica o primeiro, segundo, quarto, oitavo, etc., elementos da lista (cada vez exponencialmente maior). Isso cria uma "janela" onde o elemento pode estar.
2. **Binary Search**: Após localizar a janela em que o elemento está, o algoritmo realiza uma busca binária entre os dois elementos encontrados durante a busca exponencial.

A combinação da busca exponencial e da busca binária torna o Exponential Search muito eficiente, especialmente em listas ordenadas grandes.

## Implementação

A implementação foi feita em Python. O código encontra um elemento específico em uma lista ordenada usando o Exponential Search e o Binary Search.

### Algoritmo:

```python
def binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, right, x)
    return -1

def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, len(arr)-1), x)
