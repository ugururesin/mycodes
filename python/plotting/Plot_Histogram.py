# =============================================================================
# PYTHON Histograms
# =============================================================================

# DESCRIPTION
#A histogram is used to plot the distribution of a numeric variable.
#It's the QUANTATIVE version of the bar chart.
#However, rather than plot one bar for each unique numeric value,
#values are grouped into continuous bins,
#and one bar for each bin is plotted depicting the number.

## LIBRARY IMPORT
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sb
#%matplotlib.inline #to produce plots in Jupyter NB
import os

#Example Data & hist method
df = pd.DataFrame()
df['num_var'] = [2.2, 3.1 , 4, 4, 4.6, 5.1 , 6.3, 6.4, 6.8, 7]
plt.hist(data = df, x = 'num_var')

## WORKING DIRECTORY
os.getcwd()     #TO GET CURRENT WD
#
path="/Users/UGUR/Desktop/mycodes/_master/data"
os.chdir(path)  #TO SET THE PATH AS WD

## DATA
url = 'https://raw.githubusercontent.com/udacity/AIPND/master/Matplotlib/data/pokemon.csv'
response = requests.get(url)
response #returns 200 if it's successful
#
with open('pokemon.csv', mode='wb') as file: #wb:write binary
    file.write(response.content)
    file.close()
#
pokemon = pd.read_csv('pokemon.csv')
pokemon.info()
#

## HISTOGRAMS
plt.hist(data=pokemon, x='speed', bins = 20); #20 bars!

# BIN BOUNDARIES
bins = np.arange(0, pokemon['speed'].max()+5, 5) #(start, stop, stepsize)
#NOTE THAT 5 is added to 'pokemon['speed'].max()' due to stop is excluded!
plt.hist(data=pokemon, x='speed', bins = bins); #20 bars!

#VISUALIZATION
plt.xlim((0,5)) #limits x-axis btw 0-5

# DIST-PLOT
sb.distplot(pokemon['speed']);              #with density curve estimate
sb.distplot(pokemon['speed'], kde=False);   #without density curve estimate
###


# PLOTTING IN DETAIL
#1
#Python first creates a Figure object.
#And since the Figure doesn't start with any Axes to draw the histogram onto,
#an Axes object is created inside the Figure.
#Finally, the histogram is drawn within that Axes.
#
fig = plt.figure()
ax = fig.add_axes([.125, .125, .775, .755])
#ABOVE, first two argument position of the lower-left hand corner of the Axes!
#ABOVE, the last two elements specifying the Axes width and height!
ax.hist(data = df, x = 'num_var')
#ABOVE, we use the Axes method .hist() just like we did before with plt.hist().

#2
#In seaborn, seaborn functions usually have an "ax" parameter
#to specify upon which Axes a plot will be drawn.
fig = plt.figure()
ax = fig.add_axes([.125, .125, .775, .755])
base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color, ax = ax)

#3
#In the above 2 cases, there was no purpose to explicitly go through
#the Figure and Axes creation steps.
plt.figure(figsize = [10, 5]) # larger figure size for subplots
# example of somewhat too-large bin size
plt.subplot(1, 2, 1) # 1 row, 2 cols, subplot 1
bin_edges = np.arange(0, df['num_var'].max()+4, 4)
plt.hist(data = df, x = 'num_var', bins = bin_edges)
# example of somewhat too-small bin size
plt.subplot(1, 2, 2) # 1 row, 2 cols, subplot 2
bin_edges = np.arange(0, df['num_var'].max()+1/4, 1/4)
plt.hist(data = df, x = 'num_var', bins = bin_edges)


## MULTIPLE PLOTS
# If you don't assign Axes objects as they're created,
#you can retrieve the current Axes using
ax = plt.gca()
#or you can get a list of all Axes in a Figure fig by using
axes = fig.get_axes()
#As for creating subplots, you can use
fig.add_subplot()
#in the same way as plt.subplot() above.

#If you already know that you're going to be creating a bunch of subplots,
#you can use the plt.subplots() function:
fig, axes = plt.subplots(3, 4) # grid of 3x4 subplots
axes = axes.flatten() #reshape from 3x4 array into 12-element vector
for i in range(12):
    plt.sca(axes[i]) #set the current Axes
    plt.text(0.5, 0.5, i+1) #print conventional subplot index num to mid of Axs

#Special note for the text, the Axes limits are [0,1] on each Axes by default,
#and we increment the iterator counter i by 1 to get the subplot index,
#if we were creating the subplots through subplot()
#(Reference: plt.sca(), plt.text())

#Note any aspects of the data like number of modes and skew,
#and note the presence of outliers in the data for further investigation.
plt.figure(figsize = [10, 5])

#Histogram on left: full data
plt.subplot(1, 2, 1)
bin_edges = np.arange(0, df['skew_var'].max()+2.5, 2.5)
plt.hist(data = df, x = 'skew_var', bins = bin_edges)

#Histogram on right: focus in on bulk of data < 35
plt.subplot(1, 2, 2)
bin_edges = np.arange(0, 35+1, 1)
plt.hist(data = df, x = 'skew_var', bins = bin_edges)
plt.xlim(0, 35) # could also be called as plt.xlim((0, 35))

#LOG-SCALING
plt.xscale('log') #for log-transform

#After log-transform check the bins again!
mydata['myvar'].describe()
np.log10(mydata['myvar'].describe())
#
log_bins = 10 ** np.arange(min, max + 0.1, 0.1) #place min & max values
ticks = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
labels = ['{}'.format(v) for v in ticks]
plt.hist(data = pokemon, x='weight', bins=bins);
plt.xscale('log');
plt.xticks(ticks, labels);
###