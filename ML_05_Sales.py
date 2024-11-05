# -*- coding: utf-8 -*-
"""ML ass5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ubRfqvLxf_Wis4zwknsjbJtH0lMGhERF
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import codecs
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

with codecs.open('sales_data_sample.csv', 'r', encoding='latin1') as f:
    df = pd.read_csv(f)
df.head()

df.dtypes

df.isna().sum()

df.shape

X = df[['QUANTITYORDERED', 'ORDERLINENUMBER']]
df = df.dropna()
X

p="QUANTITYORDERED"
q="ORDERLINENUMBER"
plt.scatter(X[p], X[q], s = 30, c = 'b')
plt.show()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []  # Within cluster sum of squares

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

ks = range(1, 11)
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow Method")
plt.xlabel("K Value")
plt.ylabel("WCSS")
plt.show()  # Don't forget to call show() to display the plot

!pip install kneed

from kneed import KneeLocator

k=KneeLocator(ks,wcss,curve="convex",direction="decreasing")
optimal_k=k.elbow
print(f"The optimal number of clusters ={optimal_k}")

Kmean = KMeans(n_clusters=optimal_k, init="k-means++", random_state=42)
Kmean.fit(X)

y_kmeans = Kmean.predict(X)

#plotting the results:
plt.scatter(X[p], X[q], c=y_kmeans, s=50, cmap='viridis')
centers = Kmean.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)