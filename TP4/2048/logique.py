"""
 Programme qui définit deux cas des tests pour chacune des fonctions du fichier logique.py
 \file   logique.py
 \author Maxime Appert et Mathilde Brosseau
 \date   12 novembre 2020
 Créé le 5 novembre 2020
"""


# logique.py est importé par gui.py
# Ce fichier consiste en la logique du jeu 2048


import random
import constantes as c


# TODO:
#  Initialisation du jeu
#  1. Dans une nouvelle matrice, ajouter deux fois (un 2 ou un 4)
def demarrer_jeu():
    """
    Retourne une matrice 4x4 dont 2 éléments sont 2 ou 4 et tous les autres sont 0.

            Paramètres:
                    aucun

            Valeurs de retour:
                    matrice (list): matrice 4x4 dont 2 éléments sont 2 ou 4 et tous les autres sont 0.
    """

    matrice = initialiser_nouvelle_matrice()
    nombre_ajouts = 0

    while nombre_ajouts < 2:
        ligne = random.randint(0, 3)
        colonne = random.randint(0, 3)
        if matrice[ligne][colonne] == 0:
            matrice[ligne][colonne] = random.choice([2, 4])
            nombre_ajouts += 1

    return matrice


# TODO:
#  Retourner une nouvelle matrice 4x4 remplie de 0
def initialiser_nouvelle_matrice():
    """
    Retourne une matrice 4x4 nulle.

            Paramètres:
                    aucun

            Valeurs de retour:
                    matrice (list): matrice 4x4 dont tous les éléments sont 0.
    """

    nouvelle_matrice = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return nouvelle_matrice


# TODO:
#  Ajout d'un 2 ou d'un 4 a la matrice du jeu avec des probabilités de: 90% 2 et 10% 4
#  dans un emplacement vide aléatoire de la matrice (emplacement == 0)
#  Modifie le paramètre grille et retourne la grille modifiée.
def ajouter_nouveau_2_ou_4(grille):
    """
    Ajoute un 2 ou un 4 à une matrice et retourne la matrice résultante.

            Paramètres:
                    grille (list): matrice 4x4 quelconque

            Valeurs de retour:
                    grille (list): matrice 4x4 correspondant à la matrice intiale à laquelle un 2 (90% de chances) ou
                                   un 4 (10% de chances) ont été ajoutés.
    """

    ligne = random.randint(0, c.TAILLE_GRILLE - 1)
    colonne = random.randint(0, c.TAILLE_GRILLE - 1)
    ajout = 0

    while ajout != 1:
        if grille[ligne][colonne] == 0:
            ajout = 1
            hasard = random.randint(0, 9)  # probabilité de 9/10 d'avoir un 2 et de 1/10 d'avoir un 4
            if hasard == 9:
                grille[ligne][colonne] = 4
            if hasard < 9:
                grille[ligne][colonne] = 2
        else:
            ligne = random.randint(0, c.TAILLE_GRILLE - 1)
            colonne = random.randint(0, c.TAILLE_GRILLE - 1)

    return grille


# TODO:
#  Retourner l'état du jeu
#  Les valeurs retournées sont les états définis dans constantes.py (ETAT_x)
#  ex: return c.ETAT_VICTOIRE
#  1. Victoire
#    a) Si un élément de la matrice == 2048
#  2. Le jeu n'est pas fini
#    a) S'il y a au moins un élément == 0
#    b) OU S'il n'y a aucune cellule vide, MAIS qu'il y a un (ou des) mouvements possibles
#  3. Défaite
#    a) Les cas restants
def get_etat_jeu_courant(grille):
    """
    Retourne l'état courant de la partie, soit Victoire si la grille contient l'élément 2048, Partie en cours si la
    grille contient au moins un 0 ou deux éléments adjacents identiques et Défaite dans les cas restants.

            Paramètres:
                    grille (list): matrice 4x4 quelconque

            Valeurs de retour:
                    etat (str): string correspondant à l'état courant de la partie, soit Victoire si la grille contient
                                l'élément 2048, Partie en cours si la grille contient au moins un 0 ou deux éléments
                                adjacents identiques et Défaite dans les cas restants.
    """

    etat = c.ETAT_DEFAITE

    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne] == 2048:
                etat = c.ETAT_VICTOIRE
                return etat
            if grille[ligne][colonne] == 0:
                etat = c.ETAT_PARTIE_EN_COURS
            if ligne < 3:
                if grille[ligne][colonne] == grille[ligne + 1][colonne] or grille[ligne][colonne] == 0:
                    etat = c.ETAT_PARTIE_EN_COURS
            if colonne < 3:
                if grille[ligne][colonne] == grille[ligne][colonne + 1] or grille[ligne][colonne] == 0:
                    etat = c.ETAT_PARTIE_EN_COURS

    return etat


# NOTE: Les fonctions suivantes sont pour le mouvement gauche seulement

# TODO:
#  Comprimer la matrice de jeu.
#  À effectuer après toutes les étapes avant et après le fusionnement des éléments
#    a) Initialiser une nouvelle matrice remplie de 0 initialement.
#    b) Bouger tous les éléments à son extrême gauche, lorsque possible
#        b.a) SEULEMENT possible lorsque l'élément à gauche == 0
#        b.b) PAS POSSIBLE si gauche != 0
#    c) Retourner la nouvelle matrice comprimée, avec un booléen indiquant s'il y a au moins eu
#       1 changement
def comprimer(matrice):
    """
    Aligne tous les éléments non-nuls de la matrice passée en paramètre à l'extrême gauche puis retourne la matrice
    résultante et indique s'il y a eu un changement.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    matrice_comprimee (list): matrice 4x4 correspondant à la matrice initiale, mais où tous les éléments
                                              non-nuls sont alignés à l'extrême gauche.
                    changement (bool): booléen qui indique si la matrice initiale a subi un changement.
    """

    matrice_comprimee = initialiser_nouvelle_matrice()
    changement = False

    for ligne in range(len(matrice)):
        colonne_comprimee = 0
        for colonne in range(len(matrice[ligne])):
            if matrice[ligne][colonne] != 0:
                matrice_comprimee[ligne][colonne_comprimee] = matrice[ligne][colonne]
                colonne_comprimee += 1
                changement = True

    return matrice_comprimee, changement


# TODO:
#  Fusionner les éléments de la matrice après une compression
#  1) Si l'élément a la même valeur que le prochain élément dans la ligne
#     ET qu'ils sont non vides (!= 0)
#     ALORS doubler la valeur de l'élément courant ET vider l'élément suivant
#  2) Retourner la matrice fusionnée et un booléen indiquant s'il y a eu un changement
def fusionner(matrice):
    """
    Additionne les éléments adjacents identiques d'une ligne de la matrice passée en paramètre, comble la ligne de 0
    puis retourne la matrice résultante et indique s'il y a eu un changement.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    matrice (list): matrice 4x4 correspondant à la matrice initiale, mais où tous les éléments adjacents
                                    identiques ont été additionnés et les lignes ont été comblées de 0.
                    changement (bool): booléen qui indique si la matrice initiale a subi un changement.
    """

    changement = False

    for ligne in matrice:
        for elem in range(len(ligne) - 1):
            if ligne[elem] == ligne[elem + 1] and ligne[elem] != 0:
                ligne[elem] = ligne[elem] * 2
                ligne[elem + 1] = 0
                changement = True

    return matrice, changement


# TODO:
#  Inverser la matrice
#  1) Dans une nouvelle matrice,
#     inverser la séquence dans chaque ligne de la matrice
#  2) Retourner la nouvelle matrice
def inverser(matrice):
    """
    Inverse l'ordre des éléments de chacune des lignes de la matrice passée en paramètre et retourne la matrice
    résultante.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    matrice_inversee (list): matrice 4x4 correspondant à la matrice initiale, mais l'ordre des
                                             éléments de chaque ligne est inversé.
    """

    matrice_inversee = initialiser_nouvelle_matrice()

    for i in range(len(matrice)):
        matrice_inversee[i] = matrice[i][::-1]

    return matrice_inversee


# TODO:
#  Transposer la matrice
#  1) Dans une nouvelle matrice,
#     Échanger les lignes avec les colonnes
#  2) Retourner la nouvelle matrice
def transposer(matrice):
    """
    Retourne la transposée de la matrice passée en paramètre.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    matrice_transposee (list): matrice 4x4 correspondant à la transposée de la matrice initiale.
    """

    matrice_transposee = initialiser_nouvelle_matrice()

    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[ligne])):
            matrice_transposee[ligne][colonne] = matrice[colonne][ligne]

    return matrice_transposee


# NOTE: Les fonctions suivantes servent à gérer un mouvement dans la matrice.


# TODO:
#  Bouger la matrice à gauche
#  1) Dans une nouvelle matrice
#    a) Comprimer la matrice
#    b) Fusionner la matrice
#    c) Recomprimer la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_gauche(matrice):
    """
    Comprime, fusionne et re-comprime la matrice passée en paramètre (donc fait la translation vers la gauche), puis
    retourne la matrice résultante et indique s'il y a eu un changement.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    nouvelle_matrice (list): matrice 4x4 correspondant à la matrice initiale ayant subi une translation
                                             vers la gauche.
                    changement (bool): booléen qui indique si la matrice initiale a subi un changement.
    """

    nouvelle_matrice = initialiser_nouvelle_matrice()

    for i in range(len(matrice)):
        nouvelle_matrice[i] = matrice[i]

    nouvelle_matrice = comprimer(fusionner(comprimer(nouvelle_matrice)[0])[0])[0]

    if matrice == nouvelle_matrice:
        changement = False
    else:
        changement = True

    return nouvelle_matrice, changement


# TODO:
#  Bouger la matrice à droite
#  1) Dans une nouvelle matrice
#    a) Inverser la matrice pour simuler un mouvement à gauche
#    b) Bouger la matrice à gauche
#    c) Re-inverser la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_droite(matrice):
    """
    Inverse, fait la translation vers la gauche et re-inverse la matrice passée en paramètre (donc fait la translation
    vers la droite), puis retourne la matrice résultante et indique s'il y a eu un changement.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    nouvelle_matrice (list): matrice 4x4 correspondant à la matrice initiale ayant subi une translation
                                             vers la droite.
                    changement (bool): booléen qui indique si la matrice initiale a subi un changement.
    """

    nouvelle_matrice = initialiser_nouvelle_matrice()

    for i in range(len(matrice)):
        nouvelle_matrice[i] = matrice[i]

    nouvelle_matrice = inverser(faire_translation_gauche(inverser(nouvelle_matrice))[0])

    if matrice == nouvelle_matrice:
        changement = False
    else:
        changement = True

    return nouvelle_matrice, changement


# TODO:
#  Bouger la matrice en haut
#  1) Dans une nouvelle matrice
#    a) Transposer la matrice pour simuler un mouvement à gauche
#    b) Bouger la matrice à gauche
#    c) Re-transposer la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_haut(matrice):
    """
    Transpose, fait la translation vers la gauche et re-transpose la matrice passée en paramètre (donc fait la
    translation vers le haut), puis retourne la matrice résultante et indique s'il y a eu un changement.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    nouvelle_matrice (list): matrice 4x4 correspondant à la matrice initiale ayant subi une translation
                                             vers le haut.
                    changement (bool): booléen qui indique si la matrice initiale a subi un changement.
    """

    nouvelle_matrice = initialiser_nouvelle_matrice()

    for i in range(len(matrice)):
        nouvelle_matrice[i] = matrice[i]

    nouvelle_matrice = transposer(faire_translation_gauche(transposer(nouvelle_matrice))[0])

    if matrice == nouvelle_matrice:
        changement = False
    else:
        changement = True

    return nouvelle_matrice, changement


# TODO:
#  Bouger la matrice en bas
#  1) Dans une nouvelle matrice
#    a) Transposer la matrice pour simuler un mouvement à droite
#    b) Bouger la matrice à droite
#    c) Re-transposer la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_bas(matrice):
    """
    Transpose, fait la translation vers la droite et re-transpose la matrice passée en paramètre (donc fait la
    translation vers le bas), puis retourne la matrice résultante et indique s'il y a eu un changement.

            Paramètres:
                    matrice (list): matrice 4x4 quelconque

            Valeurs de retour:
                    nouvelle_matrice (list): matrice 4x4 correspondant à la matrice initiale ayant subi une translation
                                             vers le bas.
                    changement (bool): booléen qui indique si la matrice initiale a subi un changement.
    """

    nouvelle_matrice = initialiser_nouvelle_matrice()

    for i in range(len(matrice)):
        nouvelle_matrice[i] = matrice[i]

    nouvelle_matrice = transposer(faire_translation_droite(transposer(nouvelle_matrice))[0])

    if matrice == nouvelle_matrice:
        changement = False
    else:
        changement = True

    return nouvelle_matrice, changement
