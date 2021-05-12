from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class Auto(Vehicule):
    def __init__(self, nom, position_dep):
        super().__init__(nom, position_dep, self.roues, self.moteur, self.chassis)

    @property
    def roues(self):
        roues = [Roue(roues_dict['auto']['nom'], roues_dict['auto']['poids'],
                      roues_dict['auto']['coefficient_friction'], roues_dict['auto']['poids_supporte']),
                 Roue(roues_dict['auto']['nom'], roues_dict['auto']['poids'],
                      roues_dict['auto']['coefficient_friction'], roues_dict['auto']['poids_supporte']),
                 Roue(roues_dict['auto']['nom'], roues_dict['auto']['poids'],
                      roues_dict['auto']['coefficient_friction'], roues_dict['auto']['poids_supporte']),
                 Roue(roues_dict['auto']['nom'], roues_dict['auto']['poids'],
                      roues_dict['auto']['coefficient_friction'], roues_dict['auto']['poids_supporte'])]
        return roues

    @property
    def chassis(self):
        chassis = Chassis(chassis_dict['auto']['nom'], chassis_dict['auto']['poids'],
                          chassis_dict['auto']['aire_frontale'], chassis_dict['auto']['coefficient_trainee'])
        return chassis

    @property
    def moteur(self):
        moteur = Moteur(moteurs_dict['auto']['nom'], moteurs_dict['auto']['poids'],
                        moteurs_dict['auto']['acceleration'])
        return moteur

    def celebrer(self):
        return "i vroom-vroomed faster than you hehe"
