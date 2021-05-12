import json
import copy
import numpy as np
from typing import Union

from vehicule import Vehicule
from auto import Auto
from moto import Moto
from camion import Camion
# TODO - Partie 3 - Ajouter l'import pour votre classe vehicule
from La_bete import La_bete


MAX_TRACK_LENGTH = 230
TRACK_WIDTH = 15


def ensure_array_serializable(arr: Union[list, np.array]) -> list:
    return arr.tolist() if isinstance(arr, np.ndarray) else arr


def dump(vehicule: Vehicule):
    data = {}
    data["name"] = vehicule.nom
    components = [roue.nom for roue in vehicule.roues]
    components.append(vehicule.chassis.nom)
    components.append(vehicule.moteur.nom)
    data["components"] = components
    init_state = {}
    init_state["position"] = ensure_array_serializable(vehicule.position)
    data["movements"] = []
    data["movements"].append(copy.deepcopy(init_state))

    return data


def setupSimulation():
    sim = {}
    sim["simulation"] = {}
    sim["simulation"]["vehicules"] = []
    return sim


def setupTrack(trackLength: int):
    if trackLength > MAX_TRACK_LENGTH:
        print(f'Track length must be shorter than {MAX_TRACK_LENGTH} m')
        exit(1)

    track = {}
    track["length"] = trackLength
    return track


if __name__ == "__main__":

    trackLength = 200
    dt = 0.1

    data = setupSimulation()
    data["simulation"]["track"] = setupTrack(trackLength)

    # define vehicules here
    racing_vehicules = [Auto('racecar', [-1.5 * TRACK_WIDTH, 0, 0]),
                        Moto('motorcycle', [-0.5 * TRACK_WIDTH, 0, 0]),
                        Camion('truck', [0.5 * TRACK_WIDTH, 0, 0]),
                        La_bete('La bete', [1.5 * TRACK_WIDTH, 0, 0])]
    # TODO - Partie 3: Ajoutez votre vehicule a la liste! Sa position de départ doit être [1.5 * TRACK_WIDTH, 0, 0]

    for v in racing_vehicules:
        data["simulation"]["vehicules"].append(dump(v))

    winner = [False] * len(racing_vehicules)

    while (not any(winner)):
        for i, v in enumerate(racing_vehicules):
            v.accelerer(dt)

            curr_state = {}
            curr_state["position"] = ensure_array_serializable(v.position)

            data["simulation"]["vehicules"][i]["movements"].append(copy.deepcopy(curr_state))

            winner[i] = v.position[2] >= trackLength

    for i in range(len(winner)):
        if winner[i]:
            data["simulation"]["winner"] = racing_vehicules[i].nom
            data["simulation"]["winning_msg"] = racing_vehicules[i].celebrer()

    with open('out.json', 'w') as out:
        json.dump(data, out)
