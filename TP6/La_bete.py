from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class La_bete(Vehicule):
    def __init__(self, nom, position_dep):
        super().__init__(nom, position_dep, self.roues, self.moteur, self.chassis)

    @property
    def roues(self):
        roues = [Roue(roues_dict['la_bete']['nom'], roues_dict['la_bete']['poids'],
                      roues_dict['la_bete']['coefficient_friction'], roues_dict['la_bete']['poids_supporte'])]
        return roues

    @property
    def chassis(self):
        chassis = Chassis(chassis_dict['la_bete']['nom'], chassis_dict['la_bete']['poids'],
                          chassis_dict['la_bete']['aire_frontale'], chassis_dict['la_bete']['coefficient_trainee'])
        return chassis

    @property
    def moteur(self):
        moteur = Moteur(moteurs_dict['la_bete']['nom'], moteurs_dict['la_bete']['poids'],
                        moteurs_dict['la_bete']['acceleration'])
        return moteur

    def celebrer(self):
        return "la bête fait grrrr"
