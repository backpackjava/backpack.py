import numpy as np
import pandas as pd

menu_data = pd.read_csv("~/Python Projects VSCode/BWSIX intro to data science data/menu.csv")

# What are the top three highest calorie foods?

# list_of_cals = (list(menu_data.loc[:,"calories"]))
# values = []
# for i in range(3):
#     values.append(max(list_of_cals))
#     list_of_cals.remove(max(list_of_cals))
# for i in range(3):
#     print(list((menu_data[menu_data.calories == values[i]]).loc[:, "item"]))

# OR

largest_three = menu_data.nlargest(3, "calories")
print(list(largest_three.loc[:, "item"]))

# Which items have less than 1000 calories and cost less than $15?

low_cal = menu_data.calories < 1000
cheap = menu_data.price < 15
cheap_and_low_cal = list((menu_data[low_cal & cheap]).loc[:, "item"])

print(cheap_and_low_cal)
