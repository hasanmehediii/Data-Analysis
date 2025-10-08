import numpy as np

# Broadcasting allows numpy to perform operations on arrays of different shapes
# in a way that would not be possible with standard arithmetic operations.

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape) # (1, 4)
print(array2.shape) # (4, 1)

print(array1 * array2)
# [[ 1  2  3  4]
#  [ 2  4  6  8]
#  [ 3  6  9 12]    
#  [ 4  8 12 16]]