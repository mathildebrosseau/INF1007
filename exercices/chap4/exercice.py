#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_even_len(string: str) -> bool:
    if len(string) % 2 == 0:
        return True
    else:
        return False


def remove_third_char(string: str) -> str:
    return string[:2] + string[3:]


def replace_char(string: str, old_char: str, new_char: str) -> str: #même chose de string.replace(old_chard, new_char)
    for i in range(len(string)):
        if string[i] == old_char:
            string = string[:i] + new_char + string[i + 1:]
    return string


def get_number_of_char(string: str, char: str) -> int:
    char_number = 0
    for current_char in string:
        if current_char == char:
            char_number += 1
    return char_number


def get_number_of_words(sentence: str, word: str) -> int:
    words = sentence.split()
    word_count = 0
    for current_word in words:
        if current_word == word:
            word_count += 1
    return word_count


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans 'hello world!' est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
