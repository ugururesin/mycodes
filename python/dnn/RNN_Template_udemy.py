##########################
# RECURRENT NEURAL NETWORK
##########################

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
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# IMPORTING THE TRAINING SET
dataset_train = pd.read_csv('udemy_rnn_dataset/Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values

# FEATURE SCALING
''' Feature scaling can be done either with Standardization or Normalization!
In RNN, the Normalization is preferred in general'''
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

# CREATING A DATA STRUCTURE WITH 60 TIMESTEPS AND 1 OUTPUT
''' In this we are going to create 'a specific data structure'',
that's the most important step actually of data pre-processing for RNNs.
We're going to create a data structure specifying what the RNN will need
to remember when predicting the next stock price.
And this is called the number of time steps.
This is super important to have the right number of time steps
because a wrong number of time steps could lead to over fitting or
nonsense predictions!!! '''

X_train = []
y_train = []
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

'''60 timesteps means that at each time T,
the RNN is going to look at the 60 stock prices before time T,
that is the stock prices between 60 days before time T and time T,
and based on the trends, it is capturing during these 60 previous timesteps,
it will try to predict the next output.
So 60 timesteps of the past information from which RNN is gonna try to learn
and understand some correlations, or some trends, and based on its understanding,
it's going to try to predict the next output.
That is, the stock price at time T plus one.
So that's very important to understand.
60 is a number that I experimented, trying different number of time steps.
I tried one time step first, which was completely stupid, 
because it led to overfitting.
The model was not learning anything.
Then 20 timesteps, which was not enough to be able to capture some trends,
then 30, 40, and eventually the best number of timesteps
I ended up with was 60.
And the 60 timesteps correspond of course to the 60 previous financial days,
and since there 20 financial days in one month,
well 60 timesteps correspond to three months.
So that means that each day we're gonna look at the three previous month
to try to predict the stock price the next day.
So we're gonna have 60 timesteps and one output,
which will be the stock price at time T plus one.
So make sure to understand it clearly.'''

# RESHAPING
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))


# PART 2 - BUILDING THE RNN
###########################
# IMPORTING THE KERAS LIBRARIES AND PACKAGES
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# INITIALISING THE RNN
regressor = Sequential()
'''And why did I call it regressor this time?
As opposed to classifier like in the first two parts: ANN and CNN.
Well that because this time we're predicting a continuous output.
A continuous value, which is the google stock price, twenty plus one.
And therefore we are doing some regression.
A reminder, regression is about predicting the continuous value.
And classification is about creating a (mumble), a class.
So, this time we're predicting a continuous value.
And therefore I called my neural network, recurrent neural network regressor.
'''

# ADDING THE FIRST LSTM LAYER AND SOME DROPOUT REGULARISATION
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
'''There are 3 arguments for LSTM!
1: the number of units, which is the number of LSTM cells or units
you want to have in this LSTM layer.

2: return sequences and we will have to set it equal to true,
because we are building a stacked LSTM which therefore will have
several LSTM layers and when you add another LSTM layer after the one
you are creating right now, well you have to set the return sequences argument
to true.
Once you are done with your LSTM layers, you are not gonna add
another one after that, you will set it equal to false,
but you won't even have to do this because this is the default value of
the return sequences parameter.

3: input_shape, and that is exactly the shape of the input containing
x_train that we created in the last step of the data preprocessing part.
It's an input shape in three dimensions, in 3-D,
corresponding to the observations, the time steps, and the indicators.
But in this third argument of the LSTM class, we won't have to include
the three dimensions, only the two last ones corresponding to the
time steps and the indicators, because the first one,
corresponding to the observations, will be automatically taken into account.

So, we will only specify x_train.shape[1], corresponding to the time steps,
and [1] corresponding to the predictors, the indicators.

'''
regressor.add(Dropout(0.2))

# ADDING A SECOND LSTM LAYER AND SOME DROPOUT REGULARISATION
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# ADDING A THIRD LSTM LAYER AND SOME DROPOUT REGULARISATION
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

# ADDING A FOURTH LSTM LAYER AND SOME DROPOUT REGULARISATION
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# ADDING THE OUTPUT LAYER
regressor.add(Dense(units = 1))

# COMPILING THE RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# FITTING THE RNN TO THE TRAINING SET
regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)


# PART 3 - MAKING THE PREDICTIONS AND VISUALISING THE RESULTS
#############################################################
# GETTING THE REAL STOCK PRICE OF 2017
dataset_test = pd.read_csv('udemy_rnn_dataset/Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values

# GETTING THE PREDICTED STOCK PRICE OF 2017
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# VISUALISING THE RESULTS
plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()