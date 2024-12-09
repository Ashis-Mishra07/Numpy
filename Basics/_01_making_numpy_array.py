
import numpy as np  # here import numpy before every line

# Create a numpy array 

''' 

1D array is called a vector
2D array is called a matrix
3D array is called a tensor

'''

#1D
a=np.array([1,2,3,4,5])
print(a)
#2D
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
#3D
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])


# Create a numpy array with zeros
a=np.zeros((2,3))
# Create a numpy array with ones
a=np.ones((2,3))
# Create a numpy array with random values
a=np.random.random((2,3))

# Create a numpy array with range
a=np.arange(1,10)
a=np.arange(1,10,2) # with step 2
a=np.arange(1,10).reshape(3,3) # reshape to 3x3


# Create a numpy array with linspace
a=np.linspace(1,10,5) # range is 1 to 10 and take 5 equaly spaced values
a=np.linspace(1,10,5,dtype=int) # range is 1 to 10 and take 5 equaly spaced values with integer type

# Create identity matrix
a=np.identity(3) # 3x3 identity matrix


