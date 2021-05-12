# Projet 3 - Vitesse de chute

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 15 novembre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20201115T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif
Ce problème consiste à calculer la vitesse d’une particule dans l’eau, en utilisant un processus itératif et en tenant compte du type d’écoulement. Certaines caractéristiques du problème sont connues et spécifiées. Toutes les mesures doivent être effectuées dans le système de mesure international.

Dans ce projet, vous devez compléter deux aspects de programmation : 
- l'implémentation de fonctions pour résoudre le problème
- l'implémentation de tests unitaires pour vérifier que votre programme fonctionne bien.

Afin de calculer la vitesse de la particule, vous devez implémenter les fonctions suivantes dans le fichier [exercice.py](exercice.py) : 
1. `proprietes_eau(temperature)`, 
2. `regime_stockes(diametre_particule, rho_particule, rho_eau, mu_eau)`, 
3. `regime_intermediaire(Rep, diametre_particule, rho_particule, rho_eau, mu_eau)` et 
4. `calcule_vitesse(rho_particule, diametre_particule, temperature_eau)`.

### 1. proprietes_eau(temperature)

Cette fonction doit calculer les propriétés de l'eau (<img src="https://render.githubusercontent.com/render/math?math=\rho"> et <img src="https://render.githubusercontent.com/render/math?math=\mu">)  pour une température donnée, en s'aidant de la base de données fournie dans le fichier [data/data.csv](data/data.csv).

Cependant, cette base de données ne fournit que des valeurs de <img src="https://render.githubusercontent.com/render/math?math=\rho"> et <img src="https://render.githubusercontent.com/render/math?math=\mu"> pour des températures égales à un multiplication de 5. Vous devez donc implémenter un algorithme qui calcule les valeurs de <img src="https://render.githubusercontent.com/render/math?math=\rho"> et <img src="https://render.githubusercontent.com/render/math?math=\mu"> pour des valeurs intermédiaires, en interpolant linéairement les valeurs présentes dans la base de données.

Par exemple, une température de 14.3˚C doit approximer les propriétés de l'eau à <img src="https://render.githubusercontent.com/render/math?math=\rho=999.184"> et <img src="https://render.githubusercontent.com/render/math?math=\mu=0.0011638">.

On assume que la température passée en paramètre est toujours entre 0 et 40, exclusivement.

### 2. regime_stockes(diametre_particule, rho_particule, rho_eau, mu_eau)

Cette fonction retourne les valeurs de <img src="https://render.githubusercontent.com/render/math?math=V">, <img src="https://render.githubusercontent.com/render/math?math=C_D"> et <img src="https://render.githubusercontent.com/render/math?math=R_{ep}"> dans le cas d'un régime de Stockes (<img src="https://render.githubusercontent.com/render/math?math=R_{ep}≤0.3">), en utilisant les formules ci-dessous :

<img src="data/eq_V_stockes.gif">

<img src="data/eq_cd_stockes.gif">

### 3. regime_intermediaire(Rep, diametre_particule, rho_particule, rho_eau, mu_eau)

Cette fonction retourne les valeurs de <img src="https://render.githubusercontent.com/render/math?math=V">, <img src="https://render.githubusercontent.com/render/math?math=C_D"> et <img src="https://render.githubusercontent.com/render/math?math=R_{ep}"> dans le cas d'un régime intermédiaire (<img src="https://render.githubusercontent.com/render/math?math=0.3<R_{ep}≤1000">), en utilisant les formules ci-dessous :

<img src="data/eq_V_inter.gif">

<img src="data/eq_cd_inter.gif">


### 4. calcule_vitesse(rho_particule, diametre_particule, temperature_eau)

Cette fonction calcule et retourne la vitesse d'une particule dans l'eau en fonction de la température de l'eau ainsi que des propriétés de la particule (masse volumique et diamètre).

- Le diamètre de la particule est <img src="https://render.githubusercontent.com/render/math?math=d_p=1 mm">
- La masse volumique de la particule est <img src="https://render.githubusercontent.com/render/math?math=\rho_p=2000 kg/m^3">
- Le nombre de Reynolds de la particule est donné par <img src="https://render.githubusercontent.com/render/math?math=R_{ep}=\frac {d_p V \rho_{ H2O}}{\mu}">

#### **Algorithme itératif pour calculer la vitesse de chute de la particule :**
1. Initialement, on fait l’hypothèse que l’on se trouve dans un régime de Stockes
    - On calcule <img src="https://render.githubusercontent.com/render/math?math=V">, <img src="https://render.githubusercontent.com/render/math?math=C_D"> et <img src="https://render.githubusercontent.com/render/math?math=R_{ep}">
    - Si <img src="https://render.githubusercontent.com/render/math?math=R_{ep}<0.3">, le problème est résolu et la vitesse de la particule est égal à <img src="https://render.githubusercontent.com/render/math?math=V">
    - Sinon, on passe à l’étape suivante.
2. On passe en régime intermédiaire
	- On utilise <img src="https://render.githubusercontent.com/render/math?math=R_{ep}"> calculé précédemment pour calculer <img src="https://render.githubusercontent.com/render/math?math=C_D">, <img src="https://render.githubusercontent.com/render/math?math=V"> et le nouveau <img src="https://render.githubusercontent.com/render/math?math=R_{ep}">
	- On compare <img src="https://render.githubusercontent.com/render/math?math=V"> avec <img src="https://render.githubusercontent.com/render/math?math=V"> calculé précédemment. Si la différence est plus grande que 0.001, on recommence l’étape 2, en s’assurant de rester en régime intermédiaire.
	- Si la différence est plus petite que 0.001, le problème est résolu.

À chaque itération, il est important d’afficher les résultats de <img src="https://render.githubusercontent.com/render/math?math=V">, <img src="https://render.githubusercontent.com/render/math?math=C_D"> et <img src="https://render.githubusercontent.com/render/math?math=R_{ep}">.

## Exemple :
```
>>>calcule_vitesse(rho_particule=2000, diametre_particule=1e-3, temperature_eau=14.3)

Régime de Stockes
V=0.469, Cd=0.060, Rep=402.245
Régime intermédiaire
V=0.146, Cd=0.616, Rep=125.232
V=0.116, Cd=0.981, Rep=99.224
V=0.110, Cd=1.088, Rep=94.204
V=0.108, Cd=1.114, Rep=93.091
V=0.108, Cd=1.120, Rep=92.836
```

# Tests unitaires
Afin de vous assurer que votre programme fonctionne bien, vous devez implémenter un test unitaire pour chacune des quatre fonctions implémentées, dans le fichier [test_exercice.py](test_exercice.py).

