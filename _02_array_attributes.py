import numpy as np 

a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# ndim : number of dimensions
a = a1.ndim  # 1
b = a2.ndim  # 2 
c = a3.ndim  # 3

# shape : gived u the no of rows and colums 
a1.shape # ( 10, )  means 1 d array with 10 elements
a2.shape # ( 3 ,4 ) means it has 3 rows and 4 columns
a3.shape # ( 2,2,2 ) means it is with 2 x 2 x 2 dimension

# ( 2 , 2 , 2 ) means the last 2 x 2 says it has 2 rows and 2 columns 
# and the first 2 says it has 2 such 2 x 2 arrays


a1.size # gives the total no of elements in the array  i.e 10
a2.size # gives the total no of elements in the array  i.e 12

# dtype : gives the data type of the array
a1.dtype # int32
a2.dtype # float64
a3.dtype # int32

# itemsize : gives the size of each element in the array
a1.itemsize # 4 bytes since int value for each element
a2.itemsize # 8 bytes since float value for each element
a3.itemsize # 8 bytes  since float value  for each element

# 32 bit integer (int32) takes 4 bytes and 64 bits (int64) integer takes 8 bytes 

#changing data type of the array
a3.astype(np.int32) # changes the data type of the array int64 to int32



