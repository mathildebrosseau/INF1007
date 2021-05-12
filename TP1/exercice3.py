import math


def calculerNombreChiffres(nombre):

    # TODO: Déterminer le nombre de chiffres de "nombre" et mettre la valeur dans "nombreDeChiffres"
    nombreDeChiffres = math.floor(math.log10(nombre)) + 1

    # TODO: Afficher la valeur de "nombreDeChiffres"
    print(nombreDeChiffres)
    return nombreDeChiffres


if __name__ == '__main__':
    nombre = int(input('veuillez indiquer un nombre strictement postif: '))
    calculerNombreChiffres(nombre)