# Bucket Sort

## Descrição

O **Bucket Sort** é um algoritmo de ordenação que distribui os elementos de uma lista em "baldes", ordena cada balde individualmente e, em seguida, concatena os baldes ordenados para formar a lista final ordenada. Ele é particularmente eficaz para ordenar números distribuídos de forma uniforme ao longo de um intervalo.

## Como Funciona

1. Para números flutuantes no intervalo [0, 1), os números são mapeados para baldes com base no valor multiplicado pelo número de baldes.
2. Para números inteiros, o intervalo entre o valor mínimo e máximo é dividido pelos baldes, e os números são alocados em baldes com base em seu valor.
3. Cada balde é ordenado (geralmente com o método `sorted()`).
4. Os baldes ordenados são concatenados para formar a lista final ordenada.

### Exemplo de Uso

#### Ordenação de números flutuantes no intervalo [0, 1):

```python
arr = [0.42, 0.32, 0.12, 0.53, 0.11]
sorted_arr = bucket_sort_float(arr)
print("Lista ordenada:", sorted_arr)
