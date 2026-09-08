import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()


G.add_weighted_edges_from([
    ('Hospital Central', 'Clinica Norte', 2),
    ('Hospital Central', 'Centro Lab', 5),
    ('Clinica Norte', 'Centro Lab', 1),
    ('Centro Lab', 'Hospital Sur', 3),
    ('Hospital Sur', 'Planta Reciclaje', 4),
    ('Planta Reciclaje', 'Clinica Norte', 2)
])

print("--- MATRIZ DE ADYACENCIA (DISTANCIAS EN KM) ---")
print(nx.to_pandas_adjacency(G, dtype=float, weight='weight'))

print("\n--- EVALUACIÓN DE RUTAS ---")
print("¿Existe camino Euleriano (recorrer todas las calles sin repetir)?:", nx.has_eulerian_path(G))

# Algoritmo para encontrar el camino Hamiltoniano
def hamilton_residuos(G):
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
            
    print("¿Existe ruta Hamiltoniana (visitar cada sede una sola vez)?:", encontrado[0] is not None)
    print("\nRuta optima asignada al camion:")
    if encontrado[0]:
        print(" -> ".join(encontrado[0]))

hamilton_residuos(G)

# Visualización del grafo con nombres completos
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos, 
    with_labels=True, 
    node_color='lightgreen', 
    node_size=3000, 
    arrowsize=20, 
    font_size=8, 
    font_weight='bold'
)

# Dibujar los pesos (distancias) en las aristas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)

plt.title("Red de Recolección de Residuos Hospitalarios")
plt.tight_layout()
plt.show()
