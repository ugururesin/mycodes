# =============================================================================
# PYTHON Box Plots
# =============================================================================

# DESCRIPTION
#Generally used for QUANtitative variable vs. QUALitative variable
#(Same with Violin Plots)
#Gives min(Q0), Q1, median(Q2), Q3, max(Q4)
#IQR = Q3-Q1
#"Upper Whisker Bound" = Q3 + 1.5*IQR

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
path="/Users/UGUR/Desktop/mycodes/data"
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
sb.boxplot(data = fuel_econ, x = 'VClass', y = 'comb', color = base_color);
plt.xticks(rotation = 15)

# For HORIZONTAL BOX-PLOTS (Change x & y)
sb.boxplot(data = fuel_econ, y = 'VClass', x = 'comb', color = base_color);

## ADDITIONS
plt.figure(figsize = [10, 5])
base_color = sb.color_palette()[0]

# left plot: violin plot
plt.subplot(1, 2, 1)
ax1 = sb.violinplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)

# right plot: box plot
plt.subplot(1, 2, 2)
sb.boxplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot
###