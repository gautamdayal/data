import pandas as pd

with open('../data/bechdel/movies.csv', 'r') as f:
    bechdel_data = pd.read_csv(f)

with open('disney_movies.csv', 'r') as f:
    disney_data = pd.read_csv(f)

print(disney_data.head())
