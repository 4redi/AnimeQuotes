import random as rand
import pandas as pd

dataset = pd.read_csv(r'dataset/AnimeQuotes.csv')


def generate_quote():
  random_quote = dataset.sample(n=1).iloc[0]
  print(
      f"{random_quote['Quote']} \n\tsaid by {random_quote['Character']} from {random_quote['Anime']}  "
  )


generate_quote()

# focus on making it an interface instead of terminal
