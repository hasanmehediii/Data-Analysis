import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.std(array))      # Standard Deviation
# 1.4142135623730951
print(np.var(array))      # Variance
# 2.0000000000000004
print(np.mean(array))     # Mean
# 5.5
print(np.median(array))   # Median
# 5.5
print(np.min(array))      # Minimum
# 1
print(np.max(array))      # Maximum
# 10
print(np.sum(array))      # Sum
# 55
print(np.cumsum(array))   # Cumulative Sum
# [ 1  3  6 10 15 21 28 36 45 55]
print(np.prod(array))     # Product
# 3628800
print(np.cumprod(array))  # Cumulative Product
# [      1       2       6      24     120     720   5040 40320 362880 3628800]
print(np.argmin(array))   # Index of Minimum
# 0
print(np.argmax(array))   # Index of Maximum
# 9
print(np.sort(array))     # Sorted Array
# [ 1  2  3  4  5  6  7  8  9 10]
print(np.unique(array))   # Unique Elements
# [ 1  2  3  4  5  6  7  8  9 10]
print(np.percentile(array, 50))  # 50th Percentile (Median)
# 5.5
print(np.percentile(array, 90))  # 90th Percentile
# 9.5
print(np.histogram(array, bins=5))  # Histogram
# (array([2, 2, 2, 2, 2]), array([ 1. ,  2.8,  4.6,  6.4,  8.2, 10. ]))
print(np.corrcoef(array.flatten()))  # Correlation Coefficient
# [[1. 1.]
#  [1. 1.]]
print(np.cov(array.flatten()))       # Covariance
# 8.25