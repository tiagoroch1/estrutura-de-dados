from interpolation_search import interpolation_search

def test_interpolation_search():
    """
    Testa o algoritmo Interpolation Search com diferentes listas.
    """
    # Lista com intervalos uniformes
    lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    testes_uniformes = [
        (30, 2),
        (70, 6),
        (5, -1)
    ]

    print("Testes com lista uniforme:")
    for target, esperado in testes_uniformes:
        resultado = interpolation_search(lista_uniforme, target)
        assert resultado == esperado, f"Erro: {target}, esperado {esperado}, obtido {resultado}"
        print(f"Teste para elemento {target}: OK")

    # Lista com intervalos não uniformes
    lista_nao_uniforme = [1, 4, 7, 13, 25, 36, 47, 59, 73, 91]
    testes_nao_uniformes = [
        (13, 3),
        (59, 7),
        (100, -1)
    ]

    print("\nTestes com lista não uniforme:")
    for target, esperado in testes_nao_uniformes:
        resultado = interpolation_search(lista_nao_uniforme, target)
        assert resultado == esperado, f"Erro: {target}, esperado {esperado}, obtido {resultado}"
        print(f"Teste para elemento {target}: OK")

if __name__ == "__main__":
    test_interpolation_search()
