import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def summary_analyse_data(df):
    # TO DO: plot the 10 countries with the highest number of confirmed, deaths, active, closed, recovered,
    # and mortality rate
    # Étape 1: Créer des subfigure de 3 lignes et 2 colonnes de dimension 15*15 en utilisant la bibliothèque matplotlib
    # https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

    fig, ((axe1, axe2), (axe3, axe4), (axe5, axe6)) = plt.subplots(3, 2, figsize=(15, 15))

    # Étape 2:  dessiner sur chaque subplot les 10 pays les plus touchés par la Covid_19 selon le nombre de cas
    # confirmés, mort, actif, fermé et rétabli ainsi que le taux de mortalité en utilisant la bibliothèque seaborn.
    # https://seaborn.pydata.org/generated/seaborn.barplot.html

    col_liste = ['Confirmed', 'Deaths', 'Active', 'Closed', 'Recovered', 'Mortality_Rate']
    axes_liste = [axe1, axe2, axe3, axe4, axe5, axe6]

    for i in range(len(col_liste)):
        sns.barplot(ax=axes_liste[i], x=df[col_liste[i]].nlargest(10).values, y=df[col_liste[i]].nlargest(10).index)
        axes_liste[i].set(xlabel=f"Number of {col_liste[i]} cases", ylabel="Country",
                          title=f"Top 10 countries as per number of {col_liste[i]} cases")

    fig.tight_layout(pad=3.0)
    plt.savefig('Image/fig_01.png', dpi=600, format='png')
    fig.show()


def summary_secteur(df):
    # TO DO: Plot le pourcentage mondial des cas confirmés par pays
    # Étape 1: Créer une base de données avec les pays qui ont un pourcentage de cas confirmés
    # supérieur ou égal à 2% des nombres de cas confirmés dans le monde.
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

    nombre_total = df["Confirmed"].sum()
    deux = 0.02 * nombre_total
    grosse_df = df.loc[df["Confirmed"] >= deux]

    # Étape 2: Créer une base de données avec les pays qui ont un pourcentage de cas confirmé
    # inférieur à 2% des nombres de cas confirmé dans le monde.
    # Cette base de données doit contenir une seule ligne représentant la somme de tous les cas
    # dans les pays ayant un pourcentage de cas confirmé inférieur à 2% dont le nom sera "Others"
    # https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/

    donnees = [["Others", df["Confirmed"].sum() - grosse_df["Confirmed"].sum()]]
    petite_df = pd.DataFrame(donnees, columns=["Country_Region", "Confirmed"])

    # Étape 3: Concaténer les deux bases de données créées précédemment
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

    dataframes = [grosse_df, petite_df]
    nouvelle_df = pd.concat(dataframes)

    # Étape 4: Dessiner le pourcentage mondial des cas confirmés par pays en utilisant la bibliothèque plotly.express
    # https://plotly.com/python/pie-charts/

    fig = px.pie(nouvelle_df, values='Confirmed', names='Country_Region', title='Confirmed', hole=.4,
                 color_discrete_sequence=px.colors.sequential.RdBu)

    fig.update_traces(textposition="inside")
    fig.show()
    pio.write_image(fig, 'Image/fig_02.png', width=1000, height=500)


def countries_bar(df, countries):
    # TO DO: plot pour certains pays le nombre de cas confirmés, morts, actifs, fermés et rétablis
    # Étape 1: extraire les données des pays reçus en paramètre

    countries = sorted(countries)
    df = df.loc[countries]

    # Étape 2: TO DO: Retirer la colonne "Mortality_Rate"

    df = df.drop(columns="Mortality_Rate")

    # Étape 3: Créer une figure en utilisant la bibliothèque plotly.graph_objects
    # https://plotly.com/python/subplots/

    fig = go.Figure()

    for country in df:
        fig.add_trace(go.Bar(x=df[country].index, y=df[country].values, name=country))

    fig.update_layout(yaxis=dict(title='Cases', titlefont_size=16, tickfont_size=14),
                      xaxis=dict(title=None, tickfont_size=14), barmode='group', bargap=0.15, bargroupgap=0.1,
                      legend=dict(x=0.01, y=0.99, title=None), legend_orientation="h")
    fig.show()
    pio.write_image(fig, 'Image/fig_03.png', width=1000, height=500)
