# =============================================================================
# PYTHON Scatter Plots
# =============================================================================

## LIBRARY IMPORT
import os
import numpy as np
import pandas as pd
import requests
import seaborn as sb
import matplotlib.pyplot as plt
#%matplotlib.inline #to produce plots in Jupyter NB

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

## MATPLOTLIB'S SCATTER
plt.scatter(data= fuel_econ, x='displ', y='comb');
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)')

## SEABORN'S SCATTER
sb.regplot(data= fuel_econ, x='displ', y='comb'); #fit_reg=False to close reg.
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)')


## ALTERNATIVE APPROACH (Seaborn's Regplot)
#By default, the regression function is linear,
#and includes a shaded confidence region for the regression estimate.
sb.regplot(data = df, x = 'num_var1', y = 'num_var2')

#In this case, since the trend looks like a log(y) ~ x relationship
#that is, linear increases in the value of x are associated with
#linear increases in the log of y,
#plotting the regression line on the raw units is not appropriate.
#If we don't care about the regression line, then we could set reg_fit = False
#Otherwise, we need to transform the data!
def log_trans(x, inverse = False):
    if not inverse:
        return np.log10(x)
    else:
        return np.power(10, x)

sb.regplot(df['num_var1'], df['num_var2'].apply(log_trans))
tick_locs = [10, 20, 50, 100, 200, 500]
plt.yticks(log_trans(tick_locs), tick_locs)

## OVERPLOTTING (SOLUTIONS: Sampling, Transparency, Jitter)
#
#JITTER is a random value (or for our purposes pseudo-random)
#that is assigned to the dots to separate them
#so that they aren't plotted directly on top of each other.
#In only sb.regplot use x_jitter or (y_jitter)!
sb.regplot(data= fuel_econ, x='year', y='comb', x_jitter=0.3,
           scatter_kws = {'alpha': 1/20} );
#x_jitter=0.3 means that each x value will adjusted randomly up to ±0.3
#scatter_kws = {'alpha': 1/20}  means that make dots transparent

## HEAT MAPS
#2D Version of Histogram!
#Good for discrete variable vs. discrete variable
#Good alternative to transparency for lots of data
#Bin sizes are important!
#
plt.hist2d(data= fuel_econ, x='displ', y='comb'); #default bin=10
plt.colorbar()
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)')

# Changing the minimum value that gets a color!
plt.hist2d(data= fuel_econ, x='displ', y='comb', cmin=0.5);
plt.colorbar()
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)')

# Inverse Colors!
plt.hist2d(data= fuel_econ, x='displ', y='comb', cmin=0.5,
           cmap='viridis_r'); #viridis_r for reverse colors!
plt.colorbar()
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)')

# Changing the Bins!
fuel_econ[['displ','comb']].describe() #mins are 0.6 & 6! Use halfs of them!
bins_x = np.arange(0.6, 7+0.3, 0.3)
bins_y = np.arange(12, 58+3, 3)
plt.hist2d(data= fuel_econ, x='displ', y='comb', cmin=0.5,
           cmap='viridis_r', bins=[bins_x, bins_y]); 
plt.colorbar()
plt.xlabel('Displacement (l)')
plt.ylabel('Combined Fuel Eff. (mpg)')


## ADVANCED HEAT MAP
#If you have many data, you might want to add annotations to cells in the plot
#indicating the count of points in each cell.
#From hist2d, this requires the addition of text elements one by one,
#much like how text annotations were added one by one to the bar plots.
#We can get the counts to annotate directly from what is returned by hist2d,
#which includes not just the plotting object,
#but an array of counts and two vectors of bin edges.
#
# hist2d returns a number of different variables, including an array of counts
bins_x = np.arange(0.5, 10.5+1, 1)
bins_y = np.arange(-0.5, 10.5+1, 1)
h2d = plt.hist2d(data = df, x = 'disc_var1', y = 'disc_var2',
               bins = [bins_x, bins_y], cmap = 'viridis_r', cmin = 0.5)
counts = h2d[0]
#
# loop through the cell counts and add text annotations for each
for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        c = counts[i,j]
        if c >= 7: # increase visibility on darkest cells
            plt.text(bins_x[i]+0.5, bins_y[j]+0.5, int(c),
                     ha = 'center', va = 'center', color = 'white')
        elif c > 0:
            plt.text(bins_x[i]+0.5, bins_y[j]+0.5, int(c),
                     ha = 'center', va = 'center', color = 'black')
###