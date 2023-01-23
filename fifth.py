import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

data = titles.sort_values(by="imdb_score", ascending=False).dropna().head(1000)
values = data.groupby(by="genres")["title"].count().sort_values(ascending=False)
objects = values
y_pos = np.arange(len(values))
performance = [1000,900,800,700,600, 500, 400, 300, 200, 100, 0]
plt.bar(y_pos, performance, align='center')

plt.figure(figsize=(16, 10))


plt.show()
pass