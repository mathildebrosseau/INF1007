# TODO Fonction retournant les séquences à trier, lues à partir d'un fichier
def lire_fichier():
    chemin = "./"
    nom = "liste_de_nombres.txt"

    # Ouvrir le fichier en mode de lecture à l'aide d'un context manager
    with open(chemin + nom, 'r') as liste_nombres:
        # Lire les lignes du fichier dans un tableau de lignes
        tableau_lignes = liste_nombres.readlines()

    # Faire une tableau de tableau (contenu) contenant les séquences de nombres (transformées de string à int)
    contenu = [list(map(int, ligne.split())) for ligne in tableau_lignes]

    return contenu


# TODO Fonction écrivant les séquences triées dans un fichier spécifié
def sauvegarder_sequences_triees(chemin, nom, sequences_triees):
    # Ouvrir le fichier en mode écriture à l'aide d'un context manager
    with open(chemin + nom, 'w') as liste_sequences:

        # Pour toutes les séquences triées de nombres
        for sequence in sequences_triees:

            # Pour tous les nombres dans la séquence
            for i in range(len(sequence)):
                # Écrire le nombre suivi d'un espace
                liste_sequences.write(str(sequence[i]) + ' ')

            # Changer de ligne
            liste_sequences.write("\n")


# TODO Fonction servant à joindre les deux tableaux ensemble, avec les éléments en ordre croissant
def fusionner(gauche, droite):
    # Si le premier tableau (gauche) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le deuxième tableau (droite) comme étant le résultat
    if len(gauche) == 0:
        return droite

    # Si le deuxième tableau (droite) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le premier tableau (gauche) comme étant le résultat
    if len(droite) == 0:
        return gauche

    resultat = []
    index_gauche = index_droite = 0

    # Boucler jusqu'à ce que tous les éléments des deux tableaux (droite et gauche) soient ajoutés au tableau resultat
    while index_droite < len(droite) and index_gauche < len(gauche):

        # Les éléments doivent être triés pour être ajouté au tableau résultat.
        # Il faut donc décider de soit prendre le prochain élément du tableau droite ou soit du tableau gauche
        if gauche[index_gauche] < droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1

        # Si la fin de n'importe lequel des deux tableaux est atteinte,
        # ajouter directement tous les éléments restants de l'autre tableau au tableau résultat, et terminer la boucle.
        if index_droite == len(droite):
            resultat.extend(gauche[index_gauche:])

        elif index_gauche == len(gauche):
            resultat.extend(droite[index_droite:])

    return resultat


# TODO Fonction d'entrée du tri fusion
def tri_fusion(sequence_nombres):
    # Si le tableau (sequence_nombres) contient moins de 2 éléments, retourner directement le tableau
    # comme étant le résultat de la fonction
    if len(sequence_nombres) < 2:
        return sequence_nombres

    # Trouver l'indice de l'élément milieu du tableau
    index_milieu = len(sequence_nombres) // 2

    # Trier le tableau en séparant récursivement le tableau en 2 parties égales
    # qui seront triées et finalement fusionnées ensemble dans le résultat final
    # INDICE: Passer à chaque paramètres de la fonction fusionner la fonction tri_fusion
    # avec une partie (gauche ou droite) de la séquence de nombre

    gauche = tri_fusion(sequence_nombres[:index_milieu])
    droite = tri_fusion(sequence_nombres[index_milieu:])

    return fusionner(gauche, droite)


# NE PAS TOUCHER, C'EST UNE FONCTION DE TEST POUR VOUS AIDER À VALIDER VOS RÉSULTATS
def tester_resultat(sequences_a_trier, sequences_triees):
    bon_resultats = 0
    for indice in range(len(sequences_triees)):
        test = sequences_a_trier[indice][:]
        test.sort()  # C'est facile le Python !
        if test == sequences_triees[indice]:
            bon_resultats += 1
    return bon_resultats == len(sequences_a_trier)


# NE PAS TOUCHER AU MAIN
if __name__ == '__main__':
    sequences_a_trier = lire_fichier()

    print("Les séquences à trier sont: ")
    print(sequences_a_trier)

    sequences_triees = []

    for sequence in sequences_a_trier:
        sequences_triees.append(tri_fusion(sequence))

    print("Les séquences triées sont: ")
    print(sequences_triees)

    est_bon = tester_resultat(sequences_a_trier, sequences_triees)

    if est_bon:
        print("Bravo, le tri est bon !")
    else:
        print("Oups, le tri ne fonctionne pas")

    sauvegarder_sequences_triees("./", "resultats.txt", sequences_triees)
