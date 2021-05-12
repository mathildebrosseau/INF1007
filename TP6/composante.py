class Composante:

    def __init__(self, nom, poids):
        self.__nom = nom
        self.__poids = poids

    # NOM
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    # POIDS
    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, poids):
        self.__poids = poids