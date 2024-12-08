import random
from comparacao import comparar_algoritmos

def gerar_lista(tamanho):
    return [random.randint(1, 1000) for _ in range(tamanho)]

def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Testar algoritmos de busca")
    print("2. Testar algoritmos de ordenação")
    print("3. Comparar algoritmos")
    print("4. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            tamanho = int(input("Digite o tamanho da lista: "))
            arr = gerar_lista(tamanho)
            target = int(input("Digite o elemento a ser buscado: "))
            print("\nTestando algoritmos de busca...")
            comparar_algoritmos(arr, target)
        
        elif escolha == "2":
            tamanho = int(input("Digite o tamanho da lista: "))
            arr = gerar_lista(tamanho)
            print("\nTestando algoritmos de ordenação...")
            comparar_algoritmos(arr, None)
        
        elif escolha == "3":
            tamanho = int(input("Digite o tamanho da lista: "))
            arr = gerar_lista(tamanho)
            target = int(input("Digite o elemento a ser buscado: "))
            print("\nComparando algoritmos de busca e ordenação...")
            comparar_algoritmos(arr, target)
        
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
