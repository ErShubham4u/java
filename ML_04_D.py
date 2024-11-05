# -*- coding: utf-8 -*-
"""ML ass4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19icKZOsFR3JFDOFj7zYtFZaXYahuW1P9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("diabetes.csv")
print(df.head())

df.tail()

df.isnull().sum()

sns.heatmap(df.corr(),cmap="crest",annot=True,)

from sklearn.preprocessing import MinMaxScaler
x=df[['Pregnancies','Glucose','BMI','Age']]
# x=df.drop('Outcome',axis=1)
y=df['Outcome']
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(x)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
param_grid = {'n_neighbors': range(1, 21)}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_train, Y_train)
print("Best k:", grid_search.best_params_)

knn=KNeighborsClassifier(n_neighbors=5,metric="euclidean")
knn.fit(X_train,Y_train)
Y_pred=knn.predict(X_test)
knn.score(X_test,Y_test)

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score
cm=confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix is as follows: ")
print(cm)

accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy is: ",accuracy)
precision=precision_score(Y_test,Y_pred)
print("Error Rate is: ",1-accuracy)
print("Precision score is: ",precision)
recall=recall_score(Y_test,Y_pred)
print("Recall score is: ",recall)

import statistics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != Y_test))

plt.figure(figsize=(10, 6))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

print(statistics.mean(error_rate))

knn=KNeighborsClassifier(n_neighbors=9,metric="euclidean")
knn.fit(X_train,Y_train)
Y_pred=knn.predict(X_test)
knn.score(X_test,Y_test)

accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy is: ",accuracy)
precision=precision_score(Y_test,Y_pred)
print("Error Rate is: ",1-accuracy)
print("Precision score is: ",precision)
recall=recall_score(Y_test,Y_pred)
print("Recall score is: ",recall)