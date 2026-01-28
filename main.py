from generation import generer_labyrinthe_parfait
from resolution import dijkstra
from visualisation import visualiser_labyrinthe

def afficher_chemin(chemin):
    """Affiche le chemin sous une forme lisible."""
    if not chemin:
        print("Aucun chemin trouvé.")
        return
    print("Chemin trouvé :")
    for i, sommet in enumerate(chemin):
        print(f"Étape {i}: {sommet}")

def main():
    # Paramètres du labyrinthe
    largeur = 10
    hauteur = 10

    # Générer le labyrinthe
    print(f"Génération d'un labyrinthe parfait de taille {largeur}x{hauteur}...")
    labyrinthe = generer_labyrinthe_parfait(largeur, hauteur)
    print("Labyrinthe généré avec succès !")

    # Définir le départ et l'arrivée
    départ = (0, 0)
    arrivée = (hauteur - 1, largeur - 1)
    print(f"Départ : {départ}, Arrivée : {arrivée}")

    # Résoudre le labyrinthe avec Dijkstra
    print("Recherche du chemin le plus court...")
    chemin = dijkstra(labyrinthe, départ, arrivée)

    # Afficher le chemin
    afficher_chemin(chemin)

    # Visualiser le labyrinthe et le chemin
    if chemin:
        visualiser_labyrinthe(labyrinthe, chemin)

if __name__ == "__main__":
    main()
