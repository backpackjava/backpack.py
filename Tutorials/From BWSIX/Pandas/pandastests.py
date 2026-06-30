import numpy as np
import pandas as pd
import matplotlib as plt

# pwd: path of working directory
# ls: list of files in current directory

x = np.genfromtxt("C:/Users/rad11/Python Projects VSCode/BWSIX intro to data science data/example_mixed_data.csv", 
               delimiter = ',', dtype = None, encoding = None)
                # delimiter is what separates each datapoint    
                # dtype is datatype. None: numpy figures it our for us
                # encoding
y = np.genfromtxt("C:/Users/rad11/Python Projects VSCode/BWSIX intro to data science data/example_mixed_data.csv", 
               delimiter = ',')
                # genfromtxt with no dtype or encoding makes numpy default to reading number values: all other dtypes are NaN

staff_data = pd.read_csv("C:/Users/rad11/Python Projects VSCode/BWSIX intro to data science data/fall2024_python_staff.csv")

using_label = staff_data.loc[4, "major"] # loc uses lables to locate
using_index = staff_data.iloc[4,2]      # iloc using indices to locate

first_name_column = staff_data["first_name"] # access from one column

name_columns = staff_data.loc[:, ["first_name", "last_name"]] # using loc to access specific components:
                                                            # : references all rows btw

# print(x)
# print(y)
# print(staff_data)
# print(using_label)
# print(using_index)
print(first_name_column)
print(name_columns)
print(using_label)


