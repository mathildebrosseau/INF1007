<p align="center">
  <img src="https://promptinnov.com/wp-content/uploads/2019/02/polytechnique.jpg" />
</p>

# TP5: Librairies scientifiques et graphiques

- [Directives particulières](#directives-particuli%C3%A8res)
- [Introduction](#introduction)
- [Partie 1: Importer et manipuler les bases de données](#partie-1-Importer-et-manipuler-les-bases-de-donn%C3%A9es)
- [Partie 2: Analyse des données](#partie-2-analyse-des-donn%C3%A9es)
- [Partie 3: Modélisation et prévision](#partie-3-mod%C3%A9lisation-et-pr%C3%A9vision)
- [Annexe: Guide et normes de codage](#annexe-guide-et-normes-de-codage)

:alarm_clock: [Date de remise le Dimanche 22 novembre 23h59](https://www.timeanddate.com/countdown/generic?iso=20201122T235959&p0=165&msg=Remise+TP5&font=cursive)

## Directives particulières
* Le fichier Package.txt contient les packages nécessaires pour ce laboratoire;
* Un fichier main.ipynb est disponible si vous voulez faire le laboratoire sur Jupyter;
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;  
* Dans chaque programme, vous pouvez ajouter d’autres fonctions à celles décrites dans l’énoncé pour améliorer la lisibilité.

## Introduction
<p align="justify">
L’analyse des données fait partie des disciplines les plus prisées de nos jours. Outil stratégique au sein des organisations, elle permet entre autres de mieux comprendre des événements qui se produisent avec les facteurs qui les favorisent, ou encore de mesurer l’impact d’une opération ou d’une politique grâce à des indicateurs de performance. Dans ce laboratoire, nous essayons de mieux comprendre l’évolution de la pandémie du nouveau coronavirus Covid-19 au Canada et dans les pays les plus touchés.</p>

## Partie 1: Importer et manipuler les bases de données
<p align="justify">
L'une des bases de données la plus largement utilisées aujourd'hui fournissant des données liées au Covid-19 est celle fournie par le Centre de science et d'ingénierie des systèmes de l'université John Hopkins, auquel il est possible d'accéder sur GitHub. </p>

### 1.1. Import des bases de données:
<p align="justify">
L'ensemble des données peuvent être directement importées dans des bases de données avec la méthode read_csv de la bibliothèque Pandas. Télécharger les bases de données et les manipuler après n’est pas toujours une bonne pratique, il est préférable d'utiliser les liens qui pointent vers les fichiers CSV archivés sur GitHub, car à mesure que la situation change, il devient plus facile de charger et d'actualiser l'analyse avec de nouvelles données.</p>

<p align="justify">
Durant ce laboratoire, on va travailler avec quatre bases de données, dont les liens URL sont stockés dans la variable: add_death_df, add_confirmed_df, add_recovered_df et add_summary_df.</p>

```python
PATH_1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/'
PATH_2 = 'master/csse_covid_19_data/csse_covid_19_time_series/'
ADD_DEATH_DF = PATH_1 + PATH_2 + 'time_series_covid19_deaths_global.csv'
ADD_CONFIRMED_DF = PATH_1 + PATH_2 + 'time_series_covid19_confirmed_global.csv'
ADD_RECOVERED_DF = PATH_1 + PATH_2 + 'time_series_covid19_recovered_global.csv'
ADD_SUMMARY_DF = PATH_1 + 'web-data/data/cases_country.csv'
```

<p align="justify">
La première étape du laboratoire consiste à importer les quatre bases de données. Pour cela on va utiliser la fonction <strong>load_df(...).</strong> Cette fonction a pour objectif d’importer et créer les quatre bases de données à partir des liens URL reçus en paramètre.</p>

```python
[death_df, confirmed_df, recovered_df, summary_df] = dp.load_df(ADD_DEATH_DF, ADD_CONFIRMED_DF, 
                                                                ADD_RECOVERED_DF, ADD_SUMMARY_DF)
```
<p align="justify">
Une fois l’importation des bases de données est effectuée, on doit nous assurer que l’opération s’est bien déroulée. Pour cela on va afficher les 10 dernières colonnes de chaque base de données. Vous trouveriez ci-dessous un aperçu du résultat attendu..</p>

```python
print(death_df.iloc[:,-9:])
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10/30/20</th>
      <th>10/31/20</th>
      <th>11/1/20</th>
      <th>11/2/20</th>
      <th>11/3/20</th>
      <th>11/4/20</th>
      <th>11/5/20</th>
      <th>11/6/20</th>
      <th>11/7/20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1533</td>
      <td>1536</td>
      <td>1536</td>
      <td>1541</td>
      <td>1544</td>
      <td>1548</td>
      <td>1554</td>
      <td>1554</td>
      <td>1556</td>
    </tr>
    <tr>
      <th>1</th>
      <td>502</td>
      <td>509</td>
      <td>518</td>
      <td>527</td>
      <td>532</td>
      <td>536</td>
      <td>543</td>
      <td>549</td>
      <td>557</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1956</td>
      <td>1964</td>
      <td>1973</td>
      <td>1980</td>
      <td>1980</td>
      <td>1999</td>
      <td>2011</td>
      <td>2024</td>
      <td>2036</td>
    </tr>
    <tr>
      <th>3</th>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>279</td>
      <td>284</td>
      <td>286</td>
      <td>289</td>
      <td>291</td>
      <td>296</td>
      <td>299</td>
      <td>300</td>
      <td>303</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>263</th>
      <td>481</td>
      <td>483</td>
      <td>489</td>
      <td>493</td>
      <td>501</td>
      <td>504</td>
      <td>508</td>
      <td>511</td>
      <td>512</td>
    </tr>
    <tr>
      <th>264</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>265</th>
      <td>599</td>
      <td>599</td>
      <td>600</td>
      <td>601</td>
      <td>601</td>
      <td>601</td>
      <td>601</td>
      <td>602</td>
      <td>602</td>
    </tr>
    <tr>
      <th>266</th>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
    </tr>
    <tr>
      <th>267</th>
      <td>242</td>
      <td>243</td>
      <td>243</td>
      <td>245</td>
      <td>246</td>
      <td>248</td>
      <td>248</td>
      <td>250</td>
      <td>251</td>
    </tr>
  </tbody>
</table>

```python
print(confirmed_df.iloc[:,-9:])
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10/30/20</th>
      <th>10/31/20</th>
      <th>11/1/20</th>
      <th>11/2/20</th>
      <th>11/3/20</th>
      <th>11/4/20</th>
      <th>11/5/20</th>
      <th>11/6/20</th>
      <th>11/7/20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41334</td>
      <td>41425</td>
      <td>41501</td>
      <td>41633</td>
      <td>41728</td>
      <td>41814</td>
      <td>41935</td>
      <td>41975</td>
      <td>42033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20634</td>
      <td>20875</td>
      <td>21202</td>
      <td>21523</td>
      <td>21904</td>
      <td>22300</td>
      <td>22721</td>
      <td>23210</td>
      <td>23705</td>
    </tr>
    <tr>
      <th>2</th>
      <td>57651</td>
      <td>57942</td>
      <td>58272</td>
      <td>58574</td>
      <td>58979</td>
      <td>59527</td>
      <td>60169</td>
      <td>60800</td>
      <td>61381</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4665</td>
      <td>4756</td>
      <td>4825</td>
      <td>4888</td>
      <td>4910</td>
      <td>5045</td>
      <td>5135</td>
      <td>5135</td>
      <td>5319</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10558</td>
      <td>10805</td>
      <td>11035</td>
      <td>11228</td>
      <td>11577</td>
      <td>11813</td>
      <td>12102</td>
      <td>12223</td>
      <td>12335</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>263</th>
      <td>53075</td>
      <td>53520</td>
      <td>54060</td>
      <td>54775</td>
      <td>55408</td>
      <td>56090</td>
      <td>56672</td>
      <td>57226</td>
      <td>57657</td>
    </tr>
    <tr>
      <th>264</th>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>265</th>
      <td>2062</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2067</td>
      <td>2070</td>
    </tr>
    <tr>
      <th>266</th>
      <td>16415</td>
      <td>16432</td>
      <td>16480</td>
      <td>16543</td>
      <td>16661</td>
      <td>16698</td>
      <td>16770</td>
      <td>16819</td>
      <td>16908</td>
    </tr>
    <tr>
      <th>267</th>
      <td>8362</td>
      <td>8367</td>
      <td>8374</td>
      <td>8389</td>
      <td>8410</td>
      <td>8427</td>
      <td>8444</td>
      <td>8471</td>
      <td>8498</td>
    </tr>
  </tbody>
</table>


```python
print(recovered_df.iloc[:,-9:])
```

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10/30/20</th>
      <th>10/31/20</th>
      <th>11/1/20</th>
      <th>11/2/20</th>
      <th>11/3/20</th>
      <th>11/4/20</th>
      <th>11/5/20</th>
      <th>11/6/20</th>
      <th>11/7/20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34258</td>
      <td>34321</td>
      <td>34326</td>
      <td>34342</td>
      <td>34355</td>
      <td>34362</td>
      <td>34440</td>
      <td>34440</td>
      <td>34446</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11097</td>
      <td>11189</td>
      <td>11246</td>
      <td>11367</td>
      <td>11473</td>
      <td>11578</td>
      <td>11696</td>
      <td>11861</td>
      <td>12002</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40014</td>
      <td>40201</td>
      <td>40395</td>
      <td>40577</td>
      <td>40577</td>
      <td>41001</td>
      <td>41244</td>
      <td>41510</td>
      <td>41783</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3377</td>
      <td>3475</td>
      <td>3475</td>
      <td>3548</td>
      <td>3627</td>
      <td>3734</td>
      <td>3858</td>
      <td>3858</td>
      <td>4043</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4107</td>
      <td>4523</td>
      <td>4920</td>
      <td>5172</td>
      <td>5230</td>
      <td>5266</td>
      <td>5350</td>
      <td>5626</td>
      <td>5647</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>250</th>
      <td>45896</td>
      <td>46309</td>
      <td>46773</td>
      <td>47169</td>
      <td>47744</td>
      <td>48224</td>
      <td>48680</td>
      <td>49537</td>
      <td>49975</td>
    </tr>
    <tr>
      <th>251</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>252</th>
      <td>1366</td>
      <td>1366</td>
      <td>1366</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
    </tr>
    <tr>
      <th>253</th>
      <td>15600</td>
      <td>15680</td>
      <td>15733</td>
      <td>15733</td>
      <td>15763</td>
      <td>15819</td>
      <td>15827</td>
      <td>15862</td>
      <td>15873</td>
    </tr>
    <tr>
      <th>254</th>
      <td>7884</td>
      <td>7894</td>
      <td>7927</td>
      <td>7939</td>
      <td>7942</td>
      <td>7967</td>
      <td>7975</td>
      <td>7983</td>
      <td>7995</td>
    </tr>
  </tbody>
</table>

```python
print(summary_df)
```

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country_Region</th>
      <th>Last_Update</th>
      <th>Lat</th>
      <th>Long_</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Incident_Rate</th>
      <th>People_Tested</th>
      <th>People_Hospitalized</th>
      <th>Mortality_Rate</th>
      <th>UID</th>
      <th>ISO3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>2020-11-09 04:25:30</td>
      <td>33.939110</td>
      <td>67.709953</td>
      <td>42092.0</td>
      <td>1558.0</td>
      <td>34458.0</td>
      <td>6076.0</td>
      <td>108.126879</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.701416</td>
      <td>4</td>
      <td>AFG</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>2020-11-09 04:25:30</td>
      <td>41.153300</td>
      <td>20.168300</td>
      <td>24206.0</td>
      <td>559.0</td>
      <td>12092.0</td>
      <td>11555.0</td>
      <td>841.128640</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.309345</td>
      <td>8</td>
      <td>ALB</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>2020-11-09 04:25:30</td>
      <td>28.033900</td>
      <td>1.659600</td>
      <td>62051.0</td>
      <td>2048.0</td>
      <td>42037.0</td>
      <td>17966.0</td>
      <td>141.504046</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.300511</td>
      <td>12</td>
      <td>DZA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andorra</td>
      <td>2020-11-09 04:25:30</td>
      <td>42.506300</td>
      <td>1.521800</td>
      <td>5383.0</td>
      <td>75.0</td>
      <td>4248.0</td>
      <td>1060.0</td>
      <td>6966.931987</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.393275</td>
      <td>20</td>
      <td>AND</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Angola</td>
      <td>2020-11-09 04:25:30</td>
      <td>-11.202700</td>
      <td>17.873900</td>
      <td>12433.0</td>
      <td>307.0</td>
      <td>5899.0</td>
      <td>6227.0</td>
      <td>37.829059</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.469235</td>
      <td>24</td>
      <td>AGO</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>185</th>
      <td>West Bank and Gaza</td>
      <td>2020-11-09 04:25:30</td>
      <td>31.952200</td>
      <td>35.233200</td>
      <td>58158.0</td>
      <td>515.0</td>
      <td>50407.0</td>
      <td>7236.0</td>
      <td>1140.036413</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.885519</td>
      <td>275</td>
      <td>PSE</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Western Sahara</td>
      <td>2020-11-09 04:25:30</td>
      <td>24.215500</td>
      <td>-12.885800</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>1.674116</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.000000</td>
      <td>732</td>
      <td>ESH</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Yemen</td>
      <td>2020-11-09 04:25:30</td>
      <td>15.552727</td>
      <td>48.516388</td>
      <td>2070.0</td>
      <td>602.0</td>
      <td>1375.0</td>
      <td>93.0</td>
      <td>6.940261</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.082126</td>
      <td>887</td>
      <td>YEM</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Zambia</td>
      <td>2020-11-09 04:25:30</td>
      <td>-13.133897</td>
      <td>27.849332</td>
      <td>16954.0</td>
      <td>349.0</td>
      <td>15950.0</td>
      <td>655.0</td>
      <td>92.221718</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.058511</td>
      <td>894</td>
      <td>ZMB</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Zimbabwe</td>
      <td>2020-11-09 04:25:30</td>
      <td>-19.015438</td>
      <td>29.154857</td>
      <td>8531.0</td>
      <td>253.0</td>
      <td>8005.0</td>
      <td>273.0</td>
      <td>57.397846</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.965655</td>
      <td>716</td>
      <td>ZWE</td>
    </tr>
  </tbody>
</table>

### 1.2. Prétraitement des données:
<p align="justify">
Au vu de la diversité des sources, les formats des données diffèrent souvent les uns des autres, et ne sont pas toujours compréhensibles ni utiles à l’état brut. À cet effet, le prétraitement s’avère être une étape fondamentale de toute exploration de données, et  sa réussite dépend considérablement de la qualité des résultats de l’analyse proprement dite. Dans cette partie du laboratoire, nous effectuerons quelques transformations et filtres afin de nous focaliser sur l’essentiel et d’en obtenir un format compréhensible et peu fastidieux à analyser. </p>

Les bases de données importées précédemment se divisent en deux catégories :
1. Sommaire mondial des nombres de cas confirmé, mort, actif et rétabli (summary_df).
2. Évolution mondiale des nombres de cas confirmé mort et rétabli (death_df, confirmed_df et recovered_df).

#### 1.2.1. Prétraitement des données mondial:
<p align="justify">
La première transformation qu’on va apporter à la base de données summary_df, consiste à ajouter une colonne au nom de <strong>"Closed"</strong>, qui correspond au nombre de cas fermé dans chaque pays. Pour cela on va utiliser la fonction <strong>summary_add_col(...)</strong>, qui ajoute une colonne à la base de données df reçue en paramètre, le nom et la valeur de cette colonne se trouve respectivement dans les variables col et value. La fonction retourne la nouvelle base de données.</p>

```python
summary_df = dp.summary_add_col(summary_df, "Closed", summary_df["Deaths"] + summary_df["Recovered"])
print(summary_df)
```

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country_Region</th>
      <th>Last_Update</th>
      <th>Lat</th>
      <th>Long_</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Recovered</th>
      <th>Active</th>
      <th>Incident_Rate</th>
      <th>People_Tested</th>
      <th>People_Hospitalized</th>
      <th>Mortality_Rate</th>
      <th>UID</th>
      <th>ISO3</th>
      <th>Closed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>2020-11-09 04:25:30</td>
      <td>33.939110</td>
      <td>67.709953</td>
      <td>42092.0</td>
      <td>1558.0</td>
      <td>34458.0</td>
      <td>6076.0</td>
      <td>108.126879</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.701416</td>
      <td>4</td>
      <td>AFG</td>
      <td>36016.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>2020-11-09 04:25:30</td>
      <td>41.153300</td>
      <td>20.168300</td>
      <td>24206.0</td>
      <td>559.0</td>
      <td>12092.0</td>
      <td>11555.0</td>
      <td>841.128640</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.309345</td>
      <td>8</td>
      <td>ALB</td>
      <td>12651.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>2020-11-09 04:25:30</td>
      <td>28.033900</td>
      <td>1.659600</td>
      <td>62051.0</td>
      <td>2048.0</td>
      <td>42037.0</td>
      <td>17966.0</td>
      <td>141.504046</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.300511</td>
      <td>12</td>
      <td>DZA</td>
      <td>44085.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andorra</td>
      <td>2020-11-09 04:25:30</td>
      <td>42.506300</td>
      <td>1.521800</td>
      <td>5383.0</td>
      <td>75.0</td>
      <td>4248.0</td>
      <td>1060.0</td>
      <td>6966.931987</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.393275</td>
      <td>20</td>
      <td>AND</td>
      <td>4323.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Angola</td>
      <td>2020-11-09 04:25:30</td>
      <td>-11.202700</td>
      <td>17.873900</td>
      <td>12433.0</td>
      <td>307.0</td>
      <td>5899.0</td>
      <td>6227.0</td>
      <td>37.829059</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.469235</td>
      <td>24</td>
      <td>AGO</td>
      <td>6206.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>185</th>
      <td>West Bank and Gaza</td>
      <td>2020-11-09 04:25:30</td>
      <td>31.952200</td>
      <td>35.233200</td>
      <td>58158.0</td>
      <td>515.0</td>
      <td>50407.0</td>
      <td>7236.0</td>
      <td>1140.036413</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.885519</td>
      <td>275</td>
      <td>PSE</td>
      <td>50922.0</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Western Sahara</td>
      <td>2020-11-09 04:25:30</td>
      <td>24.215500</td>
      <td>-12.885800</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>1.674116</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.000000</td>
      <td>732</td>
      <td>ESH</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Yemen</td>
      <td>2020-11-09 04:25:30</td>
      <td>15.552727</td>
      <td>48.516388</td>
      <td>2070.0</td>
      <td>602.0</td>
      <td>1375.0</td>
      <td>93.0</td>
      <td>6.940261</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.082126</td>
      <td>887</td>
      <td>YEM</td>
      <td>1977.0</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Zambia</td>
      <td>2020-11-09 04:25:30</td>
      <td>-13.133897</td>
      <td>27.849332</td>
      <td>16954.0</td>
      <td>349.0</td>
      <td>15950.0</td>
      <td>655.0</td>
      <td>92.221718</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.058511</td>
      <td>894</td>
      <td>ZMB</td>
      <td>16299.0</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Zimbabwe</td>
      <td>2020-11-09 04:25:30</td>
      <td>-19.015438</td>
      <td>29.154857</td>
      <td>8531.0</td>
      <td>253.0</td>
      <td>8005.0</td>
      <td>273.0</td>
      <td>57.397846</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.965655</td>
      <td>716</td>
      <td>ZWE</td>
      <td>8258.0</td>
    </tr>
  </tbody>
</table>

<p align="justify">
Les colonnes <strong>Last_Update, Lat, Long_, Incident_Rate, People_Tested, People_Hospitalized, UID	et ISO3</strong>, ne nous seront pas utiles dans notre analyse. Afin de garder que les colonnes qui vont être utiles pour notre analyse on va utiliser la fonction <strong>summary_extract_col(...)</strong>, qui extrait les colonnes reçues en paramètre à partir de la base de données summary_df. La fonction retourne la base de données filtrée.</p>

```python
summary_df = dp.summary_extract_col(summary_df, COLUMNS)
print(summary_df)
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country_Region</th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Active</th>
      <th>Closed</th>
      <th>Recovered</th>
      <th>Mortality_Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>42092.0</td>
      <td>1558.0</td>
      <td>6076.0</td>
      <td>36016.0</td>
      <td>34458.0</td>
      <td>3.701416</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>24206.0</td>
      <td>559.0</td>
      <td>11555.0</td>
      <td>12651.0</td>
      <td>12092.0</td>
      <td>2.309345</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>62051.0</td>
      <td>2048.0</td>
      <td>17966.0</td>
      <td>44085.0</td>
      <td>42037.0</td>
      <td>3.300511</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andorra</td>
      <td>5383.0</td>
      <td>75.0</td>
      <td>1060.0</td>
      <td>4323.0</td>
      <td>4248.0</td>
      <td>1.393275</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Angola</td>
      <td>12433.0</td>
      <td>307.0</td>
      <td>6227.0</td>
      <td>6206.0</td>
      <td>5899.0</td>
      <td>2.469235</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>185</th>
      <td>West Bank and Gaza</td>
      <td>58158.0</td>
      <td>515.0</td>
      <td>7236.0</td>
      <td>50922.0</td>
      <td>50407.0</td>
      <td>0.885519</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Western Sahara</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>8.0</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Yemen</td>
      <td>2070.0</td>
      <td>602.0</td>
      <td>93.0</td>
      <td>1977.0</td>
      <td>1375.0</td>
      <td>29.082126</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Zambia</td>
      <td>16954.0</td>
      <td>349.0</td>
      <td>655.0</td>
      <td>16299.0</td>
      <td>15950.0</td>
      <td>2.058511</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Zimbabwe</td>
      <td>8531.0</td>
      <td>253.0</td>
      <td>273.0</td>
      <td>8258.0</td>
      <td>8005.0</td>
      <td>2.965655</td>
    </tr>
  </tbody>
</table>

<p align="justify">
Afin de faire une observation en fonction des pays, il nous faut regrouper notre base de données en fonction des pays. Pour cela on va utiliser la fonction <strong>summary_by_country(...)</strong>. Pensez à utiliser la méthode groupby().</p>

```python
summary_df_by_country = dp.summary_by_country(summary_df)
summary_df_by_country.head(10)
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Confirmed</th>
      <th>Deaths</th>
      <th>Active</th>
      <th>Closed</th>
      <th>Recovered</th>
      <th>Mortality_Rate</th>
    </tr>
    <tr>
      <th>Country_Region</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>42092.0</td>
      <td>1558.0</td>
      <td>6076.0</td>
      <td>36016.0</td>
      <td>34458.0</td>
      <td>3.701416</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>24206.0</td>
      <td>559.0</td>
      <td>11555.0</td>
      <td>12651.0</td>
      <td>12092.0</td>
      <td>2.309345</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>62051.0</td>
      <td>2048.0</td>
      <td>17966.0</td>
      <td>44085.0</td>
      <td>42037.0</td>
      <td>3.300511</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>5383.0</td>
      <td>75.0</td>
      <td>1060.0</td>
      <td>4323.0</td>
      <td>4248.0</td>
      <td>1.393275</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>12433.0</td>
      <td>307.0</td>
      <td>6227.0</td>
      <td>6206.0</td>
      <td>5899.0</td>
      <td>2.469235</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>West Bank and Gaza</th>
      <td>58158.0</td>
      <td>515.0</td>
      <td>7236.0</td>
      <td>50922.0</td>
      <td>50407.0</td>
      <td>0.885519</td>
    </tr>
    <tr>
      <th>Western Sahara</th>
      <td>10.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>8.0</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>2070.0</td>
      <td>602.0</td>
      <td>93.0</td>
      <td>1977.0</td>
      <td>1375.0</td>
      <td>29.082126</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>16954.0</td>
      <td>349.0</td>
      <td>655.0</td>
      <td>16299.0</td>
      <td>15950.0</td>
      <td>2.058511</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>8531.0</td>
      <td>253.0</td>
      <td>273.0</td>
      <td>8258.0</td>
      <td>8005.0</td>
      <td>2.965655</td>
    </tr>
  </tbody>
</table>

Finalement, la fonction **basic_inf_summary(...)** va être utilisée pour afficher un sommaire des nombres de cas confirmé, rétabli, mort, actif et fermée dans le monde.

```python
dp.basic_inf_summary(summary_df)  
```
<p><strong>Basic Information:</strong><br>
    Total number of Confirmed cases around the world  50395174.0<br>
    Total number of Recovered cases around the world  33032762.0<br>
    Total number of Deaths cases around the world  1256177.0<br>
    Total number of Active cases around the world  16074451.0<br>
    Total number of Closed cases around the world  34282025.0<br>

#### 1.2.2. Prétraitement des données des Pays:
<p align="justify">
Pour rendre la manipulation des bases de données <strong>death_df, confirmed_df et recovered_df</strong> plus simple, on va créer un dictionnaire de ses bases de données. Pour ce faire, on va utiliser la fonction <strong>creat_dict_df(…)</strong> qui va créer un dictionnaire à partir des bases de données reçues en paramètre, avec leurs noms respectifs comme clés.</p>

```python
dict_df = dp.creat_dict_df(death_df,confirmed_df,recovered_df)
print(dict_df["Confirmed"].iloc[:,-9:])
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10/30/20</th>
      <th>10/31/20</th>
      <th>11/1/20</th>
      <th>11/2/20</th>
      <th>11/3/20</th>
      <th>11/4/20</th>
      <th>11/5/20</th>
      <th>11/6/20</th>
      <th>11/7/20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41334</td>
      <td>41425</td>
      <td>41501</td>
      <td>41633</td>
      <td>41728</td>
      <td>41814</td>
      <td>41935</td>
      <td>41975</td>
      <td>42033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20634</td>
      <td>20875</td>
      <td>21202</td>
      <td>21523</td>
      <td>21904</td>
      <td>22300</td>
      <td>22721</td>
      <td>23210</td>
      <td>23705</td>
    </tr>
    <tr>
      <th>2</th>
      <td>57651</td>
      <td>57942</td>
      <td>58272</td>
      <td>58574</td>
      <td>58979</td>
      <td>59527</td>
      <td>60169</td>
      <td>60800</td>
      <td>61381</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4665</td>
      <td>4756</td>
      <td>4825</td>
      <td>4888</td>
      <td>4910</td>
      <td>5045</td>
      <td>5135</td>
      <td>5135</td>
      <td>5319</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10558</td>
      <td>10805</td>
      <td>11035</td>
      <td>11228</td>
      <td>11577</td>
      <td>11813</td>
      <td>12102</td>
      <td>12223</td>
      <td>12335</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>263</th>
      <td>53075</td>
      <td>53520</td>
      <td>54060</td>
      <td>54775</td>
      <td>55408</td>
      <td>56090</td>
      <td>56672</td>
      <td>57226</td>
      <td>57657</td>
    </tr>
    <tr>
      <th>264</th>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>265</th>
      <td>2062</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2063</td>
      <td>2067</td>
      <td>2070</td>
    </tr>
    <tr>
      <th>266</th>
      <td>16415</td>
      <td>16432</td>
      <td>16480</td>
      <td>16543</td>
      <td>16661</td>
      <td>16698</td>
      <td>16770</td>
      <td>16819</td>
      <td>16908</td>
    </tr>
    <tr>
      <th>267</th>
      <td>8362</td>
      <td>8367</td>
      <td>8374</td>
      <td>8389</td>
      <td>8410</td>
      <td>8427</td>
      <td>8444</td>
      <td>8471</td>
      <td>8498</td>
    </tr>
  </tbody>
</table>

<p align="justify">
Les colonnes Province/State, Lat et Long, ne nous seront pas utiles. Afin de garder que les données qui vont être utiles pour notre analyse, on va utiliser la fonction <strong>dict_remove_col(...)</strong>, qui va supprimer ses colonnes du dictionnaire dict_df, les colonnes doivent être supprimées de l’ensemble des clés du dictionnaire.</p>

```python
dict_df = dp.dict_remove_col(dict_df, ["Province/State","Lat","Long"])
print(dict_df["Deaths"].iloc[:,-9:])
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10/30/20</th>
      <th>10/31/20</th>
      <th>11/1/20</th>
      <th>11/2/20</th>
      <th>11/3/20</th>
      <th>11/4/20</th>
      <th>11/5/20</th>
      <th>11/6/20</th>
      <th>11/7/20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1533</td>
      <td>1536</td>
      <td>1536</td>
      <td>1541</td>
      <td>1544</td>
      <td>1548</td>
      <td>1554</td>
      <td>1554</td>
      <td>1556</td>
    </tr>
    <tr>
      <th>1</th>
      <td>502</td>
      <td>509</td>
      <td>518</td>
      <td>527</td>
      <td>532</td>
      <td>536</td>
      <td>543</td>
      <td>549</td>
      <td>557</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1956</td>
      <td>1964</td>
      <td>1973</td>
      <td>1980</td>
      <td>1980</td>
      <td>1999</td>
      <td>2011</td>
      <td>2024</td>
      <td>2036</td>
    </tr>
    <tr>
      <th>3</th>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
      <td>75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>279</td>
      <td>284</td>
      <td>286</td>
      <td>289</td>
      <td>291</td>
      <td>296</td>
      <td>299</td>
      <td>300</td>
      <td>303</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>263</th>
      <td>481</td>
      <td>483</td>
      <td>489</td>
      <td>493</td>
      <td>501</td>
      <td>504</td>
      <td>508</td>
      <td>511</td>
      <td>512</td>
    </tr>
    <tr>
      <th>264</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>265</th>
      <td>599</td>
      <td>599</td>
      <td>600</td>
      <td>601</td>
      <td>601</td>
      <td>601</td>
      <td>601</td>
      <td>602</td>
      <td>602</td>
    </tr>
    <tr>
      <th>266</th>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
      <td>349</td>
    </tr>
    <tr>
      <th>267</th>
      <td>242</td>
      <td>243</td>
      <td>243</td>
      <td>245</td>
      <td>246</td>
      <td>248</td>
      <td>248</td>
      <td>250</td>
      <td>251</td>
    </tr>
  </tbody>
</table>

<p align="justify">
Afin de faire une observation en fonction des pays, il nous faut regrouper le dictionnaire dict_df en fonction des pays pour toutes les clés du dictionnaire. Pour cela on va utiliser la fonction <strong>dict_by_country(...)</strong>. La fonction <strong>dict_by_country(...)</strong> change aussi les colonnes des dates en séries temporelles.</p>

```python
dict_df_by_country = dp.dict_by_country(dict_df)
print(dict_df_by_country["Recovered"].iloc[:,-9:])
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2020-10-30</th>
      <th>2020-10-31</th>
      <th>2020-11-01</th>
      <th>2020-11-02</th>
      <th>2020-11-03</th>
      <th>2020-11-04</th>
      <th>2020-11-05</th>
      <th>2020-11-06</th>
      <th>2020-11-07</th>
    </tr>
    <tr>
      <th>Country/Region</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>34258</td>
      <td>34321</td>
      <td>34326</td>
      <td>34342</td>
      <td>34355</td>
      <td>34362</td>
      <td>34440</td>
      <td>34440</td>
      <td>34446</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>11097</td>
      <td>11189</td>
      <td>11246</td>
      <td>11367</td>
      <td>11473</td>
      <td>11578</td>
      <td>11696</td>
      <td>11861</td>
      <td>12002</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>40014</td>
      <td>40201</td>
      <td>40395</td>
      <td>40577</td>
      <td>40577</td>
      <td>41001</td>
      <td>41244</td>
      <td>41510</td>
      <td>41783</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>3377</td>
      <td>3475</td>
      <td>3475</td>
      <td>3548</td>
      <td>3627</td>
      <td>3734</td>
      <td>3858</td>
      <td>3858</td>
      <td>4043</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>4107</td>
      <td>4523</td>
      <td>4920</td>
      <td>5172</td>
      <td>5230</td>
      <td>5266</td>
      <td>5350</td>
      <td>5626</td>
      <td>5647</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>West Bank and Gaza</th>
      <td>45896</td>
      <td>46309</td>
      <td>46773</td>
      <td>47169</td>
      <td>47744</td>
      <td>48224</td>
      <td>48680</td>
      <td>49537</td>
      <td>49975</td>
    </tr>
    <tr>
      <th>Western Sahara</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>1366</td>
      <td>1366</td>
      <td>1366</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
      <td>1375</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>15600</td>
      <td>15680</td>
      <td>15733</td>
      <td>15733</td>
      <td>15763</td>
      <td>15819</td>
      <td>15827</td>
      <td>15862</td>
      <td>15873</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>7884</td>
      <td>7894</td>
      <td>7927</td>
      <td>7939</td>
      <td>7942</td>
      <td>7967</td>
      <td>7975</td>
      <td>7983</td>
      <td>7995</td>
    </tr>
  </tbody>
</table>


Finalement, on va ajouter la colonne Active pour l’ensemble des clés du dictionnaire dict_df_by_country. Pour cela on va utiliser la fonction <strong>dict_add_key(...)</strong>.

```python
dict_df_by_country = dp.dict_add_key(dict_df_by_country)
print(dict_df_by_country["Active"].iloc[:,-9:])
```
<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2020-10-30</th>
      <th>2020-10-31</th>
      <th>2020-11-01</th>
      <th>2020-11-02</th>
      <th>2020-11-03</th>
      <th>2020-11-04</th>
      <th>2020-11-05</th>
      <th>2020-11-06</th>
      <th>2020-11-07</th>
    </tr>
    <tr>
      <th>Country/Region</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>5543</td>
      <td>5568</td>
      <td>5639</td>
      <td>5750</td>
      <td>5829</td>
      <td>5904</td>
      <td>5941</td>
      <td>5981</td>
      <td>6031</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>9035</td>
      <td>9177</td>
      <td>9438</td>
      <td>9629</td>
      <td>9899</td>
      <td>10186</td>
      <td>10482</td>
      <td>10800</td>
      <td>11146</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>15681</td>
      <td>15777</td>
      <td>15904</td>
      <td>16017</td>
      <td>16422</td>
      <td>16527</td>
      <td>16914</td>
      <td>17266</td>
      <td>17562</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>1213</td>
      <td>1206</td>
      <td>1275</td>
      <td>1265</td>
      <td>1208</td>
      <td>1236</td>
      <td>1202</td>
      <td>1202</td>
      <td>1201</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>6172</td>
      <td>5998</td>
      <td>5829</td>
      <td>5767</td>
      <td>6056</td>
      <td>6251</td>
      <td>6453</td>
      <td>6297</td>
      <td>6385</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>West Bank and Gaza</th>
      <td>6698</td>
      <td>6728</td>
      <td>6798</td>
      <td>7113</td>
      <td>7163</td>
      <td>7362</td>
      <td>7484</td>
      <td>7178</td>
      <td>7170</td>
    </tr>
    <tr>
      <th>Western Sahara</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>97</td>
      <td>98</td>
      <td>97</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
      <td>90</td>
      <td>93</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>466</td>
      <td>403</td>
      <td>398</td>
      <td>461</td>
      <td>549</td>
      <td>530</td>
      <td>594</td>
      <td>608</td>
      <td>686</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>236</td>
      <td>230</td>
      <td>204</td>
      <td>205</td>
      <td>222</td>
      <td>212</td>
      <td>221</td>
      <td>238</td>
      <td>252</td>
    </tr>
  </tbody>
</table>


<p align="justify">
Aussi, afin de faire une observation de l'évolution de la pandémie en fonction du temps, il nous faut transformer le dictionnaire dict_df en séries temporelles. Cela consistera, entre autres à transposer le dictionnaire dict_df_by_country afin d’avoir les dates en index. Pour cela, on va utiliser la fonction <strong>dict_by_day(...)</strong>.</p>

```python
dict_df_by_day = dp.dict_by_day(dict_df_by_country)
print(dict_df_by_day["Closed"].iloc[:,-9:])
```

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Country/Region</th>
      <th>Uruguay</th>
      <th>Uzbekistan</th>
      <th>Venezuela</th>
      <th>Vietnam</th>
      <th>West Bank and Gaza</th>
      <th>Western Sahara</th>
      <th>Yemen</th>
      <th>Zambia</th>
      <th>Zimbabwe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-01-22</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-01-23</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-01-24</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-01-25</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2020-01-26</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-11-03</th>
      <td>2788</td>
      <td>65389</td>
      <td>88751</td>
      <td>1104</td>
      <td>48245</td>
      <td>9</td>
      <td>1976</td>
      <td>16112</td>
      <td>8188</td>
    </tr>
    <tr>
      <th>2020-11-04</th>
      <td>2831</td>
      <td>65578</td>
      <td>89140</td>
      <td>1104</td>
      <td>48728</td>
      <td>9</td>
      <td>1976</td>
      <td>16168</td>
      <td>8215</td>
    </tr>
    <tr>
      <th>2020-11-05</th>
      <td>2875</td>
      <td>65833</td>
      <td>89520</td>
      <td>1104</td>
      <td>49188</td>
      <td>9</td>
      <td>1976</td>
      <td>16176</td>
      <td>8223</td>
    </tr>
    <tr>
      <th>2020-11-06</th>
      <td>2914</td>
      <td>65912</td>
      <td>89920</td>
      <td>1105</td>
      <td>50048</td>
      <td>9</td>
      <td>1977</td>
      <td>16211</td>
      <td>8233</td>
    </tr>
    <tr>
      <th>2020-11-07</th>
      <td>2964</td>
      <td>66131</td>
      <td>90326</td>
      <td>1105</td>
      <td>50487</td>
      <td>9</td>
      <td>1977</td>
      <td>16222</td>
      <td>8246</td>
    </tr>
  </tbody>
</table>

## Partie 2: Analyse des données:

Les bases de données sont à présent assez bien structurées on peut maintenant commencer notre analyse

### 2.1. Analyse des données mondiales:

La première analyse consiste à visualiser les dix pays les plus touchés par la Covid_19 selon le nombre de cas confirmés, mort, actif, fermé et rétabli ainsi que le taux de mortalité (utiliser la bibliothèque seaborn).

```python
wa.summary_analyse_data(summary_df_by_country)
```
![svg](Image/fig_01.svg)

La seconde analyse consiste à visualiser le pourcentage mondial des cas confirmés par pays, le pourcentage est calculé par rapport au nombre de cas confirmé dans le monde (utiliser la méthode plotly.express).

```python
wa.summary_secteur(summary_df)
```
![svg](Image/fig_02.svg)

La troisième analyse consiste à visualiser pour certains pays le nombre de cas confirmés, mort, actif, fermé et rétabli (utiliser la méthode plotly.graph_objects).

```python
wa.countries_bar(summary_df_by_country, COUNTRIES)
```
![svg](Image/fig_03.svg)

### 2.2. Analyse des données des pays:
La Covid_19 se répand dans le monde entier. L'un des meilleurs moyens de visualiser les données consiste à mapper les données sur la carte du monde. Heureusement, il est facile de créer une carte interactive comme celle ci-dessous.
```python
ca.world_map(dict_df_by_country, "Confirmed", World_PIC)
```
![](Image/Confirmed.gif)
En utilisant le dictionnaire dict_df_by_country créé précédemment, il est possible de visualiser l’évolution du nombre cumulé des cas confirmés, rétablis, morts, actif et fermé dans le monde. 
```python
ca.world_cases(dict_df_by_country)
```
![svg](Image/fig_04.svg)
Aussi, en utilisant le dictionnaire dict_df_by_date créé précédemment, il est possible de visualiser l’évolution du nombre cumulé des cas confirmés, rétablis, morts, actifs et fermés pour un certain nombre de pays sélectionner. 
```python
ca.daily_plot_countries(dict_df_by_day, COUNTRIES)
```    
<p><strong>Spain Covid_19 Statistics:</strong><br>
    Total number of Confirmed cases : 1328832<br>
    Total number of Deaths cases    : 38833<br>
    Total number of Active cases: 1139623<br>
    Total number of Closed cases: 189209<br>
    Total number of Recovered cases: 150376</p>    
<p><strong>Canada Covid_19 Statistics:</strong><br>
  Total number of Confirmed cases: 263220<br>
  Total number of Deaths cases   : 10547<br>
  Total number of Active cases   : 36335<br>
  Total number of Closed cases   : 226885<br>
  Total number of Recovered cases: 216338</p>    
<p><strong>Italy Covid_19 Statistics:*</strong><br>
  Total number of Confirmed cases: 902490<br>
  Total number of Deaths cases   : 41063<br>
  Total number of Active cases   : 532536<br>
  Total number of Closed cases   : 369954<br>
  Total number of Recovered cases: 328891</p>    
<p><strong>China Covid_19 Statistics:</strong><br>
  Total number of Confirmed cases: 91622<br>
  Total number of Deaths cases   : 4741<br>
  Total number of Active cases   : 58108<br>
  Total number of Closed cases   : 91085<br>
  Total number of Recovered cases: 86344</p>
 
![svg](Image/fig_05.svg)

Dans le cas du Covid_19, il devient intéressant de visualiser l’évolution hebdomadaire de la pandémie pour un pays. Pour cela on va utiliser le dictionnaire créé précédemment, pour créer un autre avec une évolution hebdomadaire comme index. 

```python
ca.weekly_bar(dict_df_by_day, "Canada")
```
![svg](Image/fig_06.svg)


## Partie 3: Modélisation et prévision
L'analyse terminée, il devient possible de faire une modélisation du profil de l'évolution de la Covid_19 pour un pays, et ainsi faire une projection sur l'évolution de la pandémie.

Pour cela on va commencer par la création de nos données d'entrainement, ses données vont servir à entrainer notre modèle et le rendre le plus robuste possible.

```python
country_df, train_df = fm.creat_country_data_train(dict_df_by_day, "US")
```
La seconde étape consiste à entrainer notre modèle. Pour cela on va utiliser deux algorithmes (LR: Linear Regression et SVM:Support vector machine).
```python
model_df, dic_model, dic_score = fm.train_model(train_df, ["Confirmed"])
```

  {'LR Train': 0.6795050092913221, 'SVM Train ': 0.9137934834593749}

Une fois l’entrainement de notre modèle  terminé, il devient possible de visualiser les performances de notre modélisation et de vérifier ainsi sa robustesse.
```python
fm.plot_model(country_df, model_df)
```
![svg](Image/fig_07.svg)

Après les dates pour lesquelles nous avons des données, le modèle peut naturellement être développé. Il donne une perspective possible de prédire l’évolution des cas confirmés de Covid_19.

```python
model_pred_df = fm.prediction_model(country_df, train_df, dic_model)
```

```python
fm.plot_forcasting(country_df, model_df, model_pred_df)
```
![svg](Image/fig_08.svg)

## Annexe: Guide et normes de codage
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. Vous avertis aussi si vous ne respectez pas certaines de normes de PEP8.
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)
