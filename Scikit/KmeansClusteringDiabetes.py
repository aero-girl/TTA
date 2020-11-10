# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:09:03 2020
Diabetes Linear Regression model
Clustering the Diabetes data
@author: Gavi
"""


from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

# load datasets
diabetes = datasets.load_diabetes();

# explore dataset
print(diabetes.DESCR)

# prints the dictionary keys of diabetes data
print(diabetes.keys())

# Load diabetes target/training dataset
X = diabetes.data

# Load diabetes target set
Y = diabetes.target

# prints the no of rows and columns in the dataset
print("Diabetes data shape is", X.shape)

# prints the target/training set of the data
print("Diabetes target shape is",Y.shape)

# prints grougs within diabetes data
print("Diabetes different groups are",len(np.unique(Y)))

#plt.scatter(X[:, 0], X[:,2]);
#plt.show

kmeans = KMeans(n_clusters=2, random_state=0)
Y_predict = kmeans.fit_predict(X)

# Get the cluster centroids
print(kmeans.cluster_centers_)

# Visualise clusters
plt.subplot(211)
plt.scatter(X[:, 0], X[:,2], c=Y_predict, cmap='rainbow',marker='o', edgecolor='black');
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 2],c='black', s=200, alpha=0.5)
plt.title('Diabetes Data and cluster centroids')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show


plt.subplot(212)
plt.scatter(X[:, 0], X[:,3], c=Y_predict, cmap='rainbow',marker='o', edgecolor='black');
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 3],c='black', s=200, alpha=0.5)
plt.xlabel('Age')
plt.ylabel('BP')