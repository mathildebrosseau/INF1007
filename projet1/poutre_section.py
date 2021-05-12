import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm
I_rectangle = (b * h**3) / 12
delta_rectangle = (F * L**3) / (3 * (E * 1000) * I_rectangle)

# poutre carrée
a = 15  # en mm
I_carrée = a**4 / 12
delta_carrée = (F * L**3) / (3 * (E * 1000) * I_carrée)

# poutre ronde
d = 5  # en mm
I_ronde = (math.pi * d) / 64
delta_ronde = (F * L**3) / (3 * (E * 1000) * I_ronde)

# poutre creuse
D = 15  # en mm
d = 5  # en mm
I_creuse = (math.pi * (D**4 - d**4)) / 64
delta_creuse = (F * L**3) / (3 * (E * 1000) * I_creuse)

# Calcul de la section optimale
deltas = [delta_carrée, delta_ronde, delta_creuse, delta_rectangle]
types = ['carrée', 'ronde', 'creuse', 'rectangle']

for i in range(len(deltas)):
    if deltas[i] == min(deltas):
        delta_max= deltas[i]
        type_min = types[i]

print(f"Le type de section minimisant la déformation maximale est {type_min}, avec un déformation de {format(delta_max, '0.2f')} mm.")

#On aurait aussi pu résoudre le problème en utilisant plusieurs if statements à la chaîne selon cette démarche qui est moins élégante :
#deltas = [delta_rectangle, delta_carrée, delta_ronde, delta_creuse]
#if min(deltas) == delta_rectangle:
    #delta_minimum = delta_rectangle
    #type_minimum = "rectangle"
#if min(deltas) == delta_carrée:
    #delta_minimum = delta_carrée
    #type_minimum = "carrée"
#if min(deltas) == delta_ronde:
    #delta_minimum = delta_ronde
    #type_minimum = "ronde"
#if min(deltas) == delta_creuse:
    #delta_minimum = delta_creuse
    #type_minimum = "creuse"
#print(f"Le type de section minimisant la déformation maximale est {type_minimum}, avec un déformation de {format(delta_minimum,'0.2f')} mm.")


