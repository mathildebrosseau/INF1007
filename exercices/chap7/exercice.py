#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
#from math import pi
#import sys
#sys.path.insert(1, r"C:\Users\Mathi\Documents\GitHub\c04-ch6-exercices-mathildebrosseau")
#from exercice_chapitre6 import frequence

# TODO: Définissez vos fonction ici
#def masse_volume(a=1, b=2, c=3, p=32):
    #volume = 4/3 * (pi * a * b * c)
    #masse = p * volume
    #return (volume, masse)

#exercice 4 du ppt chapitre 7
#1) 15
#2) cas de base = a
#3) le if b==1 (critère d'arrêt) et le fait qu'on fait b-1 à chaque récursivité
#3) f(a,b) = a*b

from turtle import *
def draw_tree() -> object:
    setheading(90)
    color("green")
    draw_branch()
    done()

def draw_branch(branch_length = 70, pen_size = 7, angle = 35):
    if branch_length > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 10, pen_size - 1, angle - 5)
        left(2 * angle)
        draw_branch(branch_length - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_length)


def profondeur_liste(liste, profondeur = 0, liste_de_profondeur = []):
    if type(liste) is not list:
        return profondeur

    for element in liste:
        liste_de_profondeur.append(profondeur_liste(element, profondeur + 1, liste_de_profondeur))

    return max(liste_de_profondeur)




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(masse_volume())
    #print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("Ceci est uuuuuuuuuuuuune phrase"))
    #draw_tree()
    print(profondeur_liste([[1, [[2, 3, [2]]]], [], [3]]))