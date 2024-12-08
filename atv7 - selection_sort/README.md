# Selection Sort

## Descrição

O **Selection Sort** é um algoritmo de ordenação simples que trabalha selecionando repetidamente o menor (ou maior) valor da lista e trocando-o com o primeiro elemento da parte não ordenada da lista.

## Como Funciona

1. O algoritmo encontra o menor valor da lista e coloca-o na primeira posição.
2. Depois, encontra o menor valor da sublista restante e coloca-o na segunda posição, e assim por diante, até que toda a lista esteja ordenada.

### Complexidade

- **Tempo**: O tempo de execução do Selection Sort é **O(n²)**, onde n é o número de elementos na lista. Isso ocorre porque, para cada elemento, o algoritmo precisa percorrer a lista inteira para encontrar o menor valor.
- **Espaço**: O algoritmo utiliza apenas uma quantidade constante de memória extra (**O(1)**), já que ele é realizado in-place.

### Desempenho

O algoritmo é simples e fácil de entender, mas não é eficiente para grandes conjuntos de dados, pois seu tempo de execução cresce quadraticamente à medida que o número de elementos aumenta. Para listas pequenas, no entanto, pode ser uma boa escolha.

### Exemplo de Uso

```python
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Lista ordenada:", arr)
