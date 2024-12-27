import numpy as np



# Sorting
#1D Array
a = np.array([3, 1, 2, 4, 5])

np.sort(a) # do it in ascending order
np.sort(a)[::-1] # do it in descending order

#2D Array
a = np.array([[3, 1, 2], [4, 5, 6]])

np.sort(a, axis=0) # sort along the column
np.sort(a, axis=1) # sort along the row

'''

the sort function takes arguments like 
 
np.sort( array_name , axis = 0 or 1 , kind = 'quicksort' or 'mergesort' or 'heapsort' , order = None )

NOTE
The normal sort fucntion of python return a list 
The sort function of numpy return a numpy array

'''






# Append
# The numpy.append() appends values along the mentioned axis at the end of the array

#1D Array
np.append(a,200)

#2D Array
np.append(a,[[200,300,400]],axis = 0)
np.append(a,[[200],[300]],axis = 1)
np.append(b,np.ones((b.shape[0],1)),axis=1) # to append a column of ones to a 2D array b






# Concatenate
# The numpy.concatenate() function is used to concatenate two arrays

#1D Array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate((a, b))

#2D Array
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0) # concatenate along the row
np.concatenate((a, b.T), axis=1) # concatenate along the column




# Unique
# The numpy.unique() function is used to find the unique elements of an array

a = np.array([1, 2, 6, 4, 2, 3, 2])
np.unique(a)



# Expand_dims
# The numpy.expand_dims() function is used to expand the shape of an array
# If it is 1D -> can make it 2D , if 2D -> can make it 3D

a = np.array([1, 2, 3, 4, 5]) # shade will be (5,)
np.expand_dims(a,axis=0) # to make a 1D array to 2D array shape will be (1,n)
np.expand_dims(a,axis=1) # to make a 1D array to 2D array shape will be (n,1)



# Where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied
np.where(a>50) # returns the indices where val>50 in an array format

'''
replace the values in the array where the condition is satisfied
np.where(condition, value if true, value if false)

means if the condition satisfied then what operation
      if not satisfied then what operation
      
'''
np.where(a>50,0,a) # replace all values > 50 with 0 in the array a



# Argmax and Argmin
# The numpy.argmax() function returns the indices of the maximum value along an axis
# The numpy.argmin() function returns the indices of the minimum value along an axis

a = np.array([[1, 2, 3], [4, 5, 6]])
np.argmax(a) # returns the index of the maximum value in the array
np.argmax(a, axis=0) # returns the indices of the maximum values along the column
np.argmax(a, axis=1) # returns the indices of the maximum values along the row

'''

array([[12, 52, 42,  6],
       [29, 18, 47, 55],
       [61, 93, 83,  9],
       [38, 63, 44, 85],
       [ 8, 87, 31, 72],
       [40, 71,  2,  7]])

np.argmax(a) # returns 10
np.argmax(a, axis=0) # returns [2, 4, 2, 3]
np.argmax(a, axis=1) # returns [1, 2, 1, 3, 1, 1]

'''




# Cumsum and Cumprod
# The numpy.cumsum() function returns the cumulative sum of the elements along the given axis
# The numpy.cumprod() function returns the cumulative product of the elements along the given axis

a = np.array([[1, 2, 3], [4, 5, 6]])
np.cumsum(a) # returns the cumulative sum of the elements in the array
'''
In 2D array if axis is not mentioned then it will return the cum sum
of all the elements in the 1D array .
'''
np.cumsum(a, axis=0) # returns the cumulative sum of the elements along the column
np.cumsum(a, axis=1) # returns the cumulative sum of the elements along the row

np.cumprod(a) # returns the cumulative product of the elements in the array





# Percentile 
# The numpy.percentile() function is used to compute the nth percentile of the given data (array elements) along the specified axis
# In short how many are below the given value
np.percentile(a,100) # returns the maximum value in the array
np.percentile(a,0) # returns the minimum value in the array
np.percentile(a,50) # returns the median value in the array




# Histogram
# The numpy.histogram() function is used to compute the histogram of a set of data
# It returns the frequency of the elements in the array according to the bin size

np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100])
# It will return the number of ele present in between the bin size of 10 i.e from 0 to 10 



# Correlation Coefficient
# The numpy.corrcoef() function is used to compute the Pearson correlation coefficient
# tells how the two quantities are co related , how much they are dependent 

'''

if corr = 0 ; the quantities are independent
if corr = 1 ; the quantities are dependent and are in the same direction
if corr = -1 ; the quantities are dependent and are in the opposite direction


'''
salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])

np.corrcoef(salary,experience)
'''  
        salary   exp
salary     1      0.2
exp       0.2      1

'''



# isin
# The numpy.isin() function is used to check for multiple values in an array

items = [10,20,30,40,50,60,70,80,90,100]
np.isin(a,items) # return true if present else false in the form of an boolean array
a[np.isin(a,items)] # return the values which are present in the items list in a array



# Flip
# The numpy.flip() function is used to reverse the order of elements in an array
#1D array
a = np.array([1, 2, 3, 4, 5])
np.flip(a) # reverse the order of elements in the array
#2D array
np.flip(a) # reverse the order row and col wise both
np.flip(a, axis=0) # reverse the order of elements along the row
np.flip(a, axis=1) # reverse the order of elements along the column



# Put 
# The numpy.put() function is used to replace specified elements of an array with given values
a = np.array([1, 2, 3, 4, 5])
np.put(a, [0, 2], [-44, -55]) # replace the elements at index 0 and 2 with -44 and -55 respectively

'''

np.put(array_name, [index], [values])

'''




# Delete
# The numpy.delete() function returns a new array with the deletion 
# of sub-arrays along with the mentioned axis.

np.delete(a, 1) # delete the element at index 1
np.delete(a, [1, 3]) # delete the elements at index 1 and 3










