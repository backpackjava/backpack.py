import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

windfield_data = gpd.read_file("C:/Users/rad11/Python Projects VSCode/backpack.py/WindField")
windfield_data.plot('GRIDCODE', legend = True)

svi_df = gpd.read_file("C:/Users/rad11/Python Projects VSCode/backpack.py/SVI2020_US_tract.gdb")

svi_df['RPL Themes']

rows, columns = windfield_data.shape
print(rows, columns)

plt.show()