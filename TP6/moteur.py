from composante import Composante


# PARTIE 1 - TODO
class Moteur(Composante):
    def __init__(self, nom, poids, acceleration):
        super().__init__(nom, poids)
        self.__acceleration = acceleration

    @property
    def acceleration(self):
        return self.__acceleration
