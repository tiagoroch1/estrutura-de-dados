# Merge Sort

## Descrição

O **Merge Sort** é um algoritmo de ordenação eficiente baseado na técnica de "dividir para conquistar". O algoritmo divide recursivamente uma lista em sublistas menores, até que cada sublista tenha apenas um elemento, e depois as mescla de volta em uma lista ordenada.

### Como Funciona

1. **Divisão**: A lista é dividida em duas metades até que cada sublista tenha um único elemento.
2. **Mesclagem**: Sublistas são combinadas em ordem crescente até que a lista inteira esteja ordenada.

### Complexidade

- **Tempo**: O Merge Sort tem uma complexidade de tempo de **O(n log n)**, onde `n` é o número de elementos na lista.
- **Espaço**: O Merge Sort tem uma complexidade de espaço de **O(n)**, pois exige memória extra para armazenar sublistas temporárias.

### Vantagens

- **Estabilidade**: O Merge Sort preserva a ordem relativa de elementos iguais na lista.
- **Eficiência**: Ele é eficiente para listas grandes e tem um desempenho consistente de **O(n log n)**.
  
### Desvantagens

- **Uso de Memória**: O Merge Sort usa memória adicional para armazenar as sublistas, o que pode ser um problema quando se trabalha com listas muito grandes.

## Como Usar

### Pré-requisitos

- Python 3.x

### Execução

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
