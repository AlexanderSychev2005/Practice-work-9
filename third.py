import pandas as pd
import matplotlib.pyplot as plt

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

years = titles[titles['release_year'] > 1999]
years_values = years[years['imdb_score'] >=8.0]
years_group = years.groupby(by='release_year')['release_year'].count().sort_index()
years_score = years_values.groupby(by="release_year")['imdb_score'].count().sort_values()
dataframe = pd.DataFrame({'lab': years_group.keys(), 'val': ((years_score / years_group)*100)})

list_bar = plt.bar(x=dataframe["lab"], height=dataframe['val'])
list_bar[int(dataframe['lab'][dataframe['val'] == max(dataframe['val'])]) - 2000].set_facecolor('pink')
plt.show()