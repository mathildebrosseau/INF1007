#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import pandas as pd
from sklearn.model_selection import train_test_split


# TODO: Définissez vos fonctions ici

def preprocess_data(data_path: str =r"./data/winequality-white.csv"):
    data_frame = pd.read_csv(data_path, ";", header=0)
    y = data_frame["quality"]
    X = data_frame.drop(columns=["quality"])

    return train_test_split(X, y, test_size=0.1)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    preprocess_data()