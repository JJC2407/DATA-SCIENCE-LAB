import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

from sklearn.naive_bayes import  BernoulliNB
classifier = BernoulliNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score
print("Accuracy : ",accuracy_score(y_test,y_pred))
df = pd.DataFrame({'Real values':y_test,'predicted values':y_pred})
print(df)