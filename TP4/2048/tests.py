"""
 Programme qui définit deux cas des tests pour chacune des fonctions du fichier logique.py
 \file   tests.py
 \author Maxime Appert et Mathilde Brosseau
 \date   12 novembre 2020
 Créé le 5 novembre 2020
"""


# Définissez et implémentez ici la liste des fonctions de tests responsables des tests de chacune des fonctions de
# logique.py


import logique


def tester_demarrer_jeu():
    # Test de la fonction demarrer_jeu du fichier logique.py en vérifiant si deux éléments de la matrice générée par
    #   cette fonction sont 2 ou 4

    matrice_demaree = logique.demarrer_jeu()
    compteur = 0

    for ligne in matrice_demaree:
        for elem in ligne:
            if elem == 2 or elem == 4:
                compteur += 1

    return compteur == 2


def tester_initialiser_nouvelle_matrice():
    # Test de la fonction initialiser_nouvelle_matrice du fichier logique.py en vérifiant si la matrice générée par
    #   cette fonction est bien la matrice nulle.
    matrice_attendue = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

    return logique.initialiser_nouvelle_matrice() == matrice_attendue


def tester_ajouter_nouveau_2_ou_4_remplie():
    # Test 1 de la fonction ajouter_nouveau_2_ou_4 du fichier logique.py en vérifiant si la fonction transforme bien la
    #   matrice remplie qu'on lui passe en paramètre en la matrice attendue.

    grille = [[3, 1, 0, 21],
              [8, 9, 2, 32],
              [7, 16, 5, 64],
              [8, 2, 1, 58]]

    grille_attendue_2 = [[3, 1, 2, 21],
                         [8, 9, 2, 32],
                         [7, 16, 5, 64],
                         [8, 2, 1, 58]]

    grille_attendue_4 = [[3, 1, 4, 21],
                         [8, 9, 2, 32],
                         [7, 16, 5, 64],
                         [8, 2, 1, 58]]

    return logique.ajouter_nouveau_2_ou_4(grille) == (grille_attendue_2 or grille_attendue_4)


def tester_ajouter_nouveau_2_ou_4_identite():
    # Test 2 de la fonction ajouter_nouveau_2_ou_4 du fichier logique.py en vérifiant si la matrice résultante de cette
    #   fonction lorsqu'on lui passe en paramètre la matrice identité contient bien un 2 ou un 4.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_ajouter = logique.ajouter_nouveau_2_ou_4(matrice)
    compteur = 0

    for ligne in matrice_ajouter:
        for elem in ligne:
            if elem == 2 or elem == 4:
                compteur += 1

    return compteur == 1


def tester_get_etat_jeu_courant_victoire():
    # Test 1 de la fonction get_etat_jeu_courant du fichier logique.py en vérifiant si la fonction retourne bien l'état
    #   de victoire lorsque la matrice passée en paramètre contient 2048.

    grille = [[3, 1, 0, 21],
              [8, 9, 2, 32],
              [7, 16, 2048, 64],
              [8, 2, 1, 58]]

    attendue = "Victoire"

    return attendue == logique.get_etat_jeu_courant(grille)


def tester_get_etat_jeu_courant_defaite():
    # Test 2 de la fonction get_etat_jeu_courant du fichier logique.py en vérifiant si la fonction retourne bien l'état
    #   de défaite lorsque la matrice passée en paramètre ne contient aucun élément nul et qu'aucun mouvement n'est
    #   possible.

    grille = [[3, 1, 9, 21],
              [8, 9, 2, 32],
              [7, 16, 8, 64],
              [8, 2, 1, 58]]

    attendue = "Défaite"

    return attendue == logique.get_etat_jeu_courant(grille)


def tester_get_etat_jeu_courant():
    # Test 3 de la fonction get_etat_jeu_courant du fichier logique.py en vérifiant si la fonction retourne bien l'état
    #   de partie en cours lorsque la matrice passée en paramètre a au moins un mouvement possible (donc deux éléments
    #   côte à côte sont identiques).

    matrice = [[4, 4, 9, 256],
               [9, 8, 512, 2],
               [16, 52, 64, 782],
               [2, 4, 28, 32]]

    attendue = "Partie en cours"

    return attendue == logique.get_etat_jeu_courant(matrice)


def tester_comprimer_remplie():
    # Test 1 de la fonction comprimer du fichier logique.py en vérifiant si la fonction n'apporte aucun changement à la
    #   matrice passée en paramètre lorsque celle-ci n'a pas d'éléments nuls.

    matrice = [[1, 9, 63, 54],
               [43, 1, 27, 12],
               [4, 69, 1, 32],
               [8, 3, 49, 1]]

    return matrice == logique.comprimer(matrice)[0]


def tester_comprimer_identite():
    # Test 2 de la fonction comprimer du fichier logique.py en vérifiant si la fonction retourne la matrice attendue
    #   lorsqu'on lui passe la matrice identité en paramètre.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_attendue = [[1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]]

    return matrice_attendue == logique.comprimer(matrice)[0]


def tester_fusionner_impossible():
    # Test 1 de la fonction fusionner du fichier logique.py en vérifiant si la fonction n'apporte aucun changement à la
    #   matrice passée en paramètre lorsque celle-ci n'a pas d'éléments adjacents identiques (donc la fusion est
    #   impossible).

    matrice = [[1, 9, 63, 54],
               [43, 1, 27, 12],
               [4, 69, 1, 32],
               [8, 3, 49, 1]]

    return matrice == logique.fusionner(matrice)[0]


def tester_fusionner_possible():
    # Test 2 de la fonction fusionner du fichier logique.py en vérifiant si la fonction retourne la matrice attendue
    #   lorsqu'on lui passe une certaine matrice posédant deux éléments identiques adjacents en paramètre (donc la
    #   fusion est possible).

    matrice = [[1, 9, 63, 54],
               [43, 1, 27, 12],
               [4, 4, 1, 32],
               [8, 3, 49, 1]]

    matrice_attendue = [[1, 9, 63, 54],
                        [43, 1, 27, 12],
                        [8, 0, 1, 32],
                        [8, 3, 49, 1]]

    return matrice_attendue == logique.fusionner(matrice)[0]


def tester_inverser_matrice_identite():
    # Test 1 de la fonction inverser_matrice du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe la matrice identité en paramètre.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_attendue = [[0, 0, 0, 1],
                        [0, 0, 1, 0],
                        [0, 1, 0, 0],
                        [1, 0, 0, 0]]

    return logique.inverser(matrice) == matrice_attendue


def tester_inverser_matrice_remplie():
    # Test 2 de la fonction inverser_matrice du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe une certaine matrice remplie en paramètre.

    matrice = [[1, 9, 63, 54],
               [43, 1, 27, 12],
               [4, 69, 1, 32],
               [8, 3, 49, 1]]

    matrice_attendue = [[54, 63, 9, 1],
                        [12, 27, 1, 43],
                        [32, 1, 69, 4],
                        [1, 49, 3, 8]]

    return logique.inverser(matrice) == matrice_attendue


def tester_transposer_matrice_identite():
    # Test 1 de la fonction transposer du fichier logique.py en vérifiant si la fonction ne subit aucun changement
    #  lorsqu'on lui passe la matrice identité en paramètre.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    return logique.transposer(matrice) == matrice


def tester_transposer_matrice_remplie():
    # Test 2 de la fonction transposer du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe une certaine matrice remplie en paramètre.

    matrice = [[1, 9, 63, 54],
               [43, 1, 27, 12],
               [4, 69, 1, 32],
               [8, 3, 49, 1]]

    matrice_attendue = [[1, 43, 4, 8],
                        [9, 1, 69, 3],
                        [63, 27, 1, 49],
                        [54, 12, 32, 1]]

    return logique.transposer(matrice) == matrice_attendue


def tester_translation_gauche():
    # Test 1 de la fonction translation_gauche du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe la matrice identité en paramètre.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_attendue = [[1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]]

    ecrire_resultat_test("tester_translation_gauche 1",
                         matrice_attendue == logique.faire_translation_gauche(matrice)[0])

    # Test 2 de la fonction translation_gauche du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe une certaine matrice remplie en paramètre.

    matrice = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]

    matrice_attendue = [[2, 2, 0, 0],
                        [2, 2, 0, 0],
                        [2, 2, 0, 0],
                        [2, 2, 0, 0]]

    return matrice_attendue == logique.faire_translation_gauche(matrice)[0]


def tester_translation_droite():
    # Test 1 de la fonction translation_droite du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe la matrice identité en paramètre.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_attendue = [[0, 0, 0, 1],
                        [0, 0, 0, 1],
                        [0, 0, 0, 1],
                        [0, 0, 0, 1]]

    ecrire_resultat_test("tester_translation_droite 1",
                         matrice_attendue == logique.faire_translation_droite(matrice)[0])

    # Test 2 de la fonction translation_droite du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe une certaine matrice remplie en paramètre.

    matrice = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]

    matrice_attendue = [[0, 0, 2, 2],
                        [0, 0, 2, 2],
                        [0, 0, 2, 2],
                        [0, 0, 2, 2]]

    return matrice_attendue == logique.faire_translation_droite(matrice)[0]


def tester_translation_haut():
    # Test 1 de la fonction translation_haut du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe la matrice identité en paramètre.
    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_attendue = [[1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

    ecrire_resultat_test("tester_translation_haut 1", matrice_attendue == logique.faire_translation_haut(matrice)[0])

    # Test 2 de la fonction translation_haut du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe une certaine matrice remplie en paramètre.

    matrice = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]

    matrice_attendue = [[2, 2, 2, 2],
                        [2, 2, 2, 2],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

    return matrice_attendue == logique.faire_translation_haut(matrice)[0]


def tester_translation_bas():
    # Test 1 de la fonction translation_bas du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe la matrice identité en paramètre.

    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

    matrice_attendue = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [1, 1, 1, 1]]

    ecrire_resultat_test("tester_translation_bas 1", matrice_attendue == logique.faire_translation_bas(matrice)[0])

    # Test 2 de la fonction translation_bas du fichier logique.py en vérifiant si la fonction retourne la matrice
    #   attendue lorsqu'on lui passe une certaine matrice remplie en paramètre.

    matrice = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]

    matrice_attendue = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [2, 2, 2, 2],
                        [2, 2, 2, 2]]

    return matrice_attendue == logique.faire_translation_bas(matrice)[0]


def ecrire_resultat_test(test, resultat):
    reussite_ou_echec = ("Échec", "Réussite")[resultat]
    print(test + "..." + reussite_ou_echec)


if __name__ == '__main__':
    ecrire_resultat_test(tester_demarrer_jeu.__name__, tester_demarrer_jeu())
    ecrire_resultat_test(tester_initialiser_nouvelle_matrice.__name__, tester_initialiser_nouvelle_matrice())
    ecrire_resultat_test(tester_ajouter_nouveau_2_ou_4_identite.__name__, tester_ajouter_nouveau_2_ou_4_identite())
    ecrire_resultat_test(tester_ajouter_nouveau_2_ou_4_remplie.__name__, tester_ajouter_nouveau_2_ou_4_remplie())
    ecrire_resultat_test(tester_get_etat_jeu_courant_victoire.__name__, tester_get_etat_jeu_courant_victoire())
    ecrire_resultat_test(tester_get_etat_jeu_courant_defaite.__name__, tester_get_etat_jeu_courant_defaite())
    ecrire_resultat_test(tester_get_etat_jeu_courant.__name__, tester_get_etat_jeu_courant())
    ecrire_resultat_test(tester_comprimer_identite.__name__, tester_comprimer_identite())
    ecrire_resultat_test(tester_comprimer_remplie.__name__, tester_comprimer_remplie())
    ecrire_resultat_test(tester_fusionner_impossible.__name__, tester_fusionner_impossible())
    ecrire_resultat_test(tester_fusionner_possible.__name__, tester_fusionner_possible())
    ecrire_resultat_test(tester_inverser_matrice_identite.__name__, tester_inverser_matrice_identite())
    ecrire_resultat_test(tester_inverser_matrice_remplie.__name__, tester_inverser_matrice_remplie())
    ecrire_resultat_test(tester_transposer_matrice_identite.__name__, tester_transposer_matrice_identite())
    ecrire_resultat_test(tester_transposer_matrice_remplie.__name__, tester_transposer_matrice_remplie())
    ecrire_resultat_test(tester_translation_gauche.__name__, tester_translation_gauche())
    ecrire_resultat_test(tester_translation_droite.__name__, tester_translation_droite())
    ecrire_resultat_test(tester_translation_bas.__name__, tester_translation_bas())
    ecrire_resultat_test(tester_translation_haut.__name__, tester_translation_haut())
