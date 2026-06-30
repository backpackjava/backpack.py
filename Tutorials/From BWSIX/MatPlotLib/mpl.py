import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

# x,y = np.loadtxt("C:/Users/rad11/Python Projects VSCode/BWSIX intro to data science data/linear_data.txt", unpack=True)

# def function
def f(x):
    return ((x-2)**3 + 3)
# lambda function
g = lambda x: ((x-2)**3 + 3)
h = lambda x: (x+3)

x_values = np.arange(0,4,0.2)

dataframex = pd.DataFrame(np.column_stack([x_values, f(x_values), g(x_values)]), columns = ("x", "f(x)", "g(x)"))
dataframex["h(x)"] = dataframex["x"].apply(h) # defines an h(x) column as the application of lambda function h to the column "x"
print(dataframex)

# mpl.plot(x_values,f(x_values))
mpl.plot(x_values, g(x_values))
mpl.ylabel('y')
mpl.xlabel('x')
# mpl.show()

# plotting with pandas
dataframex.plot("x", ["f(x)"])
mpl.show()
