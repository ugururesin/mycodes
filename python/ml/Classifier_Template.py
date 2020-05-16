#########################
## CLASSIFIER TEMPLATE ##
#########################

## WORKING DIRECTORY
import os
os.getcwd()     #TO GET CURRENT WD
path="/Users/UGUR/Desktop/mycodes/training/⁨DeepLearning⁩/Classification_Template"⁩
os.chdir(path)  #TO SET THE PATH AS WD
#

## IMPORTING THE DATASET
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2,3]].values		
y = dataset.iloc[:, 4].values		
#

## SPLITTING THE DATASET INTO THE TRANING & TEST SETS
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.25, random_state=0)
#

## FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#

## FITTING LR to THE TRAINING SET
from sklearn.linear_model import LogisticRegression #ATTENTION: YOU CAN USE ANY CLASSIFIER HERE!!!
classifier = LogisticRegression(random_state = 0) #random_state=0 is to have same results!
classifier.fit(X_train, y_train)
#

## PREDICTION
y_pred = classifier.predict(X_test)
#

## CONFUSION MATRIX
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
#

## TRAINING RESULTS (VISUALIZATION)
import numpy as np
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
#creating the pixel points
X1, X2 = np.meshgrid(np.arange(start= X_set[:,0].min()-1, stop= X_set[:,0].max()+1, step= 0.01),
					 np.arange(start= X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step= 0.01))
#
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
			 alpha= 0.75, cmap= ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
#
for i, j in enumerate(np.unique(y_set)):
	plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
				c = ListedColormap(('red', 'green'))(i), label= j)
#
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
#

## TESTING RESULTS (VISUALIZATION)
X_set, y_set = X_test y_test
#creating the pixel points
X1, X2 = np.meshgrid(np.arange(start= X_set[:,0].min()-1, stop= X_set[:,0].max()+1, step= 0.01),
					 np.arange(start= X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step= 0.01))
#
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
			 alpha= 0.75, cmap= ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
#
for i, j in enumerate(np.unique(y_set)):
	plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
				c = ListedColormap(('red', 'green'))(i), label= j)
#
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
#
#