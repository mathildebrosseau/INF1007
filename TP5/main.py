# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import data_processing as dp
import world_wild_analysis as wa
import countries_analysis as ca
import forcasting_model as fm

COUNTRIES = ["Spain", "Canada", "Italy", "China"]
World_PIC = r"World_Map\World_Map.shp"
COLUMNS = ["Country_Region", "Confirmed", "Deaths", "Active", "Closed", "Recovered", "Mortality_Rate"]

if __name__ == '__main__':
    # Partie 1: data_processing
    add_path_1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/'
    add_path_2 = 'master/csse_covid_19_data/csse_covid_19_time_series/'
    add_death_df = add_path_1 + add_path_2 + 'time_series_covid19_deaths_global.csv'
    add_confirmed_df = add_path_1 + add_path_2 + 'time_series_covid19_confirmed_global.csv'
    add_recovered_df = add_path_1 + add_path_2 + 'time_series_covid19_recovered_global.csv'
    add_summary_df = add_path_1 + 'web-data/data/cases_country.csv'

    [death_df, confirmed_df, recovered_df, summary_df] = dp.load_df(add_death_df, add_confirmed_df,
                                                                    add_recovered_df, add_summary_df)

    print("\n Data death_df: \n", death_df.head(10))
    print("\n Data confirmed_df: \n", confirmed_df.head(10))
    print("\n Data recovered_df: \n", recovered_df.head(10))
    print("\n Data summary_df: \n", summary_df.head(10))

    summary_df = dp.summary_add_col(summary_df, "Closed", summary_df["Deaths"] + summary_df["Recovered"])
    print("\n Data summary_df: \n", summary_df.head(10))

    summary_df = dp.summary_extract_col(summary_df, COLUMNS)
    print("\n Data summary_df: \n", summary_df.head(10))

    summary_df_by_country = dp.summary_by_country(summary_df)
    print("\n Data summary_df_by_country: \n", summary_df_by_country.head(10))

    dict_df = dp.creat_dict_df(death_df, confirmed_df, recovered_df)
    print("\n Data dict_df (Confirmed): \n", dict_df["Confirmed"].head(10))

    dict_df = dp.dict_remove_col(dict_df, ["Province/State", "Lat", "Long"])
    print("\n Data dict_df (Deaths): \n", dict_df["Deaths"].head(10))

    dict_df_by_country = dp.dict_by_country(dict_df)
    print("\n Data dict_df (Recovered): \n", dict_df_by_country["Recovered"].head(10))

    dict_df_by_country = dp.dict_add_key(dict_df_by_country)
    print("\n Data dict_df (Active): \n", dict_df_by_country["Active"].head(10))

    dict_df_by_day = dp.dict_by_day(dict_df_by_country)
    print("\n Data dict_df (Closed): \n", dict_df_by_day["Closed"].head(10))

    dp.basic_inf_summary(summary_df)

    # Partie 2.1: world_wild_analysis
    wa.summary_analyse_data(summary_df_by_country)

    wa.summary_secteur(summary_df)

    wa.countries_bar(summary_df_by_country, COUNTRIES)

    # Partie 2.2: countries_analysis
    #ca.world_map(dict_df_by_country, "Confirmed", World_PIC)

    ca.world_cases(dict_df_by_country)

    ca.daily_plot_countries(dict_df_by_day, COUNTRIES)

    ca.weekly_bar(dict_df_by_day, "US")

    # Partie 3: forcasting_model
    country_df, train_df = fm.creat_country_data_train(dict_df_by_day, "US")
    print("\nData country_df: \n", country_df)
    print("\nData train_df: \n", train_df)

    model_df, dic_model, dic_score = fm.train_model(train_df, ["Confirmed"])

    fm.plot_model(country_df, model_df)

    model_pred_df = fm.prediction_model(country_df, train_df, dic_model)

    fm.plot_forcasting(country_df, model_df, model_pred_df)
