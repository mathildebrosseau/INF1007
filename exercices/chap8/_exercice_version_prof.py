#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes, print_recipe
from os import path
import pickle

# TODO: Définissez vos fonction ici

def exercice1(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, encoding="utf-8") as f2:
        for line1 in f1:
            line2 = f2.readline()
            if line1 != line2:
                print("The files are not identical")
                print(line1)
                print("Is not the same as:")
                print(line2)
                break


def exercice2(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        for line in f1:
            words = line.split()
            f2.write("   ".join(words) + "\n")


def exercice3(note_path, result_file_path):
    with open(note_path, encoding="utf-8") as note_file:
        notes_percent = note_file.readlines()   # To get rid of \n: note_file.read().splitlines()

    with open(result_file_path, "w", encoding="utf-8") as result_file:
        for note in notes_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    result_file.write(note.strip() + " " + key + "\n")
                    break


def delete_recipe(dictionary):
    name = input("Entrez le nom de la recette que vous voulez supprimer.\n")

    if name in dictionary:
        del dictionary[name]
        print("La recette est supprimée!")
    else:
        print("Cette recette n'existe pas!")

    return dictionary


def exercice4(recipes_path):
    if path.exists(recipes_path):
        recipes = pickle.load(open(recipes_path, 'rb'))
    else:
        recipes = dict()

    while True:
        choice = input("Choisissez une option: \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette \n d) Afficher \n e) Quitter le programme\n").strip()

        if choice == "a":
            recipes = add_recipes(recipes)
        elif choice == "b":
            recipes = add_recipes(recipes)
        elif choice == "c":
            recipes = delete_recipe(recipes)
        elif choice == "d":
            print_recipe(recipes)
        elif choice == "e":
            break
        else:
            print("L'option choisi n'est pas valide!")

    pickle.dump(recipes, open(recipes_path, "wb"))


def exercice5(file_path):
    with open(file_path, encoding="utf-8") as f:
        words = f.read().strip().split()

    number = [float(w) for w in words if w.isnumeric()]

    return sorted(number)


def exercice6(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        for index, line in enumerate(f1):
            if not index % 2:
                f2.write(line)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice1("./exemple.txt", "./exemple2.txt")
    exercice2("./exemple.txt", "./exemple_copy.txt")
    exercice3("./notes.txt", "./notes_letter.txt")
    exercice4("./recettes.p")
    print(exercice5("./exemple.txt"))
    exercice6("./notes.txt", "./notes_skip.txt")

    pass
