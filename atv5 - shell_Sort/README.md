# Shell Sort

## Descrição
O **Shell Sort** é um algoritmo de ordenação que melhora a eficiência do Insertion Sort ao permitir que elementos distantes sejam trocados, reduzindo o número de movimentações necessárias à medida que o algoritmo avança.

Neste projeto, foram implementadas três variações do Shell Sort com diferentes sequências de intervalo:
1. **Shell**: A sequência mais simples, onde o intervalo começa em metade do tamanho da lista e é reduzido pela metade em cada iteração.
2. **Knuth**: A sequência gerada pela fórmula `3^k - 1`, que aumenta mais rapidamente do que a sequência de Shell.
3. **Hibbard**: A sequência gerada pela fórmula `2^k - 1`, que é mais eficiente em listas maiores.

O objetivo é comparar o desempenho das diferentes sequências em termos de tempo de execução.

## Implementação

### Algoritmo:

```python
# Funções para Shell Sort, Knuth Shell Sort e Hibbard Shell Sort estão no arquivo 'shell_sort.py'.
