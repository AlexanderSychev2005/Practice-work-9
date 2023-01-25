import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

data = titles.sort_values(by="imdb_score", ascending=False).dropna().head(1000)
genres = {}

for i in data['genres']:



plt.show()
pass