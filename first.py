import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")
def figure1():

    scores = titles[titles["type"] == "SHOW"]["imdb_score"].dropna()
    figure= plt.figure(figsize=(16, 10))
    plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.xlabel("Score")
    plt.ylabel("Num titles")
    plt.title("Scores we counted SHOW")
    #plt.savefig(fname= "our_plot.png")

    # titles[titles["type"] == "SHOW"]["imdb_score"].plot.hist(bins=np.arange(0, 10.2, 0.2))
    # titles[titles["type"] == "MOVIE"]["imdb_score"].plot.hist(bins=np.arange(0, 10.2, 0.2))

    # plt.figure(figsize=(16, 10))
    # sns.histplot(titles, x="imdb_score", bins=np.arange(0, 10.2, 0.2), hue="type")

    # mean1 = titles[titles["type"] == "SHOW"]["imdb_score"].mean()
    # mean2 = titles[titles["type"] == "MOVIE"]["imdb_score"].mean()
    # print(f"Show's avarage:", mean1, "Movie's avarage:", mean2)

    print(titles.groupby(by=["type"])["imdb_score"].mean())
def figure2():
    scores = titles[titles["type"] == "MOVIE"]["imdb_score"].dropna()
    figure = plt.figure(figsize=(16, 10))
    plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.xlabel("Score")
    plt.ylabel("Num titles")
    plt.title("Scores we counted MOVIE")
if __name__ == '__main__':
    figure1()
    figure2()
    plt.show()
    pass

