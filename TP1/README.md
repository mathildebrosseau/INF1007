# TP1

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 27 septembre 2020 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

Ce TP a pour objectif de vous introduire à l'algorithmie avec le langage de programmation Python.
Celui-ci est composé de 5 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir lu le fichier [instructions.md](instructions.md) et d'avoir téléchargé les fichiers exercices1-5.py que vous devrez compléter.
Pour ce TP, certaines contraintes sont à respecter:
- Vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.
- Il est interdit de manipuler des chaînes de caractère.
- Il est interdit d'utiliser les structures de répétitions (for, while).

## Exercice 1:
Dans cet exercice, vous devez calculer l'énergie cinétique d'une voiture. Le programme commence en demandant à l'utilisateur de saisir la masse (en kg) et la vitesse (en km/h) de la voiture, il suffit de compléter la fonction `calculerEnergie()`.
```python
    def calculerEnergie(masse,vitesse):
        # TODO convertir la vitesse en mètre par seconde, assigner la valeur à la variable "vitesse"
        vitesse=
        
        # TODO calculer l'énergie cinétique, assigner la valeur à la variable "energieCinetique"
        energieCinetique=
        
        return energieCinetique
```

## Exercice 2:
Dans cet exercice, vous devez résoudre une équation quadratique de la forme <img src="https://render.githubusercontent.com/render/math?math=ax^2"> + <img src="https://render.githubusercontent.com/render/math?math=bx"> + <img src="https://render.githubusercontent.com/render/math?math=c">. Le programme commence en demandant à l'utilisateur de saisir la valeur des variables `a`, `b` et `c`. Il suffit de compléter la fonction `resoudreEquation()`.
```python
    def resoudreEquation(a, b, c):
    # TODO: Calculer le discriminant et assigner la valeur dans la variable "delta"
    delta =

    # TODO: Déterminer la condition (bool) qui correspond à la situation où l'équation n'a aucune solution et m assigner le résultat dans la variable "naPasDeSolution"
    naPasDeSolution =

    if naPasDeSolution:
        # ces lignes de code seront executé si il y'a aucune racine
        # TODO: afficher sur l'écran "Aucune racine"

        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond à la situation où il existe une seule solution à l'équation et mettre la valeur dans "aUneSeuleSolution"
    aUneSeuleSolution =

    if aUneSeuleSolution:
        # ces ligne de code seront executées s'il y'a une seule racine
        # TODO: affichez sur l'écran "Une seule racine"

        # TODO: assignez a la variable x1 la valeur de la racine
        x1 =
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à la situation où il existe deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions =

    if aDeuxSolutions:
        # TODO: affichez sur l'écran "Deux racines"

        # TODO: calculez la première racine, assignez la a "x1"
        x1 =

        # TODO: calculez la deuxième racine, assignez la a "x2"
        x2 =

        # ne pas modifier cette ligne
        return x1, x2
```
## Exercice 3:
Dans cet exercice, vous devez calculer le nombre de chiffres qui compose un nombre indiqué par l'utilisateur. Cepandant, vous ne pouvez utiliser que les fonctions de la libraire Math.
```python
    def calculerNombreChiffres(nombre):

        # TODO: Déterminer le nombre de chiffres de "nombre" et mettre la valeur dans "nombreDeChiffres"
        nombreDeChiffres =

        # TODO: Afficher la valeur de "nombreDeChiffres"

        return nombreDeChiffres
```
## Exercice 4:
Dans cet exercice vous devez convertir un nombre de secondes en nombres d'années, semaines, jours, heures, minute et secondes. Par exemple, si l'utilisateur rentre '633323104' secondes, votre programme devra renvoyé 20 années, 4 semaines, 2 jours, 3 heures, 5 minutes et 4 secondes. Vous pouvez créer d'autres variables pour vous aider.

PS: On considère qu'une année est composée exactement de 365 jours !

```python
    def decomposer(secondes):
        # TODO: Assignez à la variable "annees" le nombre d'années
        annees =

        # TODO: Assignez à la variable "semaines" le nombre de semaines restantes
        semaines =

        # TODO: Assignez à la variable "jours" le nombre de jours restants
        jours =

        # TODO: Assignez à la variable "heures" le nombre d'heures restantes
        heures =

        # TODO: Assignez à la variable "minute" le nombre de minutes restantes
        minutes =

        # TODO: Assignez à la variable "secondes" le nombre de secondes restantes
        secondes =

        # TODO: Affichez le nombres d'années, semaines, jours, heures, minutes et secondes

        return (annees ,semaines ,jours ,heures ,minutes ,secondes)
```
## Exercice 5:
Dans cet exercice, vous manipulerez les nombres complexes. Vous devez compléter deux fonctions, la fonction `trouverModule()` qui retourne le module d'un nombre complexe et la fonction `effectuerRotation()` qui effectue une rotation du nombre selon un angle saisi par l'utilisateur. Pour rappel, pour effectuer une rotation d'un angle <img src="https://render.githubusercontent.com/render/math?math=\alpha">, il suffit de multiplier le nombre complexe par <img src="https://render.githubusercontent.com/render/math?math=(cos(\alpha)"> + <img src="https://render.githubusercontent.com/render/math?math=sin(\alpha)i)">.
Voici les deux fonctions à compléter :
```python
        def decomposer(secondes):
            def trouverModule(nombreComplexe):
            # TODO: Calculer le module du nombre complexe et l'assigner dans "module"
            module =

            return module
```
```python
        def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

            module = trouverModule(nombreComplexe)
            angle = trouverAngle(nombreComplexe)

            # TODO: Afficher le module et l'angle du nombre complexe (3 decimales de précision)


            # TODO: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'

            resultat =

            nouveauModule = trouverModule(resultat)
            nouvelAngle = trouverAngle(resultat)

            # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)

            return resultat
```
Si votre programme a été correctement écrit, vous devriez voire une simulation visuelle du nombre complexe avant et apres rotation:
<p align="center">
     <img src="img/complexe.PNG?raw=true"/>
</p>

