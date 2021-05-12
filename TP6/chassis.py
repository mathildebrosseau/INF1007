from composante import Composante


# PARTIE 1 - TODO
class Chassis(Composante):
    def __init__(self, nom, poids, aire_frontale, coefficient_trainee):
        super().__init__(nom, poids)
        self.__aire_frontale = aire_frontale
        self.__coefficient_trainee = coefficient_trainee

    @property
    def aire_frontale(self):
        return self.__aire_frontale

    @property
    def coefficient_trainee(self):
        return self.__coefficient_trainee
