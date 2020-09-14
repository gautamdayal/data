import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('../data/bechdel/movies.csv', 'r') as f:
    bechdel_data = pd.read_csv(f)

with open('disney_movies.csv', 'r') as f:
    disney_data = pd.read_csv(f)

# print(bechdel_data.head())
# print(disney_data.head())
disney_movies = list(disney_data['movie_title'])
years = {}

for movie in list(bechdel_data['code']):
    year = int(movie[:4])
    test = movie[4:]
    if year not in years:
        years[year]=[0, 0]
    if test == 'PASS':
        years[year][0] += 1
    else:
        years[year][1] += 1

year_names = [year for year in years]
passes = [years[movie][0] for movie in years]
fails = [years[movie][1] for movie in years]
N = len(year_names)

ind = np.arange(N)
width = 0.35
plt.bar(ind, passes, width, label='Pass')
plt.bar(ind + width, fails, width,
    label='Fail')

plt.ylabel('Number')
plt.title('Movies that passed the Bechdel Test')

plt.xticks(ind + width / 2, year_names, rotation=45)
plt.legend(loc='best')
plt.show()
