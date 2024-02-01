import networkx as nx

def encontrar_combinacoes(lista, resultado_desejado):
    # Criação do grafo ponderado
    G = nx.Graph()
    G.add_nodes_from(lista)

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            # Calcula a média entre dois números
            media = (lista[i] + lista[j]) / 2
            # Adiciona uma aresta ponderada ao grafo
            G.add_edge(lista[i], lista[j], weight=media)

    # Encontrar caminhos no grafo que levam à média desejada
    caminhos = []
    for node in lista:
        for path in nx.all_simple_paths(G, source=node, target=resultado_desejado):
            caminhos.append(path)

    return caminhos

# Exemplo de uso
lista_numeros = [20, 10, 2, 0, 999, 60]
resultado_desejado = 6

resultados = encontrar_combinacoes(lista_numeros, resultado_desejado)
print("Caminhos que levam à média desejada:")
for caminho in resultados:
    print(caminho)
