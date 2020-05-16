###########################
# ARTIFICIAL NEURAL NETWORK
###########################

# INSTALLING THEANO
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# INSTALLING TENSORFLOW
# pip install tensorflow

# INSTALLING KERAS
# pip install --upgrade keras

# WORKING DIRECTORY
import os
os.getcwd()     #TO GET CURRENT WD
#
path_windows ="C:\\Users\\admin\\Desktop\\mycodes\\data"
path_mac="/Users/UGUR/Desktop/mycodes/data"
os.chdir(path_windows)  #TO SET THE PATH AS WD


# PART 1 - DATA PREPROCESSING
#############################
# IMPORTING THE LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

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

#ALTERNATIVE-1
#onehotencoder = OneHotEncoder(categories = [2])
#X = onehotencoder.fit_transform(X).toarray()
#X = X[:, 1:]

#ALTERNATIVE-2
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([("Country", OneHotEncoder(),[1])], remainder="passthrough")
X = ct.fit_transform(X)
X = np.asfarray(X)
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
'''('adam' is a stochastic gradient descent method)
loss function:
if dep. var. has 2 levels => loss func.= binary_crossentropy
if dep. var. has +2 levels => loss func.= categorical_crossentropy'''
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# FITTING THE ANN to the TRAINING SET
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)


# PART 3 - MAKING PREDICTIONS AND EVALUATING THE MODEL
######################################################
# Predicting the Test set results
y_pred = classifier.predict(X_test)	#gives a probability
y_pred = (y_pred > 0.5)				#threshold for true/false

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
acc = 100*cm.trace()/cm.sum()
print("The prediction accuracy is {}%".format(acc))


# PART 4 - PREDICTING A SINGLE NEW OBSERVATION
##############################################
""" Predict if the customer with the following informations will leave the bank:
    Geography: France           ---> 0, 0 (categorical dummy variable)
    Credit Score: 600           ---> 600
    Gender: Male                ---> 1 (categorical dummy variable)
    Age: 40                     ---> 40
    Tenure: 3                   ---> 3
    Balance: 60000              ---> 60000
    Number of Products: 2       ---> 2
    Has Credit Card: Yes        ---> 1
    Is Active Member: Yes       ---> 1
    Estimated Salary: 50000     ---> 50000
                                # And normalize the numbers above!
    """
new_observation = np.array([[0.0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])
#[[]] for a 2D array! (Because it's a row!)
#'0.0' to prevent warning due to float!

new_prediction = classifier.predict(sc.transform(new_observation))
new_prediction = (new_prediction > 0.5)
new_prediction #FALSE: Customer won't leave the bank!


# PART 5 - PERFORMANCE TUNING of THE ANN
########################################
from keras.wrappers.scikit_learn import KerasClassifier 
from sklearn.model_selection import cross_val_score
from keras.models import Sequential		#to initialize NN
from keras.layers import Dense			#to create layers

## K-FOLD CROSS VALIDATION
def build_classifier():
    classifier = Sequential() #local classifier variable
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier

# The Estimator
classifier= KerasClassifier(build_fn = build_classifier, batch_size= 10, nb_epoch= 100)

# cross_val_score: is for k-fold cross validation!
# n_jobs: The number of CPUs to use to de the computation. -1:All CPUs!
accuracies = cross_val_score(estimator = classifier, X= X_train, y= y_train, cv= 10, n_jobs= -1)

# Average accuracy & the variance
mean = accuracies.mean()
variance = accuracies.std()

## USE THIS IN CASE OF "OVERFITTING"
''' "Dropout Regularization" to reduce overfitting if needed!
At each iteration of the training some neurons of the ANN are randomly disabled
to prevent them from being too dependent on each other when they learn the
correlations and therefore, by over-writing these neurons the ANN learns 
several INDEPENDENT CORRELATIONS of the data thanks to the fact that
the neurons work more independently, that prevents the neurons from
learning too much and therefore that prevents overfitting!
Dropout should be applied to the layers when there is overfitting!
Because, this will give more chance to reduce overfitting.'''
from keras.layers import Dropout
#
# THE INPUT & 1ST HIDDEN LAYER "with DROPOUT"
# (add: to add layers, Dense:for the node details)
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
classifier.add(Dropout(p=0.1)) #p: fraction of the input units to drop
#
# 2ND HIDDEN LAYER "with DROPOUT"
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(p=0.1)) #p: fraction of the input units to drop
#
# OUTPUT LAYER
# ('sigmoid' bcs we need a probability prediction!)
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
#
#

## TUNING THE ANN (The "optimizer", "batch_size" & "nb_epoch" are NOT fixed!)
#The "kernel_initializer", "activation" and "loss" can also be changed!
from keras.wrappers.scikit_learn import KerasClassifier 
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
#
def build_classifier(the_optimizer):
    classifier = Sequential() #local classifier variable
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = the_optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier
#
classifier= KerasClassifier(build_fn = build_classifier, batch_size= 10, nb_epoch= 100)
parameters = {'batch_size':[25,32],
              'nb_epoch':[100,500],
              'the_optimizer':['adam','rmsprop']} #rmsprop is better in RNN!
grid_search = GridSearchCV(estimator = classifier,
                           param_grid = parameters,
                           scoring = 'accuracy',
                           cv = 10)
grid_search = grid_search.fit(X_train, y_train)
#
best_parameters = grid_search.best_params_ 
best_accuracy = grid_search.best_score_
#
print("The best accuracy is {} with the {} parameters".format(best_accuracy,best_parameters))
##
#HERE WE CAN ALSO DO K-FOLD CROSS VALIDATION & PARAMETER TUNING TOGETHER!!!
#-DO AS A HOMEWORK!!!-