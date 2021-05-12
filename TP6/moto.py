from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class Moto(Vehicule):
    def __init__(self, nom, position_dep):
        super().__init__(nom, position_dep, self.roues, self.moteur, self.chassis)

    @property
    def roues(self):
        roues = [
            Roue(roues_dict['moto']['nom'], roues_dict['moto']['poids'], roues_dict['moto']['coefficient_friction'],
                 roues_dict['moto']['poids_supporte']),
            Roue(roues_dict['moto']['nom'], roues_dict['moto']['poids'], roues_dict['moto']['coefficient_friction'],
                 roues_dict['moto']['poids_supporte'])]
        return roues

    @property
    def chassis(self):
        chassis = Chassis(chassis_dict['moto']['nom'], chassis_dict['moto']['poids'],
                          chassis_dict['moto']['aire_frontale'], chassis_dict['moto']['coefficient_trainee'])
        return chassis

    @property
    def moteur(self):
        moteur = Moteur(moteurs_dict['moto']['nom'], moteurs_dict['moto']['poids'],
                        moteurs_dict['moto']['acceleration'])
        return moteur

    def celebrer(self):
        return "moto a gagné yeah!"
