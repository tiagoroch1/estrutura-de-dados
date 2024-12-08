# visualizacao.py
import matplotlib.pyplot as plt
import random

def merge_sort(arr, visualizations):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, visualizations)
        merge_sort(right, visualizations)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        visualizations.append(arr.copy())  # Adiciona o estado atual do array

def quick_sort(arr, low, high, visualizations):
    if low < high:
        pi = partition(arr, low, high, visualizations)
        quick_sort(arr, low, pi - 1, visualizations)
        quick_sort(arr, pi + 1, high, visualizations)

def partition(arr, low, high, visualizations):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        visualizations.append(arr.copy())  # Adiciona o estado atual do array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    visualizations.append(arr.copy())  # Adiciona o estado atual do array
    return i + 1

def selection_sort(arr, visualizations):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualizations.append(arr.copy())  # Adiciona o estado atual do array

def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]
