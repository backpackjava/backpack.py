import numpy as np
import matplotlib.pyplot as mpl
import pandas as pd

x,y = np.loadtxt("C:/Users/rad11/Python Projects VSCode/BWSIX intro to data science data/poly_data.txt", unpack = True)


degree = 9 # overfitting error minimum =3 
line_obf = np.polyval(np.polyfit(x,y,degree),x)
error = line_obf - y
mean_error = (abs(error)).mean()

print(mean_error)
mpl.plot(x,line_obf, 'r-')
mpl.scatter(x,y)
mpl.show()