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

barWidth = 0.25

# set height of bar
bars1 = [l[0] for l in list(o_counts.values())]
bars2 = [l[1] for l in list(o_counts.values())]
bars3 = [l[2] for l in list(o_counts.values())]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='green', width=barWidth, edgecolor='white', label='Positive', hatch='\\')
plt.bar(r2, bars2, color='grey', width=barWidth, edgecolor='black', label='Neutral')
plt.bar(r3, bars3, color='red', width=barWidth, edgecolor='black', label='Negative', hatch='\\')

# plt.ylim(0, 18)
# Add xticks on the middle of the group bars
plt.xlabel('Year')
plt.ylabel('Number of Songs')
plt.xticks([r + barWidth for r in range(len(bars1))], list(o_counts.keys()), rotation=45)
plt.yticks(np.arange(min(bars1), max(bars1)+1, 2.0))

plt.title('Mentions of Donald Trump in Rap Songs by Sentiment')
plt.legend()
plt.tight_layout()
plt.show()
