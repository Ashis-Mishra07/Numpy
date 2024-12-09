import numpy as np



# transpose the array / matrix / tensor
np.transpose(a2)
a2.T 




# ravel the array
a2.ravel() # it basically convert any nD matrix into 1D array
a3.ravel()






# Stacking  the array

# suppose there is a matrix 3 x 3 and another matrix 3 x 3
# we can stack them horizontally or vertically

# Horizontal stacking
np.hstack((a2,a3)) # it will stack the array horizontally
# Vertical stacking
np.vstack((a2,a3)) # it will stack the array vertically

np.hstack((a2,a3,a2,a3)) # we can stack multiple array horizontally




# Splitting the array

# suppose there is a matrix 3 x 3
# we can split them horizontally or vertically but it can be done in equal parts only 

# Horizontal splitting
np.hsplit(a2,2) # it will split the array horizontally into 2 parts 
# Vertical splitting
np.vsplit(a2,3) # it will split the array vertically into 3 parts

# NOTE : the vsplit will cut the array horizontally and hsplit will cut the array vertically






