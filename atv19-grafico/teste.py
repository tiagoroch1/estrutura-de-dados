# teste.py
import matplotlib.pyplot as plt

from visualizacao import merge_sort, quick_sort, selection_sort, generate_random_list

# Função para gerar visualizações para os três algoritmos
def plot_visualization(algorithm, arr, algorithm_name):
    visualizations = []
    if algorithm_name == 'Merge Sort':
        merge_sort(arr, visualizations)
    elif algorithm_name == 'Quick Sort':
        quick_sort(arr, 0, len(arr) - 1, visualizations)
    elif algorithm_name == 'Selection Sort':
        selection_sort(arr, visualizations)

    # Plotando as visualizações
    plt.figure(figsize=(10, 6))
    for i, v in enumerate(visualizations):
        plt.clf()
        plt.bar(range(len(v)), v, color='skyblue')
        plt.title(f'{algorithm_name} - Step {i + 1}')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.pause(0.5)  # Pausa para visualizar o gráfico
    plt.show()

# Gerando uma lista aleatória para visualização
arr = generate_random_list(20)

# Plotando visualizações para os três algoritmos
plot_visualization(merge_sort, arr.copy(), 'Merge Sort')
plot_visualization(quick_sort, arr.copy(), 'Quick Sort')
plot_visualization(selection_sort, arr.copy(), 'Selection Sort')
