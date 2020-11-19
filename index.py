import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
import matplotlib
from matplotlib import pyplot as plt
import numpy as np


###### COVID DATA ######
# df = pd.read_csv("all-states-history.csv")
# df.sort_values(by=["state", "date"],inplace=True)
# df.fillna(0, inplace=True)
# df["dailyPositiveRate"] = (df["positiveIncrease"]/df["totalTestResultsIncrease"])
# df = df[["date", "state", "positiveIncrease", "totalTestResultsIncrease", "dailyPositiveRate"]]
# df = df[(df["date"]<="2020-11-01") & (df["date"]>="2020-06-01")]
# df = df[(df["dailyPositiveRate"] >= 0) & (df["dailyPositiveRate"] <= 1)]
# df = df[(df["state"] != "DC") & (df["state"] != "GU") & (df["state"] != "PR") & (df["state"] != "VI")]

###### POPULATION DATA ######
# pop_data = pd.read_csv("population-data.csv")
# df = pd.merge(df, pop_data)
# print(df.tail())
# df = df.drop(columns=["SUMLEV", "REGION", "DIVISION", "CODE","POPEST18PLUS2019"])

###### URBAN DATA ######
# percentUrban = pd.read_csv("pop-pct-urban.csv")
# df = pd.read_csv("covid-data.csv")
# df = pd.merge(df, percentUrban)

###### MASK DATA ######
#STATES DONE: ALL STATES DONE
# df.loc[((df["state"]=="WI") & (df["date"] >= "2020-08-01")), "statewideMaskMandate"] = 1

df = pd.read_csv("covid-data.csv")

# df.to_csv("covid-data.csv", encoding='utf-8', index=False)
