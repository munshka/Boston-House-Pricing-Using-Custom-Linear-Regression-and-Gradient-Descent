# -*- coding: utf-8 -*-
"""20101050_Boston_House_Pricing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JXEA9VXpaKO9VOatwVk7iEHcx8yu4idi
"""

import torch
import pandas as pd
import seaborn
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/gdrive')

train_data = pd.read_csv('/content/gdrive/MyDrive/BRACU courses/cse427/lab3/train.csv')
train_data.head()

train_data.shape

train_data.columns

seaborn.heatmap(train_data.isnull(), cmap = 'viridis')

chas = pd.get_dummies(train_data['chas'])

train = train_data.drop(['chas'], axis = 1)

train = pd.concat([train, chas], axis = 1)
train.head()

#columns = ['ID',	'crim',	'zn'	,'indus',	'chas'	, 'nox	rm	age	dis	rad	tax	ptratio	black	lstat	medv]

target = train_data['medv']


train_data = train_data.drop(['ID', 'medv'], axis = 1)
train = train_data.to_numpy()
#train = torch.from_numpy(train)

row, column = train.shape

def centralize(x):
  mean = np.mean(x)
  stddev = np.std(x)
  x = (x - mean)/stddev
  return x

for col in range(column):
  train[:, col] = centralize(train[:, col])

train[:5]

target

rows=train.shape[0]
col=train.shape[1]
col

weights = np.zeros(train.shape[1])
bias = 0.0
learning_rate = 0.1
epochs = 50


def gradient_descent(X, y, weights, bias, learning_rate, epochs):
    m = len(y)
    costs = []

    for epoch in range(epochs):
        predictions = np.dot(X, weights) + bias

        dw = np.dot(X.T, (predictions - y))   / m
        db = np.sum(2* (predictions - y)) / m


        weights -= learning_rate * dw
        bias -= learning_rate * db
        cost = np.sum((predictions - y) ** 2) / m
        costs.append(cost)

        if epoch in [9,19,29,39,49]:
            print(f"Epoch {epoch+1}/{epochs} Loss: {cost}")

    return weights, bias, costs


weights, bias, costs = gradient_descent(train, target, weights, bias, learning_rate, epochs)