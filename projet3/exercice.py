import csv
import math

# Variable globale
g = 9.80665  # m/s^2


def proprietes_eau(temperature):
    # Extraction de la base de données
    with open('./data/data.csv') as data_file:
        data_reader = csv.reader(data_file, delimiter=',')

        compteur_ligne = 0
        liste_temperature = list()
        liste_rho = list()
        liste_mu = list()

        for row in data_reader:
            if compteur_ligne > 0:
                liste_temperature.append(float(row[0]))
                liste_rho.append(float(row[1]))
                liste_mu.append(float(row[2]))
            compteur_ligne += 1

    # Calcul des propriétés de l'eau à une température donnée
    # 1. Trouve l'élément le plus proche

    differences_temperature = [abs(liste_temperature[i] - temperature) for i in range(len(liste_temperature))]
    index_plus_proche = differences_temperature.index(min(differences_temperature))
    temprature_plus_proche = liste_temperature[index_plus_proche]

    # 2. Calcule la valeur intermédiaire par interpolation. On assume que la température est toujours entre 0 et 40
    # inclusivement.

    if temprature_plus_proche > temperature:
        a = index_plus_proche - 1
        b = index_plus_proche
    else:
        a = index_plus_proche
        b = index_plus_proche + 1

    rho = liste_rho[a] + (liste_rho[b] - liste_rho[a]) * \
        ((temperature - liste_temperature[a]) / (liste_temperature[b] - liste_temperature[a]))
    mu = liste_mu[a] + (liste_mu[b] - liste_mu[a]) * \
        ((temperature - liste_temperature[a]) / (liste_temperature[b] - liste_temperature[a]))

    return rho, mu


def calcule_rep(diametre_particule, V, rho_eau, mu_eau):
    Rep = (diametre_particule * V * rho_eau) / mu_eau
    return Rep


def regime_stockes(diametre_particule, rho_particule, rho_eau, mu_eau):
    V = ((g * diametre_particule ** 2) / 18) * ((rho_particule - rho_eau) / mu_eau)
    Rep = calcule_rep(diametre_particule, V, rho_eau, mu_eau)
    Cd = 24 / Rep

    return V, Cd, Rep


def regime_intermediaire(Rep, diametre_particule, rho_particule, rho_eau, mu_eau):
    Cd = (24 / Rep) * (1 + 0.14 * Rep**0.7)
    V = math.sqrt(((4 * g * diametre_particule) / (3 * Cd)) * ((rho_particule - rho_eau) / rho_eau))
    Rep = calcule_rep(diametre_particule, V, rho_eau, mu_eau)

    return V, Cd, Rep


def calcule_vitesse(rho_particule, diametre_particule, temperature_eau):
    rho_eau, mu_eau = proprietes_eau(temperature_eau)

    V, Cd, Rep = regime_stockes(diametre_particule, rho_particule, rho_eau, mu_eau)
    vitesse_avant = V
    print("Régime de Stockes\nV={:.3f}, Cd={:.3f}, Rep={:.3f}".format(V, Cd, Rep))

    if Rep <= 0.3:
        return vitesse_avant
    elif Rep > 1000:
        return None
    else:
        V, Cd, Rep = regime_intermediaire(Rep, diametre_particule, rho_particule, rho_eau, mu_eau)
        vitesse_apres = V
        print("Régime intermédiaire\nV={:.3f}, Cd={:.3f}, Rep={:.3f}".format(V, Cd, Rep))

    while abs(vitesse_avant - vitesse_apres) > 0.001 and Rep >= 0.3:
        vitesse_avant = vitesse_apres
        V, Cd, Rep = regime_intermediaire(Rep, diametre_particule, rho_particule, rho_eau, mu_eau)
        vitesse_apres = V
        print("V={:.3f}, Cd={:.3f}, Rep={:.3f}".format(V, Cd, Rep))

    return vitesse_apres


if __name__ == "__main__":
    rho_particule = 2000  # kg/m^3
    diametre_particule = 1.0e-3  # m
    temperature_eau = 14.3  # degres celsius

    vitesse_particule = calcule_vitesse(rho_particule, diametre_particule, temperature_eau)
