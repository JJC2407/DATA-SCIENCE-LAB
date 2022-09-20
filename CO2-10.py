import numpy as np
print("JOYAL JOSE\n21MCA026")
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8,])
print("1D Array-1 : ",arr1)
print("1D Array-2 : ",arr2)
print("Append Array-1 and Array -2 : ",np.append(arr1,arr2,axis=0))
#print(np.append(arr1,arr2,axis=0))

arr3=np.array([[1,2,],
              [3,4]])
arr4=np.array([[5,6,],
              [7,8]])
print("2D Array-1 : \n",arr3)
print("2D Array-2 : \n",arr4)
print("Append Array-1 and Array -2 : \n",np.append(arr3,arr4,axis=0))

