import pandas as pd
iris = pd.read_csv("iris.csv")
print(iris.shape)
print("First five rows :")
print(iris.head())
print("\nLast five rows :")
print(iris.tail())
print("\nSize of date set : ",iris.size)
print("\n",iris['variety'].value_counts())
print(iris.describe())