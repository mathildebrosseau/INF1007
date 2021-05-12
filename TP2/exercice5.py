def afficherMatrice(M):
    for i in range(len(M)):
        ligne = ['{}'.format(x) for x in M[i]]
        print(ligne, '\t')
    print('\n')


def matriceZero(nbLignes, nbColonnes):
    # TODO: Remplir la matrice A de 0, selon les dimensions données

    A = []
    lignes = []
    l = 0
    for c in range(nbColonnes):
        lignes.append(0)
    while l < nbLignes:
        A.append(lignes)
        l += 1
    return A


def multiplierMatrices(A, B):

    #TODO: Si les matrices ne peuvent pas etre multipliées, affecter à C une matrice nulle [nbLignesA x nbColonnesB]

    if len(A[0]) != len(B):
        C = matriceZero(len(A), len(B[0]))

    #TODO: Sinon faire la multiplication et mettre dans C le résultat

    else:
        C = list()
        for i in range(len(A)): # ligne A
            ligne = list(list())
            for j in range(len(B[0])): # colonne B
                element = list()
                for k in range(len(A[0])): #item
                    element.append(A[i][k] * B[k][j])
                ligne.append(sum(element))
                element = list()
            C.append(ligne)
    return C


if __name__ == '__main__':
    A = ([[1, 2], [1, 5]])
    B = ([[1, 2], [1, 6], [3, 8]])
    C = ([[1], [6]])
    afficherMatrice(multiplierMatrices(A, B))
    afficherMatrice(multiplierMatrices(B, A))
    afficherMatrice(multiplierMatrices(A, C))
    afficherMatrice(multiplierMatrices(B, C))