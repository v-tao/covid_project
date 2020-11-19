import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("covid-data.csv")
df.drop(columns=["date","state","positiveIncrease","totalTestResultsIncrease"], inplace=True)
labels = df.iloc[:, 0].to_numpy()
df = (df-df.min())/(df.max()-df.min())
features = df.iloc[:, 1:].to_numpy()
feature_names = ["population", "percentOver18", "percentUrban", "statewideMaskMandate"]
poly_features = PolynomialFeatures(2).fit_transform(features)
model = LinearRegression().fit(poly_features, labels)
score = model.score(poly_features, labels)
f = open("model_scores.csv", "a")
f.write(str(score))
f.write(",")
f.close()