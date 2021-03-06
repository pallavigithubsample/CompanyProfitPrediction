# -*- coding: utf-8 -*-
"""LnB Train_model.ipynb


import pandas as pd
import numpy as np
from sklearn import preprocessing  
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("/content/50_Startups (1).csv")
data.head(10)

data.isnull().sum()

data.info()

data.describe()

le=preprocessing.LabelEncoder()
data['State']=le.fit_transform(data['State'])
data.head(5)
data['State'].unique()

co_rel=data.corr()
sns.heatmap(co_rel,linecolor='white')

print(co_rel)

X=data.iloc[:,:3].values
y=data.iloc[:,4:5].values
#print(X)
#print(y)

x_train, x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

training_modelscore=model.score(x_train,y_train)
print("Model performance on training dataset:",training_modelscore)

testing_modelscore=model.score(x_test,y_test)
print("Model Performance on testing dataset:",testing_modelscore)

predmodel=pd.DataFrame(data={"Predicted values":y_pred.flatten(),"Actual_values":y_test.flatten()})
print(predmodel)

accu=r2_score(y_pred,y_test)
print("the r2 score is:",accu)

import joblib
filename='Trained.sav'
joblib.dump(model,filename)

