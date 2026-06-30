import numpy as np
import pandas as pd
import matplotlib as mpl

staff_data = pd.read_csv("C:/Users/rad11/Python Projects VSCode/BWSIX intro to data science data/fall2024_python_staff.csv")

# sorted_staff_data = staff_data.sort_index(axis = 1)
# sorted_staff_data_2 = staff_data.sort_values(by="favorite_number") # sort by their favorite number column
# print(sorted_staff_data) # just sorted in alphabetical order by axis 1 (columns)

# sample = (staff_data.sample(3)).loc[:, ["first_name", "last_name"]]
# print(sample) # take a sample of 3 random rows, and then I specified to only take in their first and last name

# kallee_data = staff_data[staff_data.first_name == "Kallee"]
# print(kallee_data) # print Kallee's information by putting a condition on the expression

has_graduated = staff_data.graduated
has_fav_even_num = staff_data.favorite_number % 2 == 0
print(staff_data[has_graduated & has_fav_even_num])