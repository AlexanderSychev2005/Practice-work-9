import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

data = titles.sort_values(by="imdb_score", ascending=False).dropna().head(1000)
genres = {}

for i in data['genres']:
    nocomma = i.replace(',', '')
    no_marks = nocomma.replace("'", '')
    no_par = no_marks.strip("[]").split(' ')
    for genre in no_par:
        if genre == '':
            genre = 'none'
        if genre not in genres.keys():
            genres[genre] = 0

        genres[genre] += 1

data_genre = pd.DataFrame(({'genres': genres.keys(), 'number_of_pr': genres.values()}))

x = plt.barh(data_genre['genres'], data_genre['number_of_pr'])
plt.xlabel('number of show and movies')
plt.ylabel('genres')
plt.tight_layout()

for i in x.patches:
    plt.text(i.get_width(), i.get_y() + 0.2,
             str(round((i.get_width()), 2)),
             fontsize=8, color='black', ha='left', va='baseline')
plt.show()
