# Atividade 1 - Binary Search

Este diretório contém a implementação do algoritmo **Binary Search** e seus testes.

## **Descrição**
O Binary Search é um algoritmo de busca eficiente em listas ordenadas. Ele utiliza o princípio de dividir e conquistar, reduzindo pela metade o espaço de busca a cada iteração.

### **Funcionamento**
1. Inicialize dois ponteiros: `left` (início da lista) e `right` (fim da lista).
2. Calcule o índice do meio: `mid = (left + right) // 2`.
3. Compare o elemento no índice `mid` com o alvo:
   - Se forem iguais, retorne o índice `mid`.
   - Se o alvo for menor, mova o ponteiro `right` para `mid - 1`.
   - Se o alvo for maior, mova o ponteiro `left` para `mid + 1`.
4. Repita até encontrar o elemento ou esgotar o espaço de busca.

---

## **Arquivos**
- `binary_search.py`: Contém a implementação do algoritmo.
- `testes.py`: Casos de teste automatizados para validar o funcionamento.
- `descricao.txt`: Explicação detalhada e exemplos de execução.

---

## **Como Executar**

1. Navegue até esta pasta:
   ```bash
   cd atividade_1
