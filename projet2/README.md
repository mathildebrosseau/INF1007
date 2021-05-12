# Projet 2 - Pas si long!

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le lundi 19 octobre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20201019T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif
Pour ce projet, vous devez implémenter un algorithme de réduction de la longueur des adresses web (ou URL shortener).

Le programme que vous allez implémenter contiendra deux composantes :
1. Lorsque l'utilisateur fournit une adresse web, le programme doit fournir une nouvelle adresse réduite, qui est composée d'un préfixe (`http://inf1007.polymtl.ca/`) et d'un code de 8 caractères (ex: `A8gHjf3`).
2. Lorsque l'utilisateur fournit une adresse réduite (l'assemblage du préfixe et du code), le programme doit fournir l'adresse originale correspondante, si elle existe dans la base de données.

Pour ce faire, vous devez compléter le fichier `exercice.py`, qui contient 4 fonctions. Vous devez modifier 3 de ces fonctions : `chargement()`, `reduit()` et `allonge()` pour lesquelles les définitions vous sont données :

1. ### chargement()

Cette fonction charge en mémoire le contenu de la base de données des adresses enregistrées.

La base de données est stockée dans un fichier CSV. Chaque ligne de ce fichier correspond à la combinaison de l'adresse web originale et du code correspondant. Le code permettant de lire le fichier est déjà implémentée mais **vous devez compléter la fonction** en choisissant le type de structure de données appropriée pour manipuler les données dans le programme.

2. ### reduit()

À partir de l'adresse passée en paramètre, cette fonction doit retourner une adresse réduite **unique**. L'adresse fournie en sortie du programme doit prendre le préfixe `http://inf1007.polymtl.ca/`, suivi par une chaîne de 8 caractères (le code) choisis aléatoirement parmi les caractères suivants :
- les lettres minuscules ou majuscules
- les chiffres
- le tiret (-) ou le tiret bas (_)

Alternativement, la fonction peut fournir une adresse personnalisée (ex: `http://inf1007.polymtl.ca/projet2` ou `http://inf1007.polymtl.ca/Benjamin`), en passant le code désiré en paramètre (ex: `personnalisation='Benjamin'`).

Dans les deux cas de figure, la fonction doit retourner une adresse unique (qui n'existe donc pas encore dans la base de données). La base de données peut être chargée en mémoire à l'aide de la fonction `chargement()` implémentée plus haut.

Après avoir généré l'adresse réduite, la fonction enregistre les deux adresses (originale et réduite) en utilisant la fonction `enregistrement()`.

Si le code personnalisé fourni en paramètre existe déjà dans la base de données, la fonction doit retourner `None`. Sinon, elle retourne l'adresse réduite.

Si l'enregistrement dans la base de données n'a pas été réalisé, c'est-à-dire si la fonction `enregistrement()` retourne `False`, la fonction doit retourner `None`.

**Vous devez implémenter cette fonction au complet.** Pour vous aider, vous pouvez utiliser les modules `string` et `random` de Python.

3. ### allonge()

Cette fonction doit retourner l'adresse originale correspondant à l'adresse réduite passée en paramètre.

En premier lieu, la fonction doit vérifier si l'adresse fournie en paramètre correspond à une entrée dans sa base de données, en réalisant deux vérifications:
1. l'adresse réduite doit débuter avec la chaîne de caractère `http://inf1007.polymtl.ca/`. Si ce n'est pas le cas, la fonctione doit retourner `None`.
2. le code inclus dans l'adresse réduite doit exister dans la base de données. Si ce n'est pas le cas, la fonction doit retourner `None`.

Si le code de l'adresse réduite existe dans la base de données, la fonction doit retourner l'adresse originale.

**Vous devez implémenter cette fonction au complet.**

## Exemple de déroulement du programme

```
>>> from exercice import *
>>> reduit('http://test.ca/mon fichier')
Erreur : l'adresse longue fournie en paramètre contient un espace.
>>> adr = reduit('http://www.polymtl.ca')
>>> print(adr)
http://inf1007.polymtl.ca/7QoScAGl
>>> adr = reduit('http://www.polymtl.ca', personnalisation='INF1007')
>>> print(adr)
http://inf1007.polymtl.ca/INF1007
>>> print(allonge(adr))
http://www.polymtl.ca
```
