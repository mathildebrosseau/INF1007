import csv
import string
import random


def enregistrement(adresse_longue, code):
    """
    Cette fonction enregistre, dans un fichier texte, la correspondance entre les adresses web longues et courtes.
    La fonction prend en paramètre l'adresse longue fournie par l'utilisateur et le code associé à cette adresse.
    La fonction vérifie au préalable si les adresses contiennent des espaces. Si c'est le cas, la fonction retourne False.
    Si l'enregistrement s'est bien déroulé, la fonction retourne True.
    """

    # Vérifie que les adresses ne contiennent pas d'espaces
    if ' ' in code:
        print('Erreur : le code fourni en paramètre contient un espace.')
        return False
    elif ' ' in adresse_longue:
        print('Erreur : l\'adresse longue fournie en paramètre contient un espace.')
        return False
    with open('data/database.csv', mode ='a', newline='\n') as f:
        addresswriter = csv.writer(f, delimiter=' ')
        addresswriter.writerow([code, adresse_longue])
    return True


def chargement():
    """
    Cette fonction charge en mémoire le contenu de la base de données des adresses enregistrées.
    """

    # TODO: initialiser la structure de données vide
    donnees = dict()

    with open('data/database.csv', mode='r') as f:
        addressreader = csv.reader(f, delimiter=' ')
        for row in addressreader:
            code, adresse_longue = row[0], row[1]

            # TODO: enregistrer les adresses dans une structure de données appropriée
            donnees[code] = adresse_longue
    return donnees


def reduit(adresse_longue, personnalisation=None):
    """
    À partir de l'adresse passée en paramètre, cette fonction retourne une adresse réduite unique.
    L'adresse fournie en sortie du programme prend le préfixe http://inf1007.polymtl.ca/,
    suivi par une chaîne de 8 caractères choisis aléatoirement parmi les suivantes :
    - des lettres minuscules ou majuscules
    - des chiffres
    - un tiret (-) ou un tiret bas (_)

    Alternativement, la fonction peut fournir une adresse personnalisée (ex: http://inf1007.polymtl.ca/projet2 ou http://inf1007.polymtl.ca/Benjamin),
    en passant le suffixe en paramètre (ex: personnalisation='Benjamin').

    Dans les deux cas de figure, la fonction doit retourner une adresse unique (qui n'existe donc pas encore dans la base de données).
    La base de données peut être chargée en mémoire à l'aide de la fonction "chargement()".
    Après avoir généré l'adresse courte, la fonction enregistre les deux adresses en utilisant la fonction "enregistrement()".
    Si le suffixe personnalisé fourni en paramètre existe déjà dans la base de données, la fonction doit retourner None.
    Si l'enregistrement dans la base de données n'a pas été réalisé, la fonction doit retourner None.
    """

    database = chargement()
    # TODO : implémenter la fonction

    if personnalisation == None:
        code = ''.join(random.choice(string.ascii_letters + string.digits + "_" + "-") for length in range(8))
        if code not in database.keys():
            adresse_courte = "http://inf1007.polymtl.ca/" + code
            if enregistrement(adresse_longue, code) == False:
                return None
            else:
                enregistrement(adresse_longue, code)
        else:
            return None
    else:
        if personnalisation not in database.keys():
            adresse_courte = "http://inf1007.polymtl.ca/" + personnalisation
            if enregistrement(adresse_longue, personnalisation) == False:
                return None
            else:
                enregistrement(adresse_longue, personnalisation)
        else:
            return None
    return adresse_courte


def allonge(adresse_courte):
    """
    Cette fonction returne l'adresse originale de l'adresse passée en paramètres.
    La fonction vérifie que l'adresse fournie en paramètre correspond à son système, donc qu'elle débute avec "http://inf1007.polymtl.ca/".
    Si ce n'est pas le cas, la fonctione retourne None.
    Si le code de l'adresse n'existe pas dans la base de données, la fonction retourne None.
    Si le code de l'adresse existe dans la base de données, la fonction retourne l'adresse originale.
    """

    database = chargement()
    # TODO : implémenter la fonction
    if str(adresse_courte)[0:26] != "http://inf1007.polymtl.ca/":
        return None
    else:
        if str(adresse_courte)[26:] not in database.keys():
            return None
        else:
            return database[str(adresse_courte)[26:]]


reduit('http://test.ca/mon fichier')
adr = reduit('http://www.polymtl.ca')
print(adr)
adr = reduit('http://www.polymtl.ca', personnalisation='INF1007')
print(adr)
print(allonge(adr))
