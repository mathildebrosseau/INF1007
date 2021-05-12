from os import listdir
from os.path import isfile, join
import sys
from typing import Union
import numpy as np

from composante import Composante
from moteur import Moteur
from chassis import Chassis
from roue import Roue

from vehicule import Vehicule
from moto import Moto
from auto import Auto
from camion import Camion

# Roulez ce fichier pour tester votre code :)

# region test_composantes


def test_creer_composante():
    result = True
    try:
        nom = "maComposante"
        poids = 10
        composante = Composante(nom=nom, poids=poids)
    except:
        return False

    result &= composante.nom == nom
    result &= composante.poids == poids

    expected_dict = {'_Composante__nom': 'maComposante',
                     '_Composante__poids': 10}
    result &= composante.__dict__ == expected_dict

    return result

def test_creer_moteur():
    result = True
    try:
        nom = "monMoteur"
        poids = 10
        acceleration = 2.5
        moteur = Moteur(nom=nom, poids=poids, acceleration=acceleration)
    except:
        return False

    result &= moteur.nom == nom
    result &= moteur.poids == poids
    result &= moteur.acceleration == acceleration

    expected_dict = {'_Moteur__acceleration': 2.5,
                     '_Composante__nom': 'monMoteur', '_Composante__poids': 10}
    result &= moteur.__dict__ == expected_dict

    return result


def test_creer_chassis():
    result = True
    try:
        nom = "monChassis"
        poids = 10
        aire_frontale = 2.4
        coefficient_trainee = 0.6
        chassis = Chassis(nom=nom, poids=poids, aire_frontale=aire_frontale,
                          coefficient_trainee=coefficient_trainee)
    except:
        return False

    result &= chassis.nom == nom
    result &= chassis.poids == poids
    result &= chassis.aire_frontale == aire_frontale
    result &= chassis.coefficient_trainee == coefficient_trainee

    expected_dict = {'_Chassis__aire_frontale': 2.4, '_Chassis__coefficient_trainee': 0.6,
                     '_Composante__nom': 'monChassis', '_Composante__poids': 10}
    result &= chassis.__dict__ == expected_dict

    return result


def test_creer_roue():
    result = True
    try:
        nom = "maRoue"
        poids = 10
        coefficient_friction = 0.4
        poids_supporte = 10
        roue = Roue(nom=nom, poids=poids, coefficient_friction=coefficient_friction,
                    poids_supporte=poids_supporte)
    except:
        return False

    result &= roue.nom == nom
    result &= roue.poids == poids
    result &= roue.coefficient_friction == coefficient_friction
    result &= roue.poids_supporte == poids_supporte

    expected_dict = {'_Roue__poids_supporte': 10, '_Roue__coefficient_friction': 0.4,
                     '_Composante__nom': 'maRoue', '_Composante__poids': 10}
    result &= roue.__dict__ == expected_dict

    return result
# endregion

# region test_vehicules
def compare_arrays(arr1: Union[list, np.array], arr2: Union[list, np.array]):
    arr1 = arr1.tolist() if isinstance(arr1, np.ndarray) else arr1
    arr2 = arr2.tolist() if isinstance(arr2, np.ndarray) else arr2
    return arr1 == arr2


def test_creer_vehicule():
    result = True
    try:
        nom_vehicule = "monVehicule"
        position_dep = [45, -2, 57]

        nom_roue = "maRoue"
        poids_roue = 10
        coefficient_friction = 0.4
        poids_supporte = 10
        roues = [Roue(nom=nom_roue, poids=poids_roue, coefficient_friction=coefficient_friction,
                      poids_supporte=poids_supporte),
                 Roue(nom=nom_roue, poids=2*poids_roue, coefficient_friction=2*coefficient_friction,
                      poids_supporte=2*poids_supporte)]

        nom_moteur = "monMoteur"
        poids_moteur = 10
        acceleration = 2.5
        moteur = Moteur(nom=nom_moteur, poids=poids_moteur,
                        acceleration=acceleration)

        nom_chassis = "monChassis"
        poids_chassis = 10
        aire_frontale = 2.4
        coefficient_trainee = 0.6
        chassis = Chassis(nom=nom_chassis, poids=poids_chassis, aire_frontale=aire_frontale,
                          coefficient_trainee=coefficient_trainee)

        vehicule = Vehicule(nom=nom_vehicule, position_dep=position_dep,
                            roues=roues, moteur=moteur, chassis=chassis)

        result &= vehicule.celebrer() == None

        result &= vehicule.position == position_dep
        result &= compare_arrays(vehicule.vitesse, [0, 0, 0])
        print(result)
        result &= vehicule.trainee == 0.0
        result &= vehicule.friction == 0.0
        dt = 1
        vehicule.accelerer(temps_ecoule=dt)
        result &= compare_arrays(vehicule.vitesse, [0, 0, 2.5])
        result &= compare_arrays(vehicule.position, [45, -2, 59.5])
        result &= vehicule.trainee == 5.4
        result &= vehicule.friction == 3.0

    except:
        return False

    result &= vehicule.nom == nom_vehicule
    result &= vehicule.poids == 50
    result &= vehicule.traction == 125.0
    result &= vehicule.roues == roues
    result &= vehicule.moteur == moteur
    result &= vehicule.chassis == chassis
    result &= vehicule.acceleration == 2.332

    expected_dict_keys = ['_Vehicule__nom', '_Vehicule__vitesse', '_Vehicule__position',
                          '_Vehicule__roues', '_Vehicule__moteur', '_Vehicule__chassis']
    result &= list(vehicule.__dict__.keys()) == expected_dict_keys

    return result


def test_creer_moto():
    result = True
    try:
        nom_moto = "maMoto"
        position_dep = [45, -3, 57]
        moto = Moto(nom=nom_moto, position_dep=position_dep)
        result &= isinstance(moto.celebrer(), str)

    except:
        return False

    result &= moto.nom == nom_moto
    result &= compare_arrays(moto.vitesse, [0, 0, 0])
    result &= compare_arrays(moto.position, position_dep)
    result &= moto.poids == 202
    result &= moto.traction == 1878.6000000000001
    result &= moto.trainee == 0.0
    result &= moto.friction == 0.0

    expected_dict_keys = ['_Vehicule__nom', '_Vehicule__vitesse', '_Vehicule__position',
                          '_Vehicule__roues', '_Vehicule__moteur', '_Vehicule__chassis']
    result &= list(moto.__dict__.keys()) == expected_dict_keys
    expected_n_wheels = 2
    result &= len(moto.__dict__.get(
        '_Vehicule__roues', [])) == expected_n_wheels

    return result


def test_creer_auto():
    result = True
    try:
        nom_auto = "maVoiture"
        position_dep = [52, -3, 57]
        auto = Auto(nom=nom_auto, position_dep=position_dep)
        result &= isinstance(auto.celebrer(), str)

    except:
        return False

    result &= auto.nom == nom_auto
    result &= compare_arrays(auto.vitesse, [0, 0, 0])
    result &= compare_arrays(auto.position, position_dep)
    result &= auto.poids == 1421
    result &= auto.traction == 11368
    result &= auto.trainee == 0.0
    result &= auto.friction == 0.0

    expected_dict_keys = ['_Vehicule__nom', '_Vehicule__vitesse', '_Vehicule__position',
                          '_Vehicule__roues', '_Vehicule__moteur', '_Vehicule__chassis']
    result &= list(auto.__dict__.keys()) == expected_dict_keys
    expected_n_wheels = 4
    result &= len(auto.__dict__.get(
        '_Vehicule__roues', [])) == expected_n_wheels

    return result


def test_creer_camion():
    result = True
    try:
        nom_camion = "monCamion"
        position_dep = [52, -3, 60]
        camion = Camion(nom=nom_camion, position_dep=position_dep)
        result &= isinstance(camion.celebrer(), str)

    except:
        return False

    result &= camion.nom == nom_camion
    result &= compare_arrays(camion.vitesse, [0, 0, 0])
    result &= compare_arrays(camion.position, position_dep)
    result &= camion.poids == 9368
    result &= camion.traction == 37472
    result &= camion.trainee == 0.0
    result &= camion.friction == 0.0

    expected_dict_keys = ['_Vehicule__nom', '_Vehicule__vitesse', '_Vehicule__position',
                          '_Vehicule__roues', '_Vehicule__moteur', '_Vehicule__chassis']
    result &= list(camion.__dict__.keys()) == expected_dict_keys
    expected_n_wheels = 6
    result &= len(camion.__dict__.get(
        '_Vehicule__roues', [])) == expected_n_wheels

    return result

# endregion

# region custom_vehicule


def get_module_name():
    default_files = ['.gitignore', 'auto.py', 'camion.py', 'chassis.py', 'composante.py', 'dictionnaire_modeles.py',
                     'main.py', 'moteur.py', 'moto.py', 'README.md', 'roue.py', 'tests.py', 'vehicule.py', 'out.json']
    all_files = [f for f in listdir('./') if isfile(join('./', f))]
    extra_files = [
        f for f in all_files if f not in default_files and f.endswith('.py')]
    if len(extra_files) > 1:
        return None
    extra_class_name = extra_files[0].split('.')[0]
    return extra_class_name


def test_creer_custom_vehicule():
    module_name = get_module_name()
    if module_name is None or len(module_name) == 0:
        print("There was an error getting the module name! Remove all extra files from directory, and make sure youre running the script from the right place!")
        return False

    result = True
    try:
        class_name = module_name.capitalize()
        customVehiculeModule = __import__(module_name)
        Vehicule = getattr(customVehiculeModule, class_name)

        nom_vehicule = "monVehicule"
        position_dep = [-10, -3, 60]
        vehicule = Vehicule(nom=nom_vehicule, position_dep=position_dep)
        result &= isinstance(vehicule.celebrer(), str)

    except:
        return False

    result &= vehicule.nom == nom_vehicule
    result &= compare_arrays(vehicule.vitesse, [0, 0, 0])
    result &= compare_arrays(vehicule.position, position_dep)
    result &= vehicule.trainee == 0.0
    result &= vehicule.friction == 0.0

    expected_dict_keys = ['_Vehicule__nom', '_Vehicule__vitesse', '_Vehicule__position',
                          '_Vehicule__roues', '_Vehicule__moteur', '_Vehicule__chassis']
    result &= list(vehicule.__dict__.keys()) == expected_dict_keys
    expected_n_wheels = 1
    result &= len(vehicule.__dict__.get(
        '_Vehicule__roues', [])) >= expected_n_wheels

    return result

# endregion


def main():
    res_composante = test_creer_composante()
    res_moteur = test_creer_moteur()
    res_chassis = test_creer_chassis()
    res_roue = test_creer_roue()

    print("----- TESTS PARTIE 1 -----")
    print("TESTS COMPOSANTES:")
    print("1 pt     - Création de composante:",
          "PASS" if res_composante else "FAIL")
    print("1.33 pts - Création de moteur:    ",
          "PASS" if res_moteur else "FAIL")
    print("1.33 pts - Création de chassis:   ",
          "PASS" if res_chassis else "FAIL")
    print("1.33 pts - Création de roue:      ", "PASS" if res_roue else "FAIL")
    total_points_p1 = round(int(res_composante) * 1 + int(res_moteur)
                            * 1.333 + int(res_chassis) * 1.333 + int(res_roue) * 1.333, 2)
    print(f"SCORE PARTIE 1: {total_points_p1} / 5.0")
    print('\n')

    res_vehicule = test_creer_vehicule()
    res_moto = test_creer_moto()
    res_auto = test_creer_auto()
    res_camion = test_creer_camion()

    print("----- TESTS PARTIE 2 -----")
    print("TESTS VEHICULES:")
    print("2 pts    - Création de vehicule:  ",
          "PASS" if res_vehicule else "FAIL")
    print("1 pt     - Création de moto:      ", "PASS" if res_moto else "FAIL")
    print("1 pt     - Création d'auto:       ", "PASS" if res_auto else "FAIL")
    print("1 pt     - Création de camion:    ",
          "PASS" if res_camion else "FAIL")
    total_points_p2 = int(res_vehicule) * 2 + int(res_moto) * \
        1 + int(res_auto) * 1 + int(res_camion) * 1
    print(f"SCORE PARTIE 2: {total_points_p2:.1f} / 5.0")
    print('\n')

    res_custom_vehicule = test_creer_custom_vehicule()
    print("----- TESTS PARTIE 3 -----")
    print("TEST VEHICULE CUSTOM")
    print("2 pts - Création d'un nouveau vehicule: ",
          "PASS" if res_custom_vehicule else "FAIL")
    total_points_p3 = int(res_custom_vehicule) * 2
    print(f"SCORE PARTIE 3: {total_points_p3:.1f} / 2.0")
    print('\n')

    print(
        f"TOTAL : {total_points_p1 + total_points_p2 + total_points_p3} / 12.0")


if __name__ == "__main__":
    # I KNOW its horrible sorry for the hack lol
    stdoutOrigin = sys.stdout
    sys.stdout = open("logs.txt", "w", encoding='utf-8')
    main()
    sys.stdout.close()
    sys.stdout = stdoutOrigin
    main()
