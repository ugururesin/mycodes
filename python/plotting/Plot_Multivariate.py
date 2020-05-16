# =============================================================================
# PYTHON Multivariate Visualization
# =============================================================================

## LIBRARY IMPORT
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
#%matplotlib.inline #to produce plots in Jupyter NB
import os

## WORKING DIRECTORY
os.getcwd()     #TO GET CURRENT WD
#
path="/Users/UGUR/Desktop/mycodes/_master/data"
os.chdir(path)  #TO SET THE PATH AS WD


## DATA-1
fuel_econ = pd.read_csv('fuel_econ.csv')
fuel_econ.head(3)
#
sedan_class = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars',
               'Midsize Cars', 'Large Cars']
vclasses = pd.api.types.CategoricalDtype(ordered=True, categories=sedan_class)
fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses);
fuel_econ['trans_type'] = fuel_econ['trans'].apply(lambda x: x.split()[0])
#

## DATA-2
url = 'https://raw.githubusercontent.com/udacity/AIPND/master/Matplotlib/data/pokemon.csv'
response = requests.get(url)
response #returns 200 if it's successful
#
with open('pokemon.csv', mode='wb') as file: #wb:write binary
    file.write(response.content)
    file.close()
pokemon = pd.read_csv('pokemon.csv')
#

#1
np.random.seed(2018)
sample = np.random.choice(fuel_econ.shape[0], 200, replace=True)
fuel_econ_subset = fuel_econ.loc[sample]
#
sb.regplot(data = fuel_econ_subset, x='displ', y='comb',
           x_jitter=0.04, fit_reg=False);
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)');