import numpy as np

a1 = np.random.random((3,3))
a1 = np.round(a1*100)

a1
([
    [43., 28., 71.],
    [27., 93., 36.],
    [31., 18.,  7.]
    
])


# max ,min ,sum ,prod of the array
np.max(a1) # 93.0
np.min(a1) # 7.0
np.sum(a1) # 354.0
np.prod(a1) # product of all element of the array

# max , min ,prod , sum  from every row | col
np.max(a1,axis=0) # give me an array with max from every column
np.max(a1,axis=1) # give me an array with max from every row 


# mean of the array
np.mean(a1) # also have the flexibility to calculate column wise or row wise
np.median(a1) # median of the array

# dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

np.dot(a2,a3) # for dot product the no of columns in the first array should be equal to the no of rows in the second array


# log and exponents
np.log(a1)
np.exp(a1)

# round/floor/ceil

np.ceil(np.random.random((2,3))*100)
np.round(np.random.random((2,3))*100)
np.floor(np.random.random((2,3))*100)

