import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
x=pd.read_csv("iris.csv")
sb.relplot(x)
plt.show()
sb.displot(x)
plt.show()
sb.histplot(x)
plt.show()