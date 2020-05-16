# =============================================================================
# PLOT FACETING
# =============================================================================

# DESCRIPTION
#In faceting, the data is divided into disjoint subsets,
#most often by different levels of a categorical variable.
#For each of these subsets, the same plot type is rendered on other variables.

## LIBRARY IMPORT
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
#%matplotlib.inline #to produce plots in Jupyter NB
import os

#1 Seaborn's FacetGrid class facilitates the creation of faceted plots.
g = sb.FacetGrid(data = df, col = 'cat_var')

#2 Map method on the FacetGrid object to specify the plot type & variable(s)
#that will be plotted in each subset (in this case, histogram on "num_var").
g.map(plt.hist, "num_var")

#Notice that each subset of the data is being plotted independently.
#Each uses the default of ten bins from hist to bin together the data,
#and each plot has a different bin size.
#Despite that, the axis limits on each facet are the same to allow clear
#and direct comparisons between groups.
#It's still worth cleaning things a little bit more
#by setting the same bin edges on all facets.
#Extra visualization parameters can be set as additional keyword arguments
#to the map function.
bin_edges = np.arange(-3, df['num_var'].max()+1/3, 1/3)
g = sb.FacetGrid(data = df, col = 'cat_var')
g.map(plt.hist, "num_var", bins = bin_edges
     

## WORKING DIRECTORY
os.getcwd()     #TO GET CURRENT WD
#
path="/Users/UGUR/Desktop/mycodes/_master/data"
os.chdir(path)  #TO SET THE PATH AS WD

## EXAMPLE DATA
fuel_econ = pd.read_csv('fuel_econ.csv')
fuel_econ.head(3)
fuel_econ.VClass.unique() #There are 5 vehicle classes
#
sb.FacetGrid(data = fuel_econ, col='VClass'); #empty plot columns
#
g = sb.FacetGrid(data = fuel_econ, col='VClass'); 
g.map(plt.hist, 'comb'); #bins=10 by default
#
bins = np.arange(12, 58+2, 2)
g = sb.FacetGrid(data = fuel_econ, col='VClass',
                 col_wrap=3,    #3 plots in a row
                 sharey=False); #each facet have i's own y-axis!
g.map(plt.hist, 'comb', bins=bins);
#