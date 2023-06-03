# Numpy - Numerical Python invented in 2005

# list -> Array

import numpy as np

arr1 = np.array(90)   # 0 Dimensional
print(arr1)   # 90
print(type(arr1))   # <class 'numpy.ndarray'>

arr2 = np.array([12, 90, 89, 78, 67, 56])    # 1 Dimensional
print(arr2)  # [12 90 89 78 67 56]
print(arr2.ndim)   # 1

arr3 = np.array([[1,2,3] , [5,6,7]])   # 2 Dimensional
print(arr3)  # [[1 2 3]
             # [5 6 7]]
print(arr3.ndim)   # 2

arr4 = np.array((1, 90, 90, 89, 78))
print(type(arr4))   # <class 'numpy.ndarray'>

arr5 = np.array([[[1,2,3], [7,8,9]], [[1,3,6], [7,8,2]]])

print(arr5)  # [[[1 2 3]
#               [7 8 9]]

#               [[1 3 6]
#                [7 8 2]]]

print(arr5.ndim)   # 3 Diminsional

arr6 = np.array([[[[1,2]]]], ndmin=3)
print(arr6.ndim)   # returns Dimension of Particular Array

arr7 = np.array([1,2,3,4,5], ndmin=5)
print(arr7)    # [[[[[1 2 3 4 5]]]]]

# Locality of Reference

print(np.__version__)   # 1.23.3


array1 = np.array([1, 28, 90, 56, 34, 45])
print(array1[1])  # 28
print(array1[-3])  # 56


array2 = np.array([[1, 28, 90, 56, 34, 45], [35, 89, 23, 14, 56, 67]])

print(array2[1,2])   # 23
print(array2[0,4])   # 34
print(array2[1,-4])   # 23

array3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[75,83,91],[123,13,122]]])

print(array3[1,0, 2])   # 9
print(array3[0, 0, 2])   # 3
print(array3[2,1,0])   # 123
print(array1[3:])   # [56 34 45]

# print(array2[])