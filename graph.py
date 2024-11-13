import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C://Users/shara/Desktop/python/matches.csv")
matches_per_season = data.groupby.('Venue').size().reset_index(name='matches_per_season')
print(matches_per_season)

plt.bar(matches_per_season['Venue'],matches_per_season['Match_Count'])
plt.xlabel('Venue')
plt.ylabel('Number of Matches')
plt.title('Number of Matches in Each Venue')
plt.show()
