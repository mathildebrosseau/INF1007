import random
import constantes as c


import numpy as np

def demarrer_jeu():
    matrice = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    ligne = random.randint(0,3)
    colonne = random.randint(0,3)
    nombre_ajouts = 0
    while nombre_ajouts < 2:
        if matrice[ligne][colonne] == 0:
            matrice[ligne][colonne] = random.choice([2,4])
            nombre_ajouts += 1
            ligne = random.randint(0, 3)
            colonne = random.randint(0, 3)
    return matrice

def initialiser_nouvelle_matrice():
    nouvelle_matrice = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return nouvelle_matrice


def ajouter_nouveau_2_ou_4(grille):
    ligne = random.randint(0, 3)
    colonne = random.randint(0, 3)
    ajout = 0
    while ajout != 1:
        if grille[ligne][colonne] == 0:
            ajout = 1
            Hasard = random.randint(0, 9)
            if Hasard == 9:
                grille[ligne][colonne] = 4
            if Hasard < 9:
                grille[ligne][colonne] = 2
        ligne = random.randint(0, 3)
        colonne = random.randint(0, 3)
    return grille

def get_etat_jeu_courant(grille):
    existe_element_nul = False
    existe_mouvement_possible = False

    for ligne in grille:
        for element in ligne:
            if element == 2048:
                return c.ETAT_VICTOIRE
            elif element == 0:
                existe_element_nul = True
    for ligne in range(len(grille) - 1):
        for colonne in range(len(grille[ligne]) - 1):
            if grille[ligne][colonne] == grille[ligne][colonne + 1] or grille[ligne][colonne] == grille[ligne + 1][colonne]:
                existe_mouvement_possible = True
    if existe_mouvement_possible or existe_element_nul:
        return c.ETAT_PARTIE_EN_COURS
    else:
        return c.ETAT_DEFAITE

def comprimer(matrice):
    matrice_comprimee = initialiser_nouvelle_matrice()
    changement_effectue = False
    colonne_comprimee = 0
    for ligne in range(len(matrice)):
        colonne_comprimee = 0
        for colonne in range(len(matrice[ligne])):
            if matrice[ligne][colonne] != 0:
                matrice_comprimee[ligne][colonne_comprimee] = matrice[ligne][colonne]
                colonne_comprimee += 1
                changement_effectue = True
    return matrice_comprimee, changement_effectue


def fusionner(matrice):
    changement = False
    for ligne in matrice:
        for elem in range(len(ligne) - 1):
            if ligne[elem] == ligne[elem + 1] and ligne[elem] == 0:
                ligne[elem] = elem * 2
                ligne[elem + 1] = 0
                changement = True
    return matrice, changement


if __name__ == '__main__':
    #print(demarrer_jeu())
    #print(ajouter_nouveau_2_ou_4([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    #print(get_etat_jeu_courant([[256, 2, 512, 8], [4, 16, 4, 16], [2, 1024, 256, 2], [1024, 2, 8, 16]]))
    print(comprimer([[0, 0, 4, 2], [8, 0, 2, 16], [0, 2, 0, 4], [0, 0, 0, 4]]))


    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a.size)

    print(fusionner([[0, 0, 4, 2], [8, 0, 2, 16], [0, 2, 0, 4], [0, 0, 0, 4]]))

    print(random)