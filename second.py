import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

values = titles[titles["type"] == "SHOW"]["age_certification"].dropna()
labels, values = np.unique(values, return_counts=True)
plt.figure(figsize=(16, 10))
plt.pie(values, labels=labels)

plt.show()
