# =============================================================================
# PYTHON VISUALIZATION CODES
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
#