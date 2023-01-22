import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

merged_data = pd.merge(titles.sort_values(by="imdb_score", ascending=False).head(1000), credits[credits["role"] == "ACTOR"], how="inner", on=["id"])
print(merged_data.groupby(by= "name")["title"].count().sort_values(ascending=False).head(10))

