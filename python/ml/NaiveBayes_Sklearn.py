#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:58:07 2019

@author: UGUR
"""

import numpy as np
X = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])
Y = np.array([1,1,1,2,2,2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB #classifier
clf.fit(X, Y)
GaussianNB()
print(clf.predict([[-0,8,-1]]))