import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from datetime import timedelta
import plotly.io as pio

COLOR = ["blue", "red", "green", "gray", "orange"]


def creat_country_data_train(dict_df, country):
    # TO DO: création des données d'entrainement,
    # Étape 1: créer un DataFrame avec deux colonnes "Days Since" et "Date"

    df = pd.DataFrame(columns=["Days Since", "Date"])

    # Étape 2: Affecter a la colonne "Days Since"  l'indice de la base de données "Confirmed" du Country du
    # dictionnaire dict_df

    df["Days Since"] = dict_df["Confirmed"][country].index

    # Étape 3: convertir le contenu de la colonne "Days Since" en datetime format
    # utiliser le lien suivant: 
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day.html

    df["Days Since"] = df["Days Since"].dt.dayofyear

    # Étape 4: Affecter a la colonne "Date"  l'indice de la base de données "Confirmed" du dictionnaire dict_df

    df["Date"] = dict_df["Confirmed"].index

    # Étape 5: grouper la base de donner créer a l'étape 1 par "Date"

    df = df.groupby(by="Date").sum()

    # Étape 6: ajouter a la base de données créée a l'étape 1 toutes les données des clés du dictionnaire dict_df
    # le nom des colonnes ajoutées sera le même que celui des clés du dictionnaire dict_df

    for key in dict_df.keys():
        df[key] = dict_df[key][country].diff().fillna(0).tolist()

    # Étape 7: Générer de façon aléatoire les données d'entrainement, qui représente 75% des données.
    # utiliser le lien suivant pour plus d'information: https://www.w3schools.com/python/ref_random_choices.asp

    train_df = df.sample(frac=0.75).sort_index()

    return df, train_df


def train_model(df, data_type):
    lin_reg = LinearRegression(normalize=True)
    svm = SVR(C=100000, degree=10, epsilon=0.01)

    x = np.array(df["Days Since"]).reshape(-1, 1)
    y = np.array(df[data_type]).reshape(-1, 1)

    lin_reg.fit(x, np.ravel(y))
    svm.fit(x, np.ravel(y))

    lin_reg_predict = lin_reg.predict(x)
    svm_predict = svm.predict(x)

    model_df = pd.DataFrame(zip(df.index, lin_reg_predict, svm_predict), columns=["Dates", "LR", "SVM"])
    dic_model = {"LR": lin_reg, "SVM": svm}
    dic_score = {"LR Train": lin_reg.score(x, y), "SVM Train ": svm.score(x, y)}

    return model_df, dic_model, dic_score


def plot_model(country_df, model_df):
    # TO DO: Visualiser l’évolution du nombre des cas confirmés
    # Étape 1: Créer une figure en utilisant la bibliothèque plotly.graph_objects

    color = iter(COLOR)

    fig = go.Figure()

    # Étape 2: Tracer les courbes suivantes sur le même graphe: l'évolution des cas confirmés et SVM/LR Model

    fig.add_trace(go.Scatter(x=country_df.index, y=country_df["Confirmed"].values, mode='lines', name="Confirmed Cases",
                             line=dict(color=next(color), width=2)))
    fig.add_trace(go.Scatter(x=model_df['Dates'], y=model_df['SVM'].values, mode='lines', name="SVM Model",
                             line=dict(color=next(color), width=2)))
    fig.add_trace(go.Scatter(x=model_df['Dates'], y=model_df['LR'].values, mode='lines', name="LR Model",
                             line=dict(color=next(color), width=2)))

    fig.update_layout(xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    fig.show()
    pio.write_image(fig, 'Image/fig_07.png', width=1000, height=500)


def prediction_model(country_df, train_df, dic_model):
    new_date = []
    new_prediction_lr = []
    new_prediction_svm = []

    for i in range(1, 60):
        new_date.append(train_df.index[-1] + timedelta(days=i))
        new_prediction_lr.append(int(dic_model["LR"].predict(np.array(country_df["Days Since"].max()
                                                                      + i).reshape(-1, 1))))
        new_prediction_svm.append(int(dic_model["SVM"].predict(np.array(country_df["Days Since"].max()
                                                                        + i).reshape(-1, 1))))

    model_pred_df = pd.DataFrame(zip(new_date, new_prediction_lr, new_prediction_svm), columns=["Dates", "LR", "SVM"])

    return model_pred_df


def plot_forcasting(country_df, model_df, model_pred_df):
    # TO DO: Visualiser l’évolution du nombre des cas confirmés ainsi que
    # la projection sur l'évolution de la pandémie pour les deux prochains mois
    # Étape 1: Créer une figure en utilisant la bibliothèque plotly.graph_objects

    color = iter(COLOR)

    fig = go.Figure()

    # Étape 2: Tracer les courbes suivantes sur le même graphe l'évolution des cas confirmés,
    # SVM/LR Model et SVM/LR prédiction

    fig.add_trace(go.Scatter(x=country_df.index, y=country_df["Confirmed"].values, mode='lines', name="Confirmed Cases",
                             line=dict(color=next(color), width=2)))
    fig.add_trace(go.Scatter(x=model_df['Dates'], y=model_df['SVM'].values, mode='lines', name="SVM Model",
                             line=dict(color=next(color), width=2)))
    fig.add_trace(go.Scatter(x=model_df['Dates'], y=model_df['LR'].values, mode='lines', name="LR Model",
                             line=dict(color=next(color), width=2)))

    fig.add_trace(
        go.Scatter(x=model_pred_df['Dates'], y=model_pred_df['SVM'].values, mode="markers", name="SVM Prediction",
                   line=dict(color=next(color), width=2)))
    fig.add_trace(
        go.Scatter(x=model_pred_df['Dates'], y=model_pred_df['LR'].values, mode="markers", name="LR Prediction",
                   line=dict(color=next(color), width=2)))

    fig.update_layout(xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    fig.show()
    pio.write_image(fig, 'Image/fig_08.png', width=1000, height=500)
