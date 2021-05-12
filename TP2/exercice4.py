import math
from random import random

def exercice4():
    approximationPi = 0.0
    Cercle, Carre, nIterations = 0, 0, 0
    #TODO: Approximer PI selon l'enonce.

    while abs(math.pi-approximationPi) > 0.0001:
        nIterations += 1
        x = random() * 2 - 1
        y = random() * 2 - 1
        if x**2 + y**2 < 1:
            Cercle += 1
        Carre = nIterations
        approximationPi = (Cercle / Carre) * 4
    return (approximationPi, nIterations)


if __name__ == '__main__':
    tuple = exercice4()
    print("Approximation de pi = {:.4f}, en {} iterations".format(tuple[0], tuple[1]))