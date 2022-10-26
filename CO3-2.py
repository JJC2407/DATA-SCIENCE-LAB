
import matplotlib.pyplot as plt
import numpy as np

day =np.array(['Monday','Tuesday','Wednesday','Thursday','Friday'])
inc = np.array([300,450,150,400,650])
plt.subplot(2,1,1)
plt.title("Sales Data1",loc="left",color="red")
plt.xlabel('DAY',color="red")
plt.ylabel('DRINKS',color="red")
plt.grid(color="Blue",linestyle="dotted")
plt.plot(day,inc,color="cyan",marker="h",markerfacecolor="magenta",markersize="20",linestyle="dotted")
day =np.array(['Monday','Tuesday','Wednesday','Thursday','Friday'])
inc2=np.array([400,500,350,300,500])
plt.subplot(2,1,2)
plt.xlabel('DAY',color="red")
plt.ylabel('FOOD',color="red")
plt.title("Sales Data2",loc="left",color="red")
plt.grid(color="Blue",linestyle="dashdot")
plt.plot(day,inc2,color="yellow",marker="d",markerfacecolor="green",markersize="20",linestyle="dashed")
plt.show()