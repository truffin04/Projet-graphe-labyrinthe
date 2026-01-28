import networkx as nx
import matplotlib.pyplot as plt

def visualiser_labyrinthe(graphe, chemin=None, taille_sommet=300, taille_figure=(10, 8)):
    """
    Visualise le labyrinthe (graphe) avec le chemin solution en rouge.

    Args:
        graphe (dict): Dictionnaire représentant le graphe (liste d'adjacence).
        chemin (list): Liste des sommets représentant le chemin solution.
        taille_sommet (int): Taille des sommets dans la visualisation.
        taille_figure (tuple): Taille de la figure Matplotlib.
    """
    # Créer un graphe NetworkX
    G = nx.Graph()

    # Ajouter les sommets et les arêtes
    for sommet in graphe:
        G.add_node(sommet)
        for voisin, _ in graphe[sommet]:
            G.add_edge(sommet, voisin)

    # Préparer les couleurs des arêtes
    edge_colors = []
    for u, v in G.edges():
        # Si l'arête fait partie du chemin, la colorier en rouge
        if chemin and ((u in chemin and v in chemin and
                       abs(chemin.index(u) - chemin.index(v)) == 1)):
            edge_colors.append('red')
        else:
            edge_colors.append('gray')

    # Dessiner le graphe
    pos = {sommet: (sommet[1], -sommet[0]) for sommet in G.nodes()}  # Inverser y pour afficher correctement
    plt.figure(figsize=taille_figure)

    # Dessiner les arêtes
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

    # Dessiner les sommets
    nx.draw_networkx_nodes(G, pos, node_size=taille_sommet, node_color='skyblue')

    # Dessiner les étiquettes des sommets
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Ajouter une légende
    plt.scatter([], [], c='red', label='Chemin solution')
    plt.scatter([], [], c='gray', label='Arêtes du labyrinthe')
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1)

    plt.title("Labyrinthe avec chemin solution")
    plt.axis('off')
    plt.show()
