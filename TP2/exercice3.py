import math

constanteGravitationnelle = 9.81
def exercice3(hauteurInitiale, coefficientDeRebond):
    #TODO: faites vos calculs et mettez le resultat dans la variable 'nombreDeRebonds'

    V = math.sqrt(2 * constanteGravitationnelle * hauteurInitiale)
    nombreDeRebonds = 0

    while hauteurInitiale >= 0.01:
        hauteurInitiale = V**2 / (2 * constanteGravitationnelle)
        V *= coefficientDeRebond
        nombreDeRebonds += 1
    return nombreDeRebonds


if __name__ == '__main__':
    hauteurInitiale = float(input("Quelle est la hauteur initiale: "))
    coefficientDeRebond = float(input("Quel est le coefficient de rebond(entre 0 et 1 exclus [0:1[ ): "))
    print(exercice3(hauteurInitiale, coefficientDeRebond))



