# =============================================================================
# PYTHON Violin Plots
# =============================================================================

# DESCRIPTION
#Generally used for QUANtitative variable vs. QUALitative variable
#Instead of plotting data points individually,
#We have a curve for each level of categorical variable.
#Where curve is wider, there are more data points!
#BOX-PLOTS are mostly used instead of Violin-Plots

## LIBRARY IMPORT
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
#%matplotlib.inline #to produce plots in Jupyter NB
import os

## FORMAT
plt.scatter(data = df, x = 'num_var1', y = 'num_var2')  #Matplotlib's scatter
sb.regplot(data = df, x = 'num_var1', y = 'num_var2')   #Seaborn (w regression)

## WORKING DIRECTORY
os.getcwd()     #TO GET CURRENT WD
#
path="/Users/UGUR/Desktop/mycodes/_master/data"
os.chdir(path)  #TO SET THE PATH AS WD

## EXAMPLE DATA
fuel_econ = pd.read_csv('fuel_econ.csv')
fuel_econ.head(3)
#
sedan_class = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars',
               'Midsize Cars', 'Large Cars']
vclasses = pd.api.types.CategoricalDtype(ordered=True, categories=sedan_class)
fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses);
#
base_color = sb.color_palette()[0]
sb.violinplot(data = fuel_econ, x = 'VClass', y = 'comb',
              color = base_color, inner = None); #or inner = 'quartile'
plt.xticks(rotation = 15)
###