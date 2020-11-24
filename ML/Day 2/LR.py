# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:58:17 2020

@author: akhil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("Salary_Data.csv")
a = dataset.iloc[:,:]
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

plt.plot(X, y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.show()