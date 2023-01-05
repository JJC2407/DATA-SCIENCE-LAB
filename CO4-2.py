import pandas as pd
import seaborn as sns
import matplotlib .pyplot as plt
data=pd.read_csv("iris.csv")
iris = sns.load_dataset("iris")
plot=sns.pairplot(iris)
sns.pairplot(iris, hue="species", kind="hist")
plt.show()
sns.pairplot(iris, kind="kde")
plt.show()
sns.pairplot(iris, kind="reg", hue="species")
plt.show()
sns.pairplot(iris,kind="scatter")
plt.show()