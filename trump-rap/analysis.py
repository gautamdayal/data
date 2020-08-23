import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

with open('../data/hip-hop-candidate-lyrics/genius_hip_hop_lyrics.csv', 'r', errors='ignore') as f:
    data = pd.read_csv(f)

# Each element is a list in the form [candidate, sentiment, year]
sentiments = []
for i in range(len(data)):
    sentiments.append([data['candidate'][i], data['sentiment'][i], data['album_release_date'][i]])

trump_sentiments = [l for l in sentiments if l[0]=='Donald Trump']
counts = {}
for l in trump_sentiments:
    year = l[2]
    if year not in counts:
        counts[year]=[0, 0, 0]
    if l[1] == 'positive':
        counts[year][0] += 1
    elif l[1] == 'neutral':
        counts[year][1] += 1
    elif l[1] == 'negative':
        counts[year][2] += 1

o_counts = collections.OrderedDict(sorted(counts.items()))

plt.style.use('fivethirtyeight')
plt.plot(list(o_counts.keys()), [l[0] for l in list(o_counts.values())], label='positive')
plt.plot(list(o_counts.keys()), [l[1] for l in list(o_counts.values())], label='neutral')
plt.plot(list(o_counts.keys()), [l[2] for l in list(o_counts.values())], label='negative')
plt.legend()
plt.title('Mentions of Donald Trump in Hip-Hop')
plt.show()
