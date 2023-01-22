import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

# scores = titles[titles["type"] == "SHOW"]["imdb_score"].dropna()
# plt.hist(scores, np.arange(0, 10.2, 0.2))
#
# scores = titles[titles["type"] == "MOVIE"]["imdb_score"].dropna()
# plt.hist(scores, np.arange(0, 10.2, 0.2))

# titles[titles["type"] == "SHOW"]["imdb_score"].plot.hist(bins=np.arange(0, 10.2, 0.2))
# titles[titles["type"] == "MOVIE"]["imdb_score"].plot.hist(bins=np.arange(0, 10.2, 0.2))
plt.figure(figsize=(16, 10))
sns.histplot(titles, x="imdb_score", bins=np.arange(0, 10.2, 0.2), hue="type")

# mean1 = titles[titles["type"] == "SHOW"]["imdb_score"].mean()
# mean2 = titles[titles["type"] == "MOVIE"]["imdb_score"].mean()
# print(f"Show's avarage:", mean1, "Movie's avarage:", mean2)

print(titles.groupby(by=["type"])["imdb_score"].mean())
# bins
# data["imdb_score"].hist()

plt.show()
pass
