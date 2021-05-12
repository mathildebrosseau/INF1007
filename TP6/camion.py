from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class Camion(Vehicule):
    def __init__(self, nom, position_dep):
        super().__init__(nom, position_dep, self.roues, self.moteur, self.chassis)

    @property
    def roues(self):
        roues = [Roue(roues_dict['camion']['nom'], roues_dict['camion']['poids'],
                      roues_dict['camion']['coefficient_friction'], roues_dict['camion']['poids_supporte']),
                 Roue(roues_dict['camion']['nom'], roues_dict['camion']['poids'],
                      roues_dict['camion']['coefficient_friction'], roues_dict['camion']['poids_supporte']),
                 Roue(roues_dict['camion']['nom'], roues_dict['camion']['poids'],
                      roues_dict['camion']['coefficient_friction'], roues_dict['camion']['poids_supporte']),
                 Roue(roues_dict['camion']['nom'], roues_dict['camion']['poids'],
                      roues_dict['camion']['coefficient_friction'], roues_dict['camion']['poids_supporte']),
                 Roue(roues_dict['camion']['nom'], roues_dict['camion']['poids'],
                      roues_dict['camion']['coefficient_friction'], roues_dict['camion']['poids_supporte']),
                 Roue(roues_dict['camion']['nom'], roues_dict['camion']['poids'],
                      roues_dict['camion']['coefficient_friction'], roues_dict['camion']['poids_supporte'])]
        return roues

    @property
    def chassis(self):
        chassis = Chassis(chassis_dict['camion']['nom'], chassis_dict['camion']['poids'],
                          chassis_dict['camion']['aire_frontale'], chassis_dict['camion']['coefficient_trainee'])
        return chassis

    @property
    def moteur(self):
        moteur = Moteur(moteurs_dict['camion']['nom'], moteurs_dict['camion']['poids'],
                        moteurs_dict['camion']['acceleration'])
        return moteur

    def celebrer(self):
        return "le gros a gagné"
