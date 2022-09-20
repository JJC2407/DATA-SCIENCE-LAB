print("JOYAL JOSE\n21MCA026")
import numpy as np
ar=np.array([
    [2,3,4,],[6,7,5,]],dtype='complex')
row_count = len(ar[:])
col_count = len(ar[:][0])
print("\n",ar)
print("\nNumber of row and column is : ",ar.shape)
print("\nDimension of the array : ",ar.ndim)
print("\nMatrix before reshape : \n",ar)
print("\nMatrix after reshape : \n",ar.reshape(3,2))