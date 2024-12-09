import numpy as np


# 1D array
for i in a1:
    print(i) # print all the elements of the array

for i in a2:
    print(i) # print all the rows of the array in the form of array

for i in a3:
    print(i) # print all the matrix of the array in the form of array


# for iterating all the elements of the array
for i in np.nditer(a3):
    print(i) # print all the elements of the array no matters about the dimension

