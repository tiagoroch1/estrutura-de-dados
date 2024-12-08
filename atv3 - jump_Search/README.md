# Atividade 3 - Jump Search

## Descrição

O Jump Search é um algoritmo de busca eficiente para listas ordenadas. Ele divide a lista em intervalos (ou "saltos") e realiza uma busca linear quando um intervalo adequado é encontrado. O algoritmo é mais eficiente do que a busca linear, pois reduz o número de comparações necessárias, mas ainda é menos eficiente do que o Binary Search em alguns casos.

### Como funciona o Jump Search:
1. O algoritmo começa com um salto de tamanho √n, onde n é o tamanho da lista.
2. Ele "salta" até encontrar um valor maior ou igual ao elemento procurado.
3. Quando encontra esse valor, ele realiza uma busca linear dentro do intervalo identificado.
4. O algoritmo retorna o índice do elemento encontrado ou -1 se não encontrar o elemento.

## Algoritmos de Busca Compa
