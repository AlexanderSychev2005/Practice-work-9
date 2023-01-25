import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")


def figure1():
    scores = titles[titles["type"] == "SHOW"]["imdb_score"].dropna()
    figure = plt.figure(figsize=(16, 10))
    plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.xlabel("Score")
    plt.ylabel("Num titles")
    plt.title("Scores we counted SHOW")
    # plt.savefig(fname= "our_plot.png")

    # titles[titles["type"] == "SHOW"]["imdb_score"].plot.hist(bins=np.arange(0, 10.2, 0.2))
    # titles[titles["type"] == "MOVIE"]["imdb_score"].plot.hist(bins=np.arange(0, 10.2, 0.2))

    # plt.figure(figsize=(16, 10))
    # sns.histplot(titles, x="imdb_score", bins=np.arange(0, 10.2, 0.2), hue="type")


def figure2():
    scores = titles[titles["type"] == "MOVIE"]["imdb_score"].dropna()
    figure = plt.figure(figsize=(16, 10))
    plt.hist(scores, np.arange(0, 10.2, 0.2))
    plt.axvline(scores.mean(), color='k', linestyle='dashed', linewidth=1)
    plt.xlabel("Score")
    plt.ylabel("Num titles")
    plt.title("Scores we counted MOVIE")


def mean():
    print(titles.groupby(by=["type"])["imdb_score"].mean())
    mean1 = titles[titles["type"] == "SHOW"]["imdb_score"].mean()
    mean2 = titles[titles["type"] == "MOVIE"]["imdb_score"].mean()
    if mean2 > mean1:
        print("movie's average is greater")
    else:
        print("show's average is greater")


def task1():
    global titles
    step = 0.2
    column = 'imdb_score'
    imdb_min = 0
    imdb_max = 10

    bins = np.arange(imdb_min, imdb_max + step, step)
    hists = titles.hist(column=column, by='type', bins=bins, edgecolor='black', linewidth=2, xlabelsize=5)
    for hist in hists:
        hist.set_xticks(bins)
        hist.grid()


if __name__ == '__main__':
    # figure1()
    # figure2()
    task1()
    mean()
    plt.show()
    pass
