from binary_search import binary_search

def test_binary_search():
    """
    Testa o algoritmo Binary Search com diferentes casos.
    """
    # Lista ordenada de exemplo
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Lista de teste:", lista)
    
    # Casos de teste
    testes = [
        (7, 3),    # Elemento 7 está no índice 3
        (1, 0),    # Elemento 1 está no índice 0
        (19, 9),   # Elemento 19 está no índice 9
        (8, -1),   # Elemento 8 não está na lista
        (21, -1)   # Elemento 21 não está na lista
    ]

    for target, esperado in testes:
        resultado = binary_search(lista, target)
        assert resultado == esperado, f"Erro: {target}, esperado {esperado}, obtido {resultado}"
        print(f"Teste para elemento {target}: OK")

if __name__ == "__main__":
    test_binary_search()
