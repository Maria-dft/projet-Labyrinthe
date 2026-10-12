Fonction relier(graphe : tableau d'entiers [10][10], a : entier, b : entier) : tableau d'entiers
    graphe[a][b] ← 1
    graphe[b][a] ← 1
    Retourner graphe
Fin Fonction

Fonction creerGraphe() : tableau d'entiers
    Variable graphe : tableau d'entiers [10][10]
    Variable i, j : entier

    Pour i de 0 à 9 par pas de 1 faire
        Pour j de 0 à 9 par pas de 1 faire
            graphe[i][j] ← 0
        Fin Pour
    Fin Pour

    graphe ← relier(graphe, 0, 1)
    graphe ← relier(graphe, 1, 2)
    graphe ← relier(graphe, 1, 4)
    graphe ← relier(graphe, 2, 3)
    graphe ← relier(graphe, 2, 5)
    graphe ← relier(graphe, 5, 6)
    graphe ← relier(graphe, 6, 7)
    graphe ← relier(graphe, 6, 8)
    graphe ← relier(graphe, 8, 9)

    Retourner graphe
Fin Fonction

Fonction chercher(graphe : tableau d'entiers [10][10], depart : entier, arrivee : entier,
                  visite : tableau de booléens [10], chemin : liste d'entiers) : booléen
    Variable voisin : entier

    visite[depart] ← vrai
    Ajouter(chemin, depart)

    Si depart = arrivee alors
        Retourner vrai
    Fin Si

    Pour voisin de 0 à 9 par pas de 1 faire
        Si graphe[depart][voisin] = 1 alors
            Si visite[voisin] = faux alors
                Si chercher(graphe, voisin, arrivee, visite, chemin) = vrai alors
                    Retourner vrai
                Fin Si
            Fin Si
        Fin Si
    Fin Pour

    Retirer(chemin)
    Retourner faux
Fin Fonction

Fonction resoudreLabyrinthe(graphe : tableau d'entiers [10][10], depart : entier,
                            arrivee : entier) : liste d'entiers
    Variable visite : tableau de booléens [10]
    Variable chemin : liste d'entiers
    Variable i : entier

    Pour i de 0 à 9 par pas de 1 faire
        visite[i] ← faux
    Fin Pour
    chemin ← liste vide

    Si chercher(graphe, depart, arrivee, visite, chemin) = vrai alors
        Retourner chemin
    Sinon
        Retourner liste vide
    Fin Si
Fin Fonction

Variable DEBUT : entier ← 0
Variable FIN : entier ← 9
Variable graphe : tableau d'entiers [10][10]
Variable noms : tableau de textes ← ["A","B","C","D","E","F","G","H","I","J"]
Variable resultat : liste d'entiers
Variable k : entier

graphe ← creerGraphe()
resultat ← resoudreLabyrinthe(graphe, DEBUT, FIN)

Si taille(resultat) > 0 alors
    Pour k de 0 à taille(resultat) - 1 par pas de 1 faire
        Afficher(noms[resultat[k]])
    Fin Pour
Sinon
    Afficher("Aucun chemin trouvé")
Fin Si
