# Atividade 18 - Estabilidade dos Algoritmos de Ordenação

### Objetivo
Nesta atividade, exploramos o conceito de estabilidade em algoritmos de ordenação, identificando quais são estáveis e quais não são, e demonstrando com exemplos.

### Como Funciona

- **Estabilidade:** Um algoritmo é estável se mantém a ordem relativa de elementos iguais.
- **Exemplo:**
  - Entrada: [("A", 3), ("B", 2), ("C", 3), ("D", 2)]
  - Saída Estável: [("B", 2), ("D", 2), ("A", 3), ("C", 3)]
  - Saída Instável: [("D", 2), ("B", 2), ("C", 3), ("A", 3)]

### Como Rodar

1. Execute o arquivo `teste.py` para visualizar a diferença entre os algoritmos estáveis e instáveis.
2. O script demonstra os resultados usando uma lista de tuplas contendo elementos repetidos.

### Algoritmos Demonstrados

1. **Estável:** Merge Sort (utilizando a função `sorted` do Python).
2. **Instável:** Selection Sort.

---

Este arquivo descreve a implementação da Atividade 18 e os resultados obtidos.
