import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)


# Scaler Operations
a1 * 2 # multiplies every element for a1 with 2
a1 ** 2 # takes the power of every element in the array
   # all the relational operators can be used in the same way
a1 > 5 # checks every element from the array and in the matrix format makes it true or false accordingly
a1 == 15 

# Vector Operations
a1 + a2 # adds the elements of the two arrays only if the dimensions are same
a1 - a2 # subtracts the elements of the two arrays only if the dimensions are same
a1 ** a2 




