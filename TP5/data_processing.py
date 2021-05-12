import pandas as pd


def load_df(add_death_df, add_confirmed_df, add_recovered_df, add_summary_df):
    # TO DO: Lire les bases de données à partir des liens URL reçus en paramètres
    death_df = pd.read_csv(add_death_df)
    confirmed_df = pd.read_csv(add_confirmed_df)
    recovered_df = pd.read_csv(add_recovered_df)
    summary_df = pd.read_csv(add_summary_df)
    return death_df, confirmed_df, recovered_df, summary_df


def summary_add_col(df, col, value):
    # TO DO: Ajouter une colonne à la base de données df reçue en paramètre (deux lignes)
    # le nom et la valeur de cette colonne se trouvent respectivement dans les variables col et value.
    df[col] = value
    return df


def summary_extract_col(df, cols):
    # TO DO: Extraire les colonnes reçues en paramètre désirer de la base de données df (une seul ligne)
    return df[cols]


def summary_by_country(df):
    # TO DO: Grouper le DataFrame par Country_Region (une seule ligne). Utiliser la méthode groupby()
    return df.groupby(by="Country_Region").sum()


def creat_dict_df(death_df, confirmed_df, recovered_df):
    # TODO: Créer un dictionnaire avec des bases de données reçues en paramètre (une seule ligne)
    return {"Deaths": death_df, "Confirmed": confirmed_df, "Recovered": recovered_df}


def dict_remove_col(dict_df, cols):
    # TO DO: Supprimer des colonnes cols du dictionnaire dict_df (une seule ligne) 
    # les colonnes doivent être supprimées de l’ensemble des clés du dictionnaire
    return {key: dict_df[key].drop(columns=cols) for key in dict_df.keys()}


def dict_by_country(dict_df):
    # TO DO: Grouper le dictionnaire dict_df par Country/Region pour toutes les clés du dictionnaire 
    # et changer les colonnes en datetime, utiliser le lien suivant pour plus d'information
    # https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.to_datetime.html
    for key in dict_df.keys():
        dict_df[key] = dict_df[key].groupby(by="Country/Region").sum()
        dict_df[key].columns = pd.to_datetime(dict_df[key].columns)
    return dict_df


def dict_add_key(dict_df):
    # TO DO: Ajouter les clés Active case et Closed Case a votre dictionnaire de DataFrame
    # les cles du dictionnaire doivent être triés comme suit:{"Confirmed", "Deaths", "Active", "Closed", "Recovered"}
    nouveau_dict_df = dict()
    nouveau_dict_df["Confirmed"] = dict_df["Confirmed"]
    nouveau_dict_df["Deaths"] = dict_df["Deaths"]
    nouveau_dict_df["Active"] = dict_df["Confirmed"] - (dict_df["Deaths"] + dict_df["Recovered"])
    nouveau_dict_df["Closed"] = dict_df["Deaths"] + dict_df["Recovered"]
    nouveau_dict_df["Recovered"] = dict_df["Recovered"]
    return nouveau_dict_df


def dict_by_day(dict_df):
    # TO DO: Grouper le dictionnaire de DataFrame par date (une seule ligne)
    # Utiliser le lien suivant:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html
    return {key: dict_df[key].transpose() for key in dict_df.keys()}


def basic_inf_summary(summary_df):
    # TO DO: Afficher les informations suivantes: Somme des nombres de cas confirmé,
    # active, fermée, mort et rétabli dans le monde.

    colonnes = ["Confirmed", "Recovered", "Deaths", "Active", "Closed"]

    for col in colonnes:
        somme_colonnes = summary_df[col].sum()
        print("Total number of " + col + " cases around the world {}".format(format(somme_colonnes, '0.1f')))
