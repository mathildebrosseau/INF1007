#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(c[0]**2 + c[1]**2), np.arctan2(c[1], c[0])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin()


def create_plot() -> None:
    x = np.linspace(-1,1, num=250)
    y = x**2 * np.sin(1/x**2) + x
    plt.scatter(x, y, label="points")
    plt.plot(x, y, label="line", color="red")
    plt.title("Titre du graphique")
    plt.xlabel("axe des x")
    plt.ylabel("axe des y")
    plt.xlim((-1,1))
    plt.legend()
    plt.show()


def monte_carlo(iteration: int = 500000) -> float:
    x_interieur = list()
    y_interieur = list()
    x_exterieur = list()
    y_exterieur = list()

    for i in range(iteration):
        x = np.random.random()
        y = np.random.random()
        if np.sqrt(x**2 + y**2) < 1:
            x_interieur.append(x)
            y_interieur.append(y)
        else:
            x_exterieur.append(x)
            y_exterieur.append(y)

    plt.scatter(x_interieur, y_interieur, label="points intérieurs")
    plt.scatter(x_exterieur, y_exterieur, label="points extérieurs")
    plt.xlabel("axe des x")
    plt.ylabel("axe des y")
    plt.title("Approximation de pi par méthode de Monte Carlo")
    plt.show()

    return float(len(x_interieur)) / iteration * 4


def evaluer_integrale() -> tuple:
    resultat_integrale = integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf)

    x = np.arange(-4, 4, 0.1)
    y = [integrate.quad(lambda x: np.exp(-x**2), 0, value)[0] for value in x]

    plt.plot(x, y)
    plt.xlim(-4, 4)
    plt.xlabel("axe des x")
    plt.ylabel("axe des y")
    plt.title("Intégrale de la fonction")
    plt.show()
    return resultat_integrale


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # print(linear_values())
    # print(coordinate_conversion(np.array([(0,0),(1,1), (5,8)])))
    # print(find_closest_index(np.array([1,5,10,12,8]), 10.5))
    # create_plot()
    # print(monte_carlo())
    # evaluer_integrale()
    x = np.arange(15)
    y1 = x
    y2 = x ** 2

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.scatter(x, y1)