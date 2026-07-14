import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pokedex_csv = pd.read_csv("C:/Users/rad11/Python Projects VSCode/backpack.py/pokedex.csv")

print(pokedex_csv)

fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(1,2,2)

x_values = np.arange(0,len(pokedex_csv['Index']),1)
# print(len(x_values))


ax1.scatter(x_values, pokedex_csv['HP'], color='blue', label='HP')
ax1.set_title("HP of Pokemon generations 1-8")

ax2.scatter(x_values, pokedex_csv['SpAtk'], color='red', label='SpA')
ax2.set_title("SpA of Pokemon generations 1-8")

ax3.scatter(x_values, pokedex_csv['SpDef'], color='green', label='SpD')
ax3.set_title("SpD of Pokemon generations 1-8")

ax1.legend(loc='upper left', bbox_to_anchor=(1,1))
ax2.legend(loc='upper left', bbox_to_anchor=(1,1))
ax3.legend(loc='upper left', bbox_to_anchor=(1,1))

fig.tight_layout()

plt.show()