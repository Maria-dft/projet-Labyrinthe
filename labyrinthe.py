def relier(graphe, a, b):
    graphe[a][b] = 1
    graphe[b][a] = 1
    return graphe


def creerGraphe():
    graphe = []

    for i in range(10):
        ligne = []
        for j in range(10):
            ligne.append(0)
        graphe.append(ligne)

    graphe = relier(graphe, 0, 1)
    graphe = relier(graphe, 1, 2)
    graphe = relier(graphe, 1, 4)
    graphe = relier(graphe, 2, 3)
    graphe = relier(graphe, 2, 5)
    graphe = relier(graphe, 5, 6)
    graphe = relier(graphe, 6, 7)
    graphe = relier(graphe, 6, 8)
    graphe = relier(graphe, 8, 9)

    return graphe


def chercher(graphe, depart, arrivee, visite, chemin):
    visite[depart] = True
    chemin.append(depart)

    if depart == arrivee:
        return True

    for voisin in range(10):
        if graphe[depart][voisin] == 1:
            if visite[voisin] == False:
                if chercher(graphe, voisin, arrivee, visite, chemin) == True:
                    return True

    chemin.pop()
    return False


def resoudreLabyrinthe(graphe, depart, arrivee):
    visite = []
    for i in range(10):
        visite.append(False)

    chemin = []

    if chercher(graphe, depart, arrivee, visite, chemin) == True:
        return chemin
    else:
        return []


DEBUT = 0
FIN = 9
noms = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

graphe = creerGraphe()
resultat = resoudreLabyrinthe(graphe, DEBUT, FIN)

if len(resultat) > 0:
    for k in range(len(resultat)):
        print(noms[resultat[k]], end=" ")
    print()
else:
    print("Aucun chemin trouvé")