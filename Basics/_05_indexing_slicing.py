import numpy as np

# INDEXING

# for 1D array the indexing will be same as list
# left to right start from 0 and right to left start from -1

a1[3] # return the third index value element

# for 2D array
a1[2,3] # return the element at 2nd row and 3rd column

array([[[0, 1],
        [2, 3]],

       [[4, 5],
        [6, 7]]])


# to get the element 5 
a3[1,0,1] # 1-> second matrix, 0-> first row, 1-> second column


# SLICING

# for 1D array the slicing will be same as list
a1[2:5] # return the element from 2 to 4 index

# for 2D array
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

a2[0, : ]  # return the first row with all the columns
a2[ : , 1] # return the second column
a2[0:2, 1:3] # return the first two rows and second and third column

a2[1: , 1:3] # return  5 6 
#                      9 10


# for 3D array
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])

a3[1] # returns you the middle array
a3[::2] # return the first and last matrix

