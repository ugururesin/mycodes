## Simple Linear Regression With scikit-learn
#
#The first step is to import the package numpy and the class LinearRegression from 
import numpy as np
from sklearn.linear_model import LinearRegression
#
#Data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])
#
model = LinearRegression()
#
#fit_intercept is a Boolean (True by default) that decides whether to calculate the intercept b0 (True) or consider it equal to zero (False).
#normalize is a Boolean (False by default) that decides whether to normalize the input variables (True) or not (False).
#copy_X is a Boolean (True by default) that decides whether to copy (True) or overwrite the input variables (False).
#n_jobs is an integer or None (default) and represents the number of jobs used in parallel computation. None usually means one job and -1 to use all processors.
model.fit(x, y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
