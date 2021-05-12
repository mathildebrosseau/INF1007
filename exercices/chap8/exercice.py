#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from os import path
import json
from recettes import add_recipes, print_recipe

# TODO: Définissez vos fonction ici

def exercice1(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as f1, open(fichier2, 'r', encoding='utf-8') as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"Les fichiers sont différents. À la ligne {index + 1}, on a: ", line1, "versus: ", line2)
                break

def exercice2(fichier, fichier_copie):
    with open(fichier, 'r', encoding="utf-8") as original, open(fichier_copie, 'w', encoding='utf-8') as copie:
        for ligne_originale in original:
            copie.write(ligne_originale.replace(' ', '   '))

def exercice3(file_path, result_file_path):
    with open(file_path, encoding='utf-8') as f:
        note_percent = f.read().splitlines()
        print(note_percent)

    with open(result_file_path, 'w', encoding='utf-8') as f:
        for note in note_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    f.write(note  + ' ' + key + '\n')
                    break

def delete_recipe(recipes):
    name = input("Entrez le nom de la recette à supprimer. \n")
    if name in recipes:
        del recipes[name]
        print(f"La recette {name} est supprimée. \n")
    else:
        print("La recette n'existe pas. \n")
    return recipes

def exercice4(file_path = "./recipes.json"):
    if path.exists(file_path):
        recipes = json.load(open(file_path, 'r')) # mode lecture d'un fichier binaire
    else:
        recipes = dict()

    while True:
        choice = input("Choisissez une option: \n a : ajouter une recette \n b : modifier une recette \n c : supprimer une recette \n d : afficher une recette \n e : quitter le programme \n").strip()
        if choice == 'a':
            recipes = add_recipes(recipes)
        elif choice == 'b':
            recipes = add_recipes(recipes)
        elif choice == 'c':
            recipes = delete_recipe(recipes)
        elif choice == 'd':
            print_recipe(recipes)
        elif choice == 'e':
            break
        else:
            print("Choix invalide, réessayez svp.")
    json.dump(recipes, open(file_path, 'w'))

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    #exercice1(r"C:\Users\Mathi\Documents\GitHub\c04-ch8-exercices-mathildebrosseau\exemple.txt", r"./exemple2.txt")
    #exercice2(r"C:\Users\Mathi\Documents\GitHub\c04-ch8-exercices-mathildebrosseau\exemple.txt", r"./exemple2_copie.txt")
    #exercice3(r"./notes.txt", "./notes_letter.txt")
    #exercice4()
    43.isdigit()