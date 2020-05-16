# =============================================================================
# PYTHON PieChart
# =============================================================================

# DESCRIPTION
#Make sure that your interest is in relative frequencies.
#Areas should represent parts of a whole,
#rather than measurements on a second variable
#(unless that second variable can logically be summed up into some whole).
#
#Limit the number of slices plotted. A pie chart works best with 2 or 3 slices,
#though it's also possible to plot with 4 or 5 slices
#as long as the wedge sizes can be distinguished.
#If you have many categories, or categories that have small proportional rep.,
#consider grouping them together so that fewer wedges are plotted,
#or use an 'Other' category to handle them.
#
#Plot the data systematically. One typical method of plotting a pie chart is
#to start from the top of the circle, then plot each categorical level cw
#from most frequent to least frequent.
#If you have 3 categories and are interested in the comparison of 2 of them,
#a common plotting method is to place the 2 categories of interest
#on either side of the 12 o'clock direction, with the third category
#filling in the remaining space at the bottom.

## LIBRARY IMPORT
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
#%matplotlib.inline #to produce plots in Jupyter NB
import os

## PIE-CHART
#You can create a pie chart with matplotlib's pie function.
#This function requires that the data be in a summarized form:
#the primary argument to the function will be the wedge sizes.
sorted_counts = df['cat_var'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square')
#'square' argument makes it so that the scaling of the plot is equal
#on both the x- and y-axes. Without this call, the pie could end up looking
#oval-shaped, rather than a circle.
#

## DONUT-PLOT
sorted_counts = df['cat_var'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square')
###