## Descrição

O **Interpolation Search** é um algoritmo de busca eficiente para listas ordenadas de números, especialmente quando os dados estão uniformemente distribuídos. Ao contrário do **Binary Search**, que divide a lista ao meio a cada iteração, o **Interpolation Search** tenta estimar onde o valor procurado pode estar, com base nos valores extremos da lista.

### Como funciona o Interpolation Search:
1. O algoritmo começa com dois índices, `low` e `high`, representando as extremidades da lista.
2. Ele faz uma estimativa da posição do elemento com base na fórmula:
   \[
   pos = low + \frac{(x - arr[low]) * (high - low)}{arr[high] - arr[low]}
   \]
   Onde `x` é o elemento procurado, `arr[low]` é o valor na extremidade inferior e `arr[high]` é o valor na extremidade superior da lista.
3. Se o valor estimado está dentro dos limites da lista e é igual ao elemento procurado, o algoritmo retorna o índice. Caso contrário, ele ajusta os limites `low` e `high` e repete o processo.

### Comparação com o Binary Search:

- **Binary Search**: Divide a lista em dois, buscando a posição do elemento em cada iteração. Sua eficiência é garantida, com complexidade de tempo O(log n).
- **Interpolation Search**: Faz uma estimativa da posição com base nos valores da lista, o que pode ser mais rápido em listas uniformemente distribuídas. Sua complexidade de tempo no melhor caso é O(log log n), mas no pior caso pode ser O(n), quando os dados não são uniformemente distribuídos.

### Casos em que o Interpolation Search é mais eficiente que o Binary Search:

1. **Distribuição Uniforme**: O **Interpolation Search** é muito eficiente em listas onde os valores estão uniformemente distribuídos. Isso porque ele calcula a posição de forma mais inteligente, ao invés de dividir a lista ao meio a cada iteração.
   - Exemplo: Se você estiver procurando um número em uma lista de preços de produtos que estão em uma faixa de preços contínua e uniforme, o **Interpolation Search** pode localizar o elemento mais rapidamente.

2. **Grandes listas ordenadas**: Quando a lista é grande e os dados são distribuídos de forma quase uniforme, o **Interpolation Search** pode ser mais rápido que o **Binary Search**, pois realiza menos comparações ao "pular" para a posição estimada.

### Complexidade de Tempo:
- **Interpolation Search**:
  - Melhor Caso: O(log log n)
  - Pior Caso: O(n) (quando os dados são mal distribuídos ou são todos iguais)
- **Binary Search**:
  - Melhor e Pior Caso: O(log n)

### Comparação de Desempenho:

Neste repositório, comparamos o **Interpolation Search** com o **Binary Search** em termos de tempo de execução. O **Binary Search** é mais eficiente para dados que não são uniformemente distribuídos, enquanto o **Interpolation Search** pode ser mais rápido quando os dados são distribuídos de maneira mais regular.

## Estrutura dos Arquivos

- `interpolation_search.py`: Contém a implementação do **Interpolation Search**.
- `testes.py`: Arquivo de teste que executa o **Interpolation Search** e o **Binary Search** em listas ordenadas e mede o tempo de execução de ambos os algoritmos.
- `descricao.txt`: Descrição detalhada sobre o funcionamento do **Interpolation Search** e suas vantagens.
- `README.md`: Este arquivo, que contém a explicação do projeto.

## Como rodar

Para rodar os testes, execute o arquivo `testes.py` com o seguinte comando:

```bash
python testes.py

