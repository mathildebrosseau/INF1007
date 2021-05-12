import inspect

# region constantes
#        Si nécessaire ajoutez vos constantes ici afin de ne pas utiliser de chiffres magiques dans le code

TAILLE_MAX = 32
AUCUN = -1  # Valeur utilisee lorsqu'il n'y a aucun chemin, aucun predecesseur, etc. Pour utiliser une constante unique,


# il faut qu'elle ait une valeur invalide a la fois comme distance et comme numero de noeud.

# endregion

# region "Fonctions d'aide, Rien à modifier ici!"

# Indique si un element est dans l'ensemble.
def est_dans(ensemble, element):
    for elem in ensemble:
        if elem == element:
            return True

    return False


def comparer_tableaux(tableau_a, tableau_b):
    print(
        "Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[
            len(tableau_a) == len(tableau_b)])

    est_pareil = True
    for i in range(len(tableau_a)):
        if tableau_a[i] != tableau_b[i]:
            est_pareil = False

    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[est_pareil])


def afficher_tableau(nom_tableau, tableau):
    print("Affichage tableau: " + nom_tableau)

    for elem in tableau:
        print("{0:4}".format(elem), end=" ")
    print()


def afficher_matrice(nom_matrice, matrice):
    print("Affichage du contenu de la matrice: " + nom_matrice)
    for line in matrice:
        for elem in line:
            print("{0:4}".format(elem), end=" ")
        print()


# endregion

# region "Fonction à compléter"

# 1- Lit la matrice poids (distances entre les villes) a partir d'un fichier. Retourne le contenu de la matrice lue
def lire_poids(nom_fichier):
    # TODO: Lire le fichier et verifier que la lecture n'a pas fait d'erreur;
    #  La matrice retournée n'a pas d'importance s'il y a eu une erreur.
    # TODO : Ajouter une couche de vérification des données en entrée. Vérifier que toutes les lignes de la matrice
    #  ont la même longeur et qu'il n'y a pas de valeurs incohérentes (autres que des entier positifs ou -1). Si la
    #  matrice est non conforme, utilisez la fonction exit() pour terminer le programme après avoir notifié
    #  l'utilisateur.

    with open("./" + nom_fichier, "r") as f:
        contenu = f.readlines()
        if contenu is None:
            print("Erreur de lecture du fichier.")
            exit()

    matrice_liste = [list(ligne.split()) for ligne in contenu]

    for lignes in matrice_liste:
        if len(lignes) != len(matrice_liste[0]):
            print("Erreur : Les lignes de la matrice n'ont pas toutes la même longueur.")
            exit()
        for elem in lignes:
            if not elem.isdigit() and '-' not in elem:
                print("Erreur : Valeurs non entières dans la matrice.")
                exit()
            elif int(elem) < AUCUN:
                print("Erreur : Valeurs inférieures à -1 dans la matrice.")
                exit()

    matrice_lue = [[int(element) for element in ligne] for ligne in matrice_liste]

    return matrice_lue


# 2- Initialise les structures pour appliquer l'algorithme de Dijkstra.
def initialiser(noeud_initial, n_noeuds):
    # TODO: Initialiser et retourne les tableaux distances, predecesseurs et noeuds.
    #       Tel qu'indique dans l'enonce:
    #       Les distances sont initialisees a -1 sauf pour le noeud initial qui est a 0.
    # TODO: - Les predecesseurs sont initialisés a -1.
    # TODO: - Noeuds doit etre initialise pour contenir toutes les valeurs de 0 a nNoeuds-1.
    distances, predecesseurs, noeuds = [], [], []

    for i in range(n_noeuds):
        if i == noeud_initial:
            distances.append(0)
        else:
            distances.append(AUCUN)
        predecesseurs.append(AUCUN)
        noeuds.append(i)

    return distances, predecesseurs, noeuds


# 3 - Trouve et retourne l'élément le plus proche de l'élément initial, selon le tableau actuel des distances.
def trouver_element_plus_proche(distances, noeuds):
    # TODO: Pour chaque element de la liste de noeuds, vérifier lequel a la plus petite valeur dans les distances et
    #  retourner l'indice de cet élément. distance_min = AUCUN
    distance_min = AUCUN
    premier_elem_different_aucun = False
    index_noeud = 0

    for elem in noeuds:
        if (not premier_elem_different_aucun and distances[elem] != AUCUN) or (
                distances[elem] < distance_min and distances[elem] != AUCUN):
            premier_elem_different_aucun = True
            distance_min = distances[elem]
            index_noeud = elem

    return index_noeud


# 4 - Fait la mise à jour des distances et des predecesseurs si on permet de passer par par_noeud. Cette fonction ne
#     retourne rien elle modifie les paramètres référencés directement.
def mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, par_noeud):
    # TODO: Pour chaque element de l'ensemble noeuds, vérifier si passer par_noeud pour y aller réduit la distance par
    #  rapport à celle actuellement dans le tableau distances; si c'est le cas, modifie la distance pour cette
    #  nouvelle valeur et change le prédécesseur de cet élément comme étant par_noeud.  Attention aux valeurs -1 dans
    #  les poids et les distances.  Voir la description dans l'énoncé pour plus de détails.

    for elem in noeuds:

        def nouvelle_distance(elem=elem, poids=poids, par_noeud=par_noeud, distances=distances):
            distances[elem] = poids[par_noeud][elem] + distances[par_noeud]
            predecesseurs[elem] = par_noeud

        if poids[par_noeud][elem] > 0:
            if distances[elem] == AUCUN:
                nouvelle_distance()
            elif distances[elem] != AUCUN:
                if distances[par_noeud] + poids[par_noeud][elem] < distances[elem]:
                    nouvelle_distance()


# 5- Affiche le plus court chemin, soit la liste des noeuds par lesquels il faut passer pour se rendre de la source a
# la destination. Suppose que l'algorithme a deja ete applique pour calculer les tableaux de distances et
# predecesseurs. Cette fonction ne retourne rien.
def afficher_chemin_plus_proche(distances, predecesseurs, noeud_source, noeud_destination):
    # TODO: Afficher le chemin similairement à l'exemple de sortie suivant:
    #       Le chemin le plus court de 4 vers 7 est:
    #       4 -> 2 -> 5 -> 7
    #       de distance 10
    passage = []
    destination_atteinte = False
    noeud_trajet = noeud_destination

    while not destination_atteinte:
        if noeud_trajet == noeud_source:
            destination_atteinte = True
        passage.append(noeud_trajet)
        noeud_trajet = predecesseurs[noeud_trajet]

    passage.reverse()
    passage_string = str(passage[0])
    for i in range(1, len(passage)):
        passage_string += " -> " + str(passage[i])
    print(f"Le chemin le plus court de {noeud_source} vers {noeud_destination} est:\n"
          f"{passage_string}\n"
          f"de distance {distances[noeud_destination]}.")


# endregion

# region "Fonctions de test - Rien à modifier pour vous ici!"

BON_SI_VRAI = ["ERREUR", "BON"]


def tester_trouver_element_plus_proche():
    print("Test de trouve_element_plus_proche:")

    distances = [7, 2, -1, 5, 6]
    noeuds = [0, 1, 2, 3, 4]

    plus_proche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plus_proche == 1])

    noeuds = [0, 2, 3, 4]
    plus_proche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plus_proche == 3])


def tester_mettre_a_jour_distances():
    print("Test de mettre_a_jour_distances")
    poids = [[0, 4, 2, -1], [-1, 0, -1, 2], [1, 1, 0, 6], [-1, -1, -1, 0]]
    distances = [0, -1, -1, -1]
    predecesseurs = [-1, -1, -1, -1]

    noeuds = [0, 1, 2, 3]
    distances_attendues = [0, 4, 2, -1]
    predecesseurs_attendus = [-1, 0, 0, -1]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 0)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : Deux sous tests")
    comparer_tableaux(distances, distances_attendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : Deux sous tests")
    comparer_tableaux(predecesseurs, predecesseurs_attendus)
    distances = distances_attendues
    predecesseurs = predecesseurs_attendus

    noeuds = [1, 2, 3]
    distances_attendues = [0, 3, 2, 8]
    predecesseurs_attendus = [-1, 2, 0, 2]

    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparer_tableaux(distances, distances_attendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparer_tableaux(predecesseurs, predecesseurs_attendus)
    distances = distances_attendues
    predecesseurs = predecesseurs_attendus

    # Un etat impossible dans l'algorithme, mais ceci permet de verifier si mettreAJourDistances verifie seulement
    # les elements de l'ensemble noeuds.
    distances[0] = 10
    noeuds = [1, 2, 3]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[distances[0] == 10])


# endregion

if __name__ == '__main__':
    tester_trouver_element_plus_proche()
    tester_mettre_a_jour_distances()
    print("Fin des tests")

    # TODO: Lire la matrice des poids à partir du fichier poids.txt et l'afficher dans le terminal.
    matrice_poids = lire_poids("poids.txt")
    afficher_matrice("Poids", matrice_poids)

    # TODO: Demander a l'utilsateur l'indice du noeud source, avec validation de l'entree.
    noeud_source = input("Quel est l'indice du noeud de source ? ")

    if noeud_source.isdigit():
        noeud_source = int(noeud_source)
    else:
        print("Cet indice n'est pas conforme. L'indice doit être un entier.")
        exit()
    if noeud_source >= len(matrice_poids):
        print("Cet indice est trop grand et ne fait pas parti de la matrice.")
        exit()

    # TODO: Intialiser les tableaux de distances, predecesseurs et noeuds.
    distances, predecesseurs, noeuds = initialiser(noeud_source, len(matrice_poids))

    # TODO: Tant qu'il reste des éléments dans l'ensemble noeuds:
    while len(noeuds) > 0:
        # 	TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.
        index_elem_plus_proche = trouver_element_plus_proche(distances, noeuds)

        #   TODO: Si tous les chemins possibles ont été évalués (aucun prochain element a visiter), sortir de la boucle
        if len(noeuds) == 0:
            break

        # 	TODO: Mettre à jour les distances en vérifiant si c'est plus court de passer par le noeud le plus proche.
        mettre_a_jour_distances(matrice_poids, distances, predecesseurs, noeuds, index_elem_plus_proche)

        # 	TODO: Retirer cet element le plus proche de l'ensemble noeuds.
        noeuds.remove(index_elem_plus_proche)

    # TODO: Afficher le contenu de distances.
    afficher_tableau('Distances', distances)

    # TODO: Afficher le contenu de predecesseurs.
    afficher_tableau('Predecesseurs', predecesseurs)

    # TODO: Demander a l'utilisateur un noeud destination different de la source, avec validation de l'entree (indiquer
    #       l'intervalle de sommet possible et si la valeur entrée est hors de celui-ci).
    noeud_destination = input("Quel est l'indice du noeud de destination ? ")

    if noeud_destination.isdigit():
        noeud_destination = int(noeud_destination)
    else:
        print("Cet indice n'est pas conforme. L'indice doit être un entier.")
        exit()
    if noeud_destination >= len(matrice_poids):
        print("Cet indice est trop grand et ne fait pas parti de la matrice.")
        exit()

    # TODO: Valider si un chemin entre les deux sommet existe
    if distances[noeud_destination] <= AUCUN:
        print("Il n'y a aucun trajet entre ces deux noeuds")
        exit()

    # TODO: Afficher la solution, soit le plus court chemin allant de la source vers la destination.
    afficher_chemin_plus_proche(distances, predecesseurs, noeud_source, noeud_destination)
