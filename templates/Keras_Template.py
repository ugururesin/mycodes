# ARTIFICIAL NEURAL NETWORK

# INSTALLING THEANO
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# INSTALLING TENSORFLOW
# pip install tensorflow

# INSTALLING KERAS
# pip install --upgrade keras

# PART 1 - DATA PREPROCESSING
#############################
# IMPORTING THE LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# WORKING DIRECTORY
import os
os.getcwd()     #TO GET CURRENT WD
#
path_windows ="C:\\Users\\admin\\Desktop\\mycodes\\data"
path_mac="/Users/UGUR/Desktop/mycodes/data"
os.chdir(path_windows)  #TO SET THE PATH AS WD

# IMPORTING THE DATASET
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# ENCODING CATEGORICAL DATA
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# SPLITTING THE DATASET INTO THE TRAINING SET AND TEST SET
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# PART 2 - NOW LET'S MAKE THE ANN!
##################################
# IMPORTING THE KERAS LIBRARIES AND PACKAGES
import keras
from keras.models import Sequential		#to initialize NN
from keras.layers import Dense			#to create layers

# Initialising the ANN
classifier = Sequential()

# THE INPUT & 1ST HIDDEN LAYER
# (add: to add layers, Dense:for the node details)
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# 2ND HIDDEN LAYER
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# OUTPUT LAYER
# ('sigmoid' bcs we need a probability prediction!)
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# COMPILING THE ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# FITTING THE ANN to the TRAINING SET
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)


# PART 3 - MAKING PREDICTIONS AND EVALUATING THE MODEL
######################################################
# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)