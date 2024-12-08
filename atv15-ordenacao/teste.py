from algoritmos.merge_sort_strings import merge_sort_strings
from algoritmos.quick_sort_strings import quick_sort_strings
from algoritmos.binary_search_strings import binary_search_strings

def exibir_resultados(lista, sorted_merge, sorted_quick, palavra, resultado_busca):
    print("Lista original:")
    print(lista)
    print("\nOrdenação com Merge Sort:")
    print(sorted_merge)
    print("\nOrdenação com Quick Sort:")
    print(sorted_quick)
    print(f"\nResultado da busca pela palavra '{palavra}': {resultado_busca}")

def salvar_resultados(lista, sorted_merge, sorted_quick, palavra, resultado_busca):
    with open("ordenacao_busca_strings.txt", "w") as f:
        f.write("### Busca e Ordenação em Strings\n\n")
        f.write("Lista original:\n")
        f.write(", ".join(lista) + "\n\n")
        f.write("Ordenação com Merge Sort:\n")
        f.write(", ".join(sorted_merge) + "\n\n")
        f.write("Ordenação com Quick Sort:\n")
        f.write(", ".join(sorted_quick) + "\n\n")
        f.write(f"Resultado da busca pela palavra '{palavra}': {resultado_busca}\n")

# Dados de teste
lista_palavras = ["banana", "maçã", "uva", "laranja", "abacaxi", "pêssego"]
palavra_busca = "uva"

# Ordenando com Merge Sort
sorted_merge = merge_sort_strings(lista_palavras.copy())

# Ordenando com Quick Sort
sorted_quick = quick_sort_strings(lista_palavras.copy())

# Busca Binária
resultado_busca = binary_search_strings(sorted_merge, palavra_busca)

# Exibindo os resultados
exibir_resultados(lista_palavras, sorted_merge, sorted_quick, palavra_busca, resultado_busca)

# Salvando os resultados
salvar_resultados(lista_palavras, sorted_merge, sorted_quick, palavra_busca, resultado_busca)
