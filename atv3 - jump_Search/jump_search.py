import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # Tamanho do salto
    prev = 0
    
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Elemento não encontrado
    
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    
    return -1  # Elemento não encontrado
