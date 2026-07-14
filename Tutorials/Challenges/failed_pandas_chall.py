import numpy as np
import pandas as pd

state_populations_url = 'https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv'
state_populations = pd.read_csv(state_populations_url)
state_abbrevs_url = 'https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-abbrevs.csv'
state_abbrevs = pd.read_csv(state_abbrevs_url)
state_areas_url = 'https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-areas.csv'
state_areas = pd.read_csv(state_areas_url)

# Compute the total population of the entire united states, as well as its population density for each year.
state_populations['USA totals'] = state_populations.loc[np.where((state_populations['ages'] == 'total') & (state_populations['state/region'] == 'USA')), 'population']
state_populations = state_populations.loc[((state_populations['ages'] == 'total') & ((state_populations['state/region'] == 'USA'))) ]
state_populations = state_populations.drop('state/region',axis=1).drop('population',axis=1).reset_index().sort_values(ascending = False, by='USA totals').reset_index()
# print(state_populations)

total_area = np.sum(state_areas['area (sq. mi)'])

densities = state_populations.loc[:,state_populations['USA totals']]/total_area
print(densities)

# Sort the states by population density.

# What year saw the biggest change in population for the US as a whole?

# Which states had the biggest percentage change in population in that year?

# state_densities = state_populations.loc[np.where((state_populations['year'] == '2012') & (state_populations['ages'] == 'total')), 'population']

