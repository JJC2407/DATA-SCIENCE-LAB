import numpy as np
print("JOYAL JOSE\n21MCA026")
print("\n1D array")
ar=np.array([1,2,3,4,5])
print(ar)
print("\n1D array after insertion")
ar=np.insert(ar,3,[9])
print(ar)
print("\n2D array")
ar1=np.array([[1,2],[4,5],[7,8]])
print(ar1)
print("\n2D Array after insertion")
ar1=np.insert(ar1,1,[2,3],axis=0)
print(ar1)