# Ternary Search

Este projeto implementa o algoritmo **Ternary Search**, utilizado para localizar elementos em listas ordenadas. Também há uma comparação entre o desempenho do Ternary Search e o Binary Search.

---

## Descrição

O **Ternary Search** é uma extensão do **Binary Search**, dividindo a lista em três partes em vez de duas. Apesar de realizar mais comparações por iteração, ele pode ser útil em alguns cenários.

### Como funciona:
1. Divide a lista em três partes usando os índices `mid1` e `mid2`.
2. Compara o elemento-alvo com os valores em `mid1` e `mid2`.
3. Reduz o espaço de busca para a parte apropriada:
   - Entre `left` e `mid1 - 1`, se o alvo for menor que `arr[mid1]`.
   - Entre `mid1 + 1` e `mid2 - 1`, se o alvo estiver entre `arr[mid1]` e `arr[mid2]`.
   - Entre `mid2 + 1` e `right`, se o alvo for maior que `arr[mid2]`.

---

## Arquivos

- **`ternary_search.py`**: Implementação do Ternary Search.
- **`binary_search.py`**: Implementação do Binary Search.
- **`testes.py`**: Código para testar ambos os algoritmos.
- **`dados.txt`**: Resultados das execuções.
- **`README.md`**: Explicação do projeto.

---

## Resultados

| Tamanho da Lista | Ternary Search (s) | Binary Search (s) |
|-------------------|--------------------|--------------------|
| 10               | 0.000001          | 0.000001          |
| 1.000            | 0.000004          | 0.000003          |
| 100.000          | 0.000065          | 0.000055          |

### Conclusão:
O **Binary Search** é ligeiramente mais rápido devido ao menor número de comparações.

---

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
