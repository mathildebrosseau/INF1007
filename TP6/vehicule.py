from chassis import Chassis
from moteur import Moteur
from roue import Roue
import numpy as np

AIR_DENSITY = 1.2


class Vehicule:
    # PARTIE 2 - TODO
    def __init__(self, nom, position_dep, roues, moteur, chassis):
        self.__nom = nom
        self.__vitesse = [0.0, 0.0, 0.0]
        self.__position = position_dep
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis

    # NOM
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    # VITESSE
    @property
    def vitesse(self):
        return self.__vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self.__vitesse = vitesse

    # POSITION
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    # ROUES
    @property
    def roues(self):
        return self.__roues

    @roues.setter
    def roues(self, roues):
        self.__roues = roues

    # MOTEUR
    @property
    def moteur(self):
        return self.__moteur

    @moteur.setter
    def moteur(self, moteur):
        self.__moteur = moteur

    # CHASSIS
    @property
    def chassis(self):
        return self.__chassis

    @chassis.setter
    def chassis(self, chassis):
        self.__chassis = chassis

    # POIDS
    @property
    def poids(self):
        poids_roues = 0
        for i in range(len(self.roues)):
            poids_roues += self.roues[i].poids
        poids = poids_roues + self.chassis.poids + self.moteur.poids
        return poids

    # TRAINEE
    @property
    def trainee(self):
        trainee = 0.5 * self.chassis.coefficient_trainee * self.chassis.aire_frontale * AIR_DENSITY * self.vitesse[2]**2
        return trainee

    # TRACTION
    @property
    def traction(self):
        traction = self.poids * self.moteur.acceleration
        return traction

    # FRICTION
    @property
    def friction(self):
        friction = 0
        for i in range(len(self.roues)):
            friction += self.roues[i].coefficient_friction * self.vitesse[2]
        return friction

    # ACCELERATION
    @property
    def acceleration(self):
        acceleration = (self.traction - self.trainee - self.friction) / self.poids
        return acceleration

    # FONCTION ACCELERER
    def accelerer(self, temps_ecoule):
        force_totale = self.traction - self.friction - self.trainee
        acceleration = force_totale / self.poids
        self.vitesse[2] += acceleration * temps_ecoule
        self.position[2] += self.vitesse[2] * temps_ecoule

    # FONCTION CELEBRER
    def celebrer(self):
        return None
