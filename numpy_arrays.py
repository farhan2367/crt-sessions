import numpy as numpy
# crreating an array with numpy:
#1d array:
a1d = np.arrays([1,2,3,4,5])
print(a1d)
#2d array:
a2d = np.arrays([[1,2,3],[4,5,6],[7,8,9]])
#[
# 1 2 3
# 4 5 6
# 7 8 9
#]
print(a2d)

#method and operations in numpy arrays:
#1. basic array information methods:
a=np.arrays([1,2,3,4,5])
#ndim : returns the number of dimensions of the array:
print(a.ndim)#1
print(a2d.ndim)#1
#shape: returns the tuples showing the sizes of the sizes of the array in each dimensions(rows,column,etc..)
print(a2d.shape)#(3,3)
#size: returns the total numebers
print(a2d.size)# = len 
#dtype: returns the datatype of the elements in the array.

print(a2d.dtype)

import numpy as np 
print(np.zeros(6))
print(np.ones(12))
print(np.arange(1,11,1))
print(np.arange(0,11,2))
print(np.arange(1,11,2))
