# generation.py
import random

def generer_labyrinthe_parfait(largeur, hauteur):
    """
    Génère un labyrinthe parfait de taille `largeur x hauteur` avec l'algorithme de Kruskal.
    Retourne un dictionnaire représentant le graphe (liste d'adjacence).
    """
    sommets = [(i, j) for i in range(hauteur) for j in range(largeur)]
    arêtes = []

    # Générer toutes les arêtes possibles (horizontales et verticales)
    for i in range(hauteur):
        for j in range(largeur):
            if i < hauteur - 1:
                arêtes.append(((i, j), (i + 1, j)))
            if j < largeur - 1:
                arêtes.append(((i, j), (i, j + 1)))

    # Mélanger les arêtes
    random.shuffle(arêtes)

    # Initialiser les structures pour Union-Find
    parent = {sommet: sommet for sommet in sommets}
    rank = {sommet: 0 for sommet in sommets}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Compression de chemin
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return False  # Déjà dans le même ensemble
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
            if rank[x_root] == rank[y_root]:
                rank[x_root] += 1
        return True

    # Initialiser le graphe
    graphe = {sommet: [] for sommet in sommets}

    # Appliquer Kruskal
    for u, v in arêtes:
        if union(u, v):
            graphe[u].append((v, 1))
            graphe[v].append((u, 1))

    return graphe
