def selection_sort(arr):
    n = len(arr)
    # Iterando sobre cada posição do array
    for i in range(n):
        # Encontrar o menor elemento na parte não ordenada
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Trocar o menor elemento encontrado com o elemento da posição i
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Imprimir o estado da lista a cada iteração
        print(f"Iteração {i + 1}: {arr}")

# Teste com diferentes tamanhos de lista
if __name__ == "__main__":
    # Lista de exemplo para teste
    small_list = [64, 25, 12, 22, 11]
    print("Ordenando a lista pequena:")
    selection_sort(small_list)
    print("\n")
    
    medium_list = [64, 25, 12, 22, 11, 45, 33, 20, 18, 37]
    print("Ordenando a lista média:")
    selection_sort(medium_list)
    print("\n")
    
    large_list = [64, 25, 12, 22, 11, 45, 33, 20, 18, 37, 88, 13, 42, 7, 95, 53, 29]
    print("Ordenando a lista grande:")
    selection_sort(large_list)
