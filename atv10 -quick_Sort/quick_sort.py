def quick_sort(arr, pivot_choice='last'):
    """Função para realizar o Quick Sort com diferentes critérios de escolha do pivô"""
    
    if len(arr) <= 1:
        return arr
    
    # Escolher o pivô com base no critério selecionado
    if pivot_choice == 'first':
        pivot = arr[0]
    elif pivot_choice == 'last':
        pivot = arr[-1]
    elif pivot_choice == 'middle':
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Critério de pivô inválido")
    
    # Particiona a lista em duas partes
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    # Para o caso em que existem elementos iguais ao pivô, eles ficam no meio
    middle = [x for x in arr if x == pivot]

    # Recursivamente aplica o Quick Sort nas duas partes
    return quick_sort(left, pivot_choice) + middle + quick_sort(right, pivot_choice)

