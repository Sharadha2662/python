import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C://Users/shara/Desktop/python/censes.csv")
martial_income = data.groupby('Martial Status ')['Income'].mean().reset_index()
print("Average Income by Martial Status :\n", martial_income)
fig, axs = plt.subplots(3, 2, figsize=(15, 10))
axs[0, 0].bar(martial_income['Martial Status '], martial_income['Income'])
axs[0, 0].set_title("Average Income by Martial Status ")
axs[0, 0].set_xlabel("Martial Status ")
axs[0, 0].set_ylabel("Average Income")
plt.tight_layout()
plt.show()