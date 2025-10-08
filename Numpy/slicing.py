import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step]

print(array[1:3])
# [[ 5  6  7  8]
#  [ 9 10 11 12]]

print(array[0:4:2])
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

print(array[:, 1:3])
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

print(array[::-2])
# [[13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

print(array[:, 1])
# [ 2  6 10 14]

print(array[:, -1])
# [ 4  8 12 16] 