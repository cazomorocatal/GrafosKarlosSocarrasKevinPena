import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_weighted_edges_from([
    ('A', 'B', 2), ('A', 'C', 5), ('B', 'C', 1),
    ('C', 'D', 3), ('D', 'E', 4), ('E', 'B', 2)
])

print(nx.to_pandas_adjacency(G, dtype=float, weight='weight'))
print("Euler:", nx.has_eulerian_path(G))

def hamilton(G):
    def buscar(camino):
        if len(camino) == len(G):
            encontrado[0] = camino
        else:
            for vecino in G.successors(camino[-1]):
                if vecino not in camino and encontrado[0] is None:
                    buscar(camino + [vecino])

    encontrado = [None]
    for inicio in G.nodes:
        if encontrado[0] is None:
            buscar([inicio])
    print("Hamilton:", encontrado[0] is not None)
    print("Camino Hamilton:", encontrado[0])

hamilton(G)

nx.draw(G, with_labels=True, node_color='lightblue', node_size=1400, arrows=True)
plt.show()