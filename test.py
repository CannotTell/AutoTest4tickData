#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/4/2017 2:40 PM
# @Author  : JZK
# @File    : test.py



import cv2
from sklearn import svm
import random
import numpy

imgl = cv2.imread('C:\\Users\\zhukai.jiang\\Desktop\\index.jpg')
img = cv2.cvtColor(imgl, cv2.COLOR_BGR2GRAY)
# print(img)
X = img  # training samples
y = []
for i in range(300):
    y.append(random.randint(0,300))
# print(y)
#y = [0]  # training target
clf = svm.SVC()  # class
clf.fit(X,y)  # training the svc model

result = clf.predict([[2, 2]])  # predict the target of testing samples
print(result)
    # result  # target

print(clf.support_vectors_)  # support vectors

print(clf.support_)  # indeices of support vectors

print(clf.n_support_)  # number of support vectors for each class