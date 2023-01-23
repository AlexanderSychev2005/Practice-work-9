import pandas as pd

credits = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

merged_data = pd.merge(titles.sort_values(by="imdb_score", ascending=False).head(1000), credits[credits["role"] == "ACTOR"], how="inner", on=["id"])
merged_data_head = merged_data.groupby(by= "name")["title"].count().sort_values(ascending=False).head(10)
print(f'TOP - 10 ACTORS\n{merged_data_head.to_string(header=False)}')



