from binary_search_isbn import binary_search_isbn

def exibir_resultado(lista, isbn, indice):
    if indice != -1:
        print(f"O ISBN {isbn} foi encontrado na posição {indice} da lista.")
    else:
        print(f"O ISBN {isbn} não foi encontrado na lista.")

def salvar_resultado(lista, isbn, indice):
    with open("busca_isbn.txt", "w") as f:
        f.write("### Resultados da Busca por ISBN\n\n")
        f.write("Lista de ISBNs ordenada:\n")
        f.write(", ".join(lista) + "\n\n")
        if indice != -1:
            f.write(f"O ISBN {isbn} foi encontrado na posição {indice} da lista.\n")
        else:
            f.write(f"O ISBN {isbn} não foi encontrado na lista.\n")

# Dados de teste
isbn_lista = [
    "978-3-16-148410-0",
    "978-1-4028-9462-6",
    "978-0-545-01022-1",
    "978-0-7432-7356-5",
    "978-1-86197-876-9"
]
isbn_lista.sort()  # Garantir que a lista está ordenada
isbn_procurado = "978-0-545-01022-1"

# Executando a busca
indice_encontrado = binary_search_isbn(isbn_lista, isbn_procurado)

# Exibindo os resultados
exibir_resultado(isbn_lista, isbn_procurado, indice_encontrado)

# Salvando os resultados
salvar_resultado(isbn_lista, isbn_procurado, indice_encontrado)
