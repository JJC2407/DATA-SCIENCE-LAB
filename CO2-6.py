import numpy as np
print("JOYAL JOSE\n21MCA026")
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[14,15,16,17]])
print("Matrix\n",a)
print("\nMatrix elements excluding the first row\n",a[1:])
print("\nMatrix elements excluding the last column\n",a[:,:3])
print("\nMatrix elements of 1 st and 2 nd column in 2 nd and 3 rd row\n",a[1:3,:2])
print("\nMatrix elements of 2 nd and 3 rd column\n",a[:,1:3])
print("\nMatrix elements 2 nd and 3 rd element of 1 st row\n",a[:1,1:3])
b=a.reshape(1,-1)[0][4:10]
print("\nMatrix elements from indices 4 to 10 in descending order\n",np.sort(b))
