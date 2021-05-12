def exercice1(tableau):
    #TODO: trier le tableau

    for i in range(len(tableau)):
        min = tableau[i]
        for j in range(i, len(tableau)):
            if tableau[j] <= min:
                min = tableau[j]
                index_min = i
            if tableau[j] == min:
                ancienne_valeur = tableau[i]
                tableau[i] = min
                tableau[j] = ancienne_valeur
    return tableau


if __name__ == '__main__':
    #Voici un exemple de tableau à trier:
    tableau_a_trier = [2,4,6,4,6,7,8,9,7,5,4,3]

    resultat = exercice1(tableau_a_trier)
    print(resultat)