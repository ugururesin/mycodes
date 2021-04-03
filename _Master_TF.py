## TENSORFLOW - v2.0 ##
#######################
import tensorflow as tf

## COMPUTATIONAL GRAPH CREATION
input1 = tf.constant(2.0)
input2 = tf.constant(5.0)
sess = tf.Session()
add_node = tf.add(input1, input2)

print(add_node)           #Tensor("Add:0", shape=(), dtype=float32)
print(sess.run(add_node)) #7.0
p1 = tf.placeholder(tf.float32)
p2 = tf.placeholder(tf.float32)
add_ph = p1 + p2
print(sess.run(add_ph, {p1: 2, p2: 5}))             #7.0
print(sess.run(add_ph, {p1: 1.2, p2: 3.5}))         #4.7
print(sess.run(add_ph, {p1: [1, 2], p2: [5, 8]}))   #[ 6. 10.]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
a = tf.Variable([1], dtype=tf.float32)
b = tf.Variable([-2], dtype=tf.float32)
linear_model = a*x+b
init = tf.global_variables_initializer()
print(sess.run(linear_model, {x:[0,1,2,3,4,5]}))

init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model, {x:[0,1,2,3,4,5]}))
[-2. -1.  0.  1.  2.  3.]

squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
feed_dict = {
    x:[0,1,2,3,4,5],
    y:[-1,-.5,0,.5,1,1.5] }

print(sess.run(loss, feed_dict))  #4.75
assignA = tf.assign(a, [.25])
assignB = tf.assign(b, [0])
sess.run([assignA, assignB])      #[array([0.25], dtype=float32), array([0.], dtype=float32)]
print(sess.run(loss, feed_dict))  #1.9375
assignA = tf.assign(a, [.5])
assignB = tf.assign(b, [-1])
sess.run([assignA, assignB])      #[array([0.5], dtype=float32), array([-1.], dtype=float32)]
print(sess.run(loss, feed_dict))  #0.0


'''
ESTIMATORS
TensorFlow tf.contrib.learn is a high level API for machine learning process. It offers variety of Estimators that represent predefined models. Some of the examples are:

LinearClassifier - model for linear classification
KMeansClustering - an estimator for K-Means clustering.
DNNClassifier - a classifier for deep neural network models
DNNRegressor - deep neural network models.
'''

import numpy as np
import tensorflow as tf


''' The Data
Note that we used one_hot parameter with the value False. 
This means the labels will be read as integer values instead of one hot encoded vectors.
'''
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=False)


''' The Initials
First, we need some values to be provided.
We have 10 classes for our dataset, image size is 28 and the hidden layer size is set to 1024:
'''
image_size = 28
labels_size = 10
hidden_size = 1024


''' The Estimator
To create the estimator we need the set of feature columns.
TensorFlow offers the tf.contrib.layers.real_valued_column to build it.
As our images are flattened we will use the image_size*image_size as dimension.
'''
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=image_size*image_size)]


''' Model Inıt
Next step is to initiate the model itself.
DNNClassifier is used as it uses deep neural network underneath.
There is only one hidden layer, so the hidden_units parameter (which is a list of sizes)
contains only one number.
As an optimiser there will be used AdamOptimizer
'''
classifier = tf.contrib.learn.DNNClassifier(
  feature_columns=feature_columns,
  hidden_units=[hidden_size],
  n_classes=labels_size,
  optimizer=tf.train.AdamOptimizer())


''' Making Predictions
The trained model can also be used to make prediction on the new data.
Let's get the first 10 samples from the validation dataset and use the classifier on them.
'''
features = mnist.validation.images[:10]
labels = mnist.validation.labels[:10].astype(np.int32)
predictions = list(classifier.predict(x=features))


''' Validation
Now we can and check the predictions against the real .values
'''
print("\nPredicted labels from validation set: %s"%predictions)
print("Underlying values: %s"%list(labels))
