import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Walking','Cycling','Car','Bus','Train'])
y = np.array([29,15,35,18,3])

plt.bar(x, y,color='Green',width=.1)
plt.xlabel("Mode of Transport")
plt.ylabel("frequency")
plt.show()