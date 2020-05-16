# =============================================================================
# PYTHON BarChart
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

## BAR-PLOT
sb.countplot(data = pokemon, x='generation_id'); #plots with colors (default)

# COLORS
sb.color_palette()              #list of tuples for colors
mycolor= sb.color_palette()[0]  #first color of the list
sb.countplot(data = pokemon, x='generation_id', color=mycolor);

# SORTING THE BARS
# WAY-1 (Manual)
sb.countplot(data = pokemon, x='generation_id', color=mycolor,
             order = [5,1,3,4,2,7,6]);
# WAY-2 (By value_counts)
sb.countplot(data = pokemon, x='generation_id', color=mycolor,
             order = pokemon['generation_id'].value_counts().index);
             
# ROTATING THE LABELS-X
sb.countplot(data = pokemon, x='type_1', color=mycolor) #unreadable labels!
plt.xticks(rotation = 90); #rotates the labels 90 degree ccw

# HORIZANTAL BAR-CHART (Turn 'x' into 'y')
sb.countplot(data = pokemon, y='type_1', color=mycolor,
             order = pokemon['type_1'].value_counts().index);

# =============================================================================
# DATA IS MODIFIED FOR FURTHER COMMANDS (melt method!)
# =============================================================================
pkmn_types = pokemon.melt(id_vars = ['id', 'species'],
                          value_vars = ['type_1', 'type_2'],
                          var_name ='type_level', value_name ='type').dropna()
pkmn_types[802:812]              
#             

# RELATIVE FREQUENCY
type_counts = pkmn_types['type'].value_counts()
type_order = type_counts.index
sb.countplot(data = pkmn_types, y='type', color=mycolor, order = type_order);
#
n_pokemon = pokemon.shape[0]    #number of pokemons
max_type_count = type_counts[0] #number of types
max_prop = max_type_count / n_pokemon   
print(max_prop) #denominator
#
tick_props = np.arange(0, max_prop, 0.02) #proportion values btw 0 and max
tick_props
tick_names = ['{:0.2f}'.format(v) for v in tick_props]
tick_names
#
sb.countplot(data = pkmn_types, y='type', color=mycolor, order = type_order);
plt.xticks(tick_props * n_pokemon, tick_names) #(position, tick_labels)
plt.xlabel('proportion')
#
sb.countplot(data = pkmn_types, y='type', color=mycolor, order = type_order);
for i in range(type_counts.shape[0]):
    count = type_counts[i]
    pct_string = '{:0.1f}%'.format(100*count/n_pokemon)
    plt.text(count+1,i,pct_string, va='center'); #(x_pos, y_pos, str_printed)
###
    
# =============================================================================
# PYTHON Clustered Bar Charts
# =============================================================================

# DESCRIPTION
#To depict the relationship between two categorical variables,
#we can extend the univariate bar chart into a clustered bar chart.
#We still want to depict the count of data points in each group,
#but each group is now a combination of labels on two variables.
#So we organize the bars into an order that makes the plot easy to interpret.
#In CBC, bars are organized into clusters based on levels of the 1st variable,
#then bars are ordered consistently across the 2nd variable within each cluster
#This is easiest to see with an example, using seaborn's countplot function.
#To take the plot from univariate to bivariate,
#we add the second variable to be plotted under the "hue" argument:
sb.countplot(data = df, x = 'cat_var1', hue = 'cat_var2')

## EXAMPLE DATA
fuel_econ = pd.read_csv('fuel_econ.csv')
fuel_econ.head(3)
#
fuel_econ['trans_type'] = fuel_econ['trans'].apply(lambda x: x.split()[0])
fuel_econ.head(1)

## CLUSTERED BAR CHART
sb.countplot(data = fuel_econ, x='VClass', hue='trans_type')
plt.xticks(rotation=15)

## ALTERNATIVE (Heat Map)
ct_count = fuel_econ.groupby(['VClass', 'trans_type']).size()
ct_count = ct_count.reset_index(name = 'count')
ct_count = ct_count.pivot(index='VClass', columns='trans_type', values='count')
#
sb.heatmap(ct_count, annot=True, fmt='d') #annotations, d:decimals
###

# =============================================================================
# ADAPTATION of BAR-CHARTS
# =============================================================================
#BoxPlot - COUNTS
sb.boxplot(data = fuel_econ, x='VClass', y='comb',
           color = base_color);
plt.xticks(rotation=15);
#

#BarPlot - MEANS
sb.barplot(data = fuel_econ, x='VClass', y='comb',
           color = base_color); #add errwidth=0 to remove mean whiskers
plt.xticks(rotation=15);
plt.ylabel('Avg. Combined Fuel Eff. (mpg)');
#

#BarPlot - STANDARD DEVIATION
sb.barplot(data = fuel_econ, x='VClass', y='comb',
           color = base_color, ci='sd');
plt.xticks(rotation=15);
plt.ylabel('Avg. Combined Fuel Eff. (mpg)');
#

#PointPlot - STANDARD DEVIATION
sb.pointplot(data = fuel_econ, x='VClass', y='comb',
           ci='sd'); #add linestyles="" to remove the lines
plt.xticks(rotation=15);
plt.ylabel('Avg. Combined Fuel Eff. (mpg)');
#

###