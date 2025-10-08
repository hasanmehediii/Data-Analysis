import numpy as np

array0 = np.array('A')
array1 = np.array(['A', 'B', 'C'])
array2 = np.array([['A', 'B', 'C'], ['D', 'E', 'F']])
array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F']],
                   [['G', 'H', 'I'], ['J', 'K', 'L']]])

print(array0.ndim)
print(array1.ndim)
print(array2.ndim)
print(array3.ndim)
print(array3.shape)

print(array3[0][0][0])
print(array3[0, 0, 0])
print(array3[1][0][2])
print(array3[1, 0, 2])