def analise_buscas():
    buscas = [
        {"algoritmo": "Binary Search", "melhor": "O(1)", "pior": "O(log n)", "espaco": "O(1)"},
        {"algoritmo": "Interpolation Search", "melhor": "O(1)", "pior": "O(n)", "espaco": "O(1)"},
        {"algoritmo": "Jump Search", "melhor": "O(1)", "pior": "O(√n)", "espaco": "O(1)"},
        {"algoritmo": "Exponential Search", "melhor": "O(1)", "pior": "O(log n)", "espaco": "O(1)"},
        {"algoritmo": "Ternary Search", "melhor": "O(1)", "pior": "O(log n)", "espaco": "O(1)"}
    ]
    return buscas

def analise_ordenacoes():
    ordenacoes = [
        {"algoritmo": "Merge Sort", "melhor": "O(n log n)", "pior": "O(n log n)", "espaco": "O(n)"},
        {"algoritmo": "Quick Sort", "melhor": "O(n log n)", "pior": "O(n²)", "espaco": "O(log n)"},
        {"algoritmo": "Selection Sort", "melhor": "O(n²)", "pior": "O(n²)", "espaco": "O(1)"},
        {"algoritmo": "Shell Sort", "melhor": "O(n log n)", "pior": "O(n²)", "espaco": "O(1)"},
        {"algoritmo": "Bucket Sort", "melhor": "O(n)", "pior": "O(n²)", "espaco": "O(n + k)"},
        {"algoritmo": "Radix Sort", "melhor": "O(nk)", "pior": "O(nk)", "espaco": "O(n + k)"}
    ]
    return ordenacoes
