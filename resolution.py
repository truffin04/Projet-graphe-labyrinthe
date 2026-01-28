# resolution.py
import math

def dijkstra(graphe, départ, arrivée):
    """
    Implémente l'algorithme de Dijkstra pour trouver le chemin le plus court entre `départ` et `arrivée` dans `graphe`.
    Le graphe est représenté comme un dictionnaire de listes d'adjacence : {sommet: [(voisin, poids), ...]}.

    Args:
        graphe (dict): Dictionnaire représentant le graphe.
        départ (tuple): Sommet de départ.
        arrivée (tuple): Sommet d'arrivée.

    Returns:
        list: Chemin le plus court sous forme de liste de sommets, ou une liste vide si aucun chemin n'existe.
    """
    # Initialisation des distances et des précédents
    distances = {sommet: math.inf for sommet in graphe}
    précédents = {sommet: None for sommet in graphe}
    distances[départ] = 0

    # Liste des sommets non traités (file de priorité simplifiée)
    sommets_non_traites = set(graphe.keys())

    while sommets_non_traites:
        # Trouver le sommet avec la plus petite distance parmi les sommets non traités
        sommet_courant = min(sommets_non_traites, key=lambda sommet: distances[sommet])
        sommets_non_traites.remove(sommet_courant)

        # Si on atteint l'arrivée, on peut s'arrêter
        if sommet_courant == arrivée:
            break

        # Mettre à jour les distances des voisins
        for voisin, poids in graphe[sommet_courant]:
            nouvelle_distance = distances[sommet_courant] + poids
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                précédents[voisin] = sommet_courant

    # Reconstruire le chemin
    chemin = []
    sommet = arrivée
    while sommet is not None:
        chemin.append(sommet)
        sommet = précédents[sommet]
    chemin.reverse()

    # Vérifier si un chemin valide a été trouvé
    return chemin if chemin[0] == départ else []
