##############################
# CONVOLUTIONAL NEURAL NETWORK
##############################

### THEORY ###
##############

# Step1. CONVOLUTION
#  -----------------                                -------------   ##The size
#  | 0 0 0 0 0 0 0 |       --------                 | 0 1 0 0 0 |   ##reduced!
#  | 0 1 0 0 0 1 0 |       | 0 1 0|                 | 0 1 1 1 0 |
#  | 0 0 0 0 0 0 0 |  (X)  | 0 1 0|               = | 1 0 1 2 1 |
#  | 0 0 0 1 0 0 0 |       | 0 1 0|                 | 1 4 2 1 0 |
#  | 0 1 0 0 0 1 0 |       --------                 | 0 0 1 2 1 |
#  | 0 0 1 1 1 0 0 |                                -------------
#  | 0 0 0 0 0 0 0 |      "FEATURE DETECTOR" or     "FEATURE MAP" or             
#  -----------------      "FEATURE KERNEL"   or     "CONVOLVED MAP" or        
#  "THE INPUT IMAGE"      "FILTER"                  "ACTIVATION MAP"
#

# Step2. MAX POOLING                                        ##In a CNN,
#  -------------                                            ##multiple layers
#  | 0 1 0 0 0 |                        | 1 1 0|            ##are created by
#  | 0 1 1 1 0 | ____________________>  | 4 2 1|            ##different FDs!        
#  | 1 0 1 2 1 | Max Pooling by (2,2)   | 0 2 1| 
#  | 1 4 2 1 0 |                        "POOLED FEATURE MAP"
#  | 0 0 1 2 1 |
#  -------------
#  "FEATURE MAP"
#

# Step.3 FLATTENING                   ##By flattening, we didn't lose info!!!
# --------                (1)         ##By ticking the max of (2,2) subtables
# | 1 1 0|  __________>   (1)         ##of the feature map, information is kept 
# | 4 2 1|  Flattening    (0)         ##by keeping track of the part image
# | 0 2 1|                ...         ##that contained the high numbers
# --------                (1)         ##corresponding to where the f.detector
# "POOLED FM"        "input layer"    ##detected some specific feautes!
#

# Step.4 FULL CONNECTION
#
#               fully 
#  input -----> connected ----->  output
#  layer        layer             layer
#


##################
### CODING CNN ###
##################

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

import keras

# PART 1 - BUILDING THE CNN
###########################
# IMPORTING THE KERAS LIBRARIES AND PACKAGES
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# INITIALISING THE CNN
classifier = Sequential()

# STEP 1 - CONVOLUTION
#'3x3':feature detector size
#'32': number of feature detector
# WARNING: input_shape is 64,64,3 for TensorFlow! 64,64 for Theano!
# WARNING: For Relu, in feature maps, all values MUST be non-negative!!!
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# STEP 2 - POOLING
classifier.add(MaxPooling2D(pool_size = (2, 2))) #(2,2) is common

# ADDING A "SECOND CONVOLUTIONAL LAYER"
classifier.add(Conv2D(32, (3, 3), activation = 'relu')) #no need input_shape for additional layers
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# STEP 3 - FLATTENING
classifier.add(Flatten())

# STEP 4 - FULL CONNECTION
classifier.add(Dense(units = 128, activation = 'relu'))     #128 is experimental (2^n numbers are common!)
classifier.add(Dense(units = 1, activation = 'sigmoid'))    #1 node for 2 class

# COMPILING THE CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# PART 2 - FITTING THE CNN TO THE IMAGES
########################################
'''CV needs to find some patterns in the pixels, and this requires many images!
Here, in total there are 10,000 images (8,000 for traning) and it's not much!
Either we need some more images, or we can use a trick: "Data Augmentation"!
It will create many batches of our images, and in each batch it will apply
some random transformations on a random selection of our images,
like rotating them, flipping them, shifting them, or even shearing them!
Eventually what we'll get during the training is many more diverse images
inside these batches, and therefore a lot more material to train.
And now we understand why it is called image augmentation.
That's because the amount of our training images is augmented!
Besides, because the transformations are random transformations,
well our model will never find the same picture across the batches.
So all this image augmentation trick can only reduce overfitting.'''

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('udemy_cnn_dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('udemy_cnn_dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set, steps_per_epoch = 8000, epochs = 25,
                         validation_data = test_set, validation_steps = 2000)


# PART 3 - SINGLE PREDICTION
############################
import numpy as np
from keras.preprocessing import image
test_image = image.load_img('udemy_cnn_dataset/single_prediction/cat_or_dog_1.jpg',
                            target_size = (64,64))
test_image = image.load_img('udemy_cnn_dataset/single_prediction/cat_or_dog_1.jpg',
                            target_size = (64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices
#
if result[0][0] == 1:
    prediction = 'Dog'
else:
    prediction = "Cat"