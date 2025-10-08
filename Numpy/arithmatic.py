import numpy as np

array = np.array([1, 2, 3])

# Scalar arithmetic operations
print(array + 2)  # [3 4 5]
print(array - 2)  # [-1  0  1]
print(array * 2)  # [2 4 6]
print(array / 2)  # [0.5 1.  1.5]
print(array ** 2) # [1 4 9]
print(array % 2)  # [1 0 1]

# Vectorized math functions
print(np.sqrt(array))  # [1.         1.41421356 1.73205081]
print(np.exp(array))   # [ 2.71828183  7.3890561 20.08553692]
print(np.log(array))   # [0.         0.69314718 1.09861229]
print(np.sin(array))  # [0.84147098 0.90929743 0.14112001]
print(np.cos(array))  # [0.54030231 -0.41614684 -0.9899925 ]
print(np.tan(array))  # [1.55740772 -2.18503986 -0.14254654]

radii = np.array([1, 2, 3])
areas = np.pi * (radii ** 2)
print(areas)  # [ 3.14159265 12.56637061 28.27433388]

# Element-wise operations between arrays
array2 = np.array([4, 5, 6])
print(array + array2)  # [5 7 9]
print(array * array2)  # [ 4 10 18]
print(array - array2)  # [-3 -3 -3]
print(array / array2)  # [0.25 0.4  0.5 ]
print(array ** array2) # [  1  32 729]
print(array % array2)  # [1 2 3]


# Comparisons operations

scores = np.array([85, 90, 78, 92, 88])
print(scores > 80)   # [ True  True False  True  True]
print(scores < 90)   # [ True False  True False  True]
print(scores >= 88)  # [False  True False  True  True]
print(scores <= 85)  # [ True False False False False]
print(scores == 88)  # [False False False False  True]
print(scores != 92)  # [ True  True  True False  True]

scores[scores >= 90] = 100
print(scores)  # [ 85 100  78 100  88]