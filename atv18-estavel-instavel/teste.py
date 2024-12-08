# teste.py

from stability_check import stable_sort_example, unstable_sort_example

# Exemplo de lista com elementos repetidos
arr = [
    ("A", 3),
    ("B", 2),
    ("C", 3),
    ("D", 2),
    ("E", 1),
]

# Usando o algoritmo estável
stable_result = stable_sort_example(arr.copy())
print("Resultado da Ordenação Estável (Merge Sort):")
print(stable_result)

# Usando o algoritmo instável
unstable_result = unstable_sort_example(arr.copy())
print("\nResultado da Ordenação Instável (Selection Sort):")
print(unstable_result)
