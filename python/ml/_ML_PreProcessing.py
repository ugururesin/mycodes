#################################
## DATA PREPROCESSING TEMPLATE ##
#################################

## LIBRARIES
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os
#

## WORKING DIRECTORY
os.getcwd()     #TO GET CURRENT WD
path="/Users/UGUR/Desktop/mycodes"
os.chdir(path)  #TO SET THE PATH AS WD
#

## IMPORTING THE DATASET
dataset = pd.read_csv('Mydata.csv')
X = dataset.iloc[:, :-1].values		#take all rows & cols (except for last col)
y = dataset.iloc[:, -1].values		#take all rows & only the last col
#

## SPLITTING THE DATASET INTO THE TRANING & TEST SETS
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=0)
#

## FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)