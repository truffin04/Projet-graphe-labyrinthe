# Projet de Graphes : Génération et Résolution d'un Labyrinthe Parfait

**Auteur** : Tom Ruffin
**Date de début** : 21 janvier 2026
**Cours** : BUT Informatique - S2 - Graphes

---

## Description du projet

Ce projet a pour but de **générer un labyrinthe parfait** (un labyrinthe avec un seul chemin entre deux points quelconques) à l'aide de la théorie des graphes, puis de le résoudre en utilisant l'**algorithme de Dijkstra**. Le labyrinthe est modélisé comme un graphe, où chaque intersection ou case est un sommet et chaque chemin est une arête.

### Objectifs pédagogiques
- Comprendre la modélisation d'un **labyrinthe** en un **graphe**.
- Implémenter des algorithmes classiques de la théorie des graphes : **Kruskal** (pour la génération) et **Dijkstra** (pour la résolution).
- Visualiser un graphe et ses propriétés à l'aide de la bibliothèque `networkx`.

---

## Technologies et bibliothèques utilisées

- **Python 3.11** : Langage principal du projet.
- **NetworkX** : Pour la création, la manipulation et la visualisation des graphes.
- **Matplotlib** : Pour l'affichage du graphe et du labyrinthe.
- **Algorithmes** :
  - **Kruskal** : Génération du labyrinthe parfait (arbre couvrant minimal).
  - **Dijkstra** : Résolution du labyrinthe (chemin le plus court).

---

## Installation

### Prérequis
- Python 3.11 ou supérieur installé sur votre machine.
- Les bibliothèques `networkx` et `matplotlib` (pour la visualisation).

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/truffin04/Projet-graphe-labyrinthe.git
   
