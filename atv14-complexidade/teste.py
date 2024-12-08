from complexidade import analise_buscas, analise_ordenacoes

def exibir_tabela(dados):
    print(f"{'Algoritmo':<20}{'Melhor Caso':<15}{'Pior Caso':<15}{'Espaço':<10}")
    print("-" * 60)
    for item in dados:
        print(f"{item['algoritmo']:<20}{item['melhor']:<15}{item['pior']:<15}{item['espaco']:<10}")

def salvar_resultados(buscas, ordenacoes):
    with open("resultados/analise_complexidade.txt", "w") as f:
        f.write("### Análise de Complexidade\n\n")
        f.write("#### Algoritmos de Busca\n")
        f.write(f"{'Algoritmo':<20}{'Melhor Caso':<15}{'Pior Caso':<15}{'Espaço':<10}\n")
        f.write("-" * 60 + "\n")
        for item in buscas:
            f.write(f"{item['algoritmo']:<20}{item['melhor']:<15}{item['pior']:<15}{item['espaco']:<10}\n")
        f.write("\n#### Algoritmos de Ordenação\n")
        f.write(f"{'Algoritmo':<20}{'Melhor Caso':<15}{'Pior Caso':<15}{'Espaço':<10}\n")
        f.write("-" * 60 + "\n")
        for item in ordenacoes:
            f.write(f"{item['algoritmo']:<20}{item['melhor']:<15}{item['pior']:<15}{item['espaco']:<10}\n")

# Executando as análises
buscas = analise_buscas()
ordenacoes = analise_ordenacoes()

print("### Análise de Complexidade de Buscas ###")
exibir_tabela(buscas)
print("\n### Análise de Complexidade de Ordenações ###")
exibir_tabela(ordenacoes)

# Salvando em arquivo
salvar_resultados(buscas, ordenacoes)
