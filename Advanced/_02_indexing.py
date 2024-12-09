# This will help you if u need custom indexings

# Fancy Indexing
# This is used to get the data from array based on custom index

a[:,[0,2,3]] # This will return all rows and 0,2,3 columns

a[[0,2,3]]  # This will return 0,2,3 rows and all columns
a[[0,2,3],:]  


# Boolean Indexing

# This is used to filter the data based on some condition

a = np.random.randint(1,100,24).reshape(6,4)
# randint will take ( start , end , how_many_numbers ) and reshape it  

a > 50 # This will return a matrix fill with True or False based on condition i.e ele are greater than 50
a[ a>50 ]  # This will return all elements greater than 50 in 1D array
a[ a%2==0 ] # This will return all elements which are even in 1D array

# find all numbers greater than 50 and are even
a[  (a > 50) & (a % 2 == 0) ]  # and is logical and  , & is bitwise and 











