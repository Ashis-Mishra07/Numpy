'''

Set functions

    np.union1d
    np.intersect1d
    np.setdiff1d
    np.setxor1d
    np.in1d


'''


m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

# union gives the union of the two arrays
np.union1d(m,n) # array([1, 2, 3, 4, 5, 6, 7])


# intersect gives the intersection of the two arrays
np.intersect1d(m,n)  # array([3, 4, 5])


# setdiff1d gives the difference of the two arrays 
# present in n but not in m
np.setdiff1d(n,m) # array([6, 7])


# removes the common elements from the two arrays
# rest keep as it is
np.setxor1d(m,n) # array([1, 2, 6, 7])



# return if the element is present in the array or not-> true or false
np.in1d(m,1) # array([ True, False, False, False, False])
np.in1d(m,[1,2,3]) # array([ True,  True,  True, False, False])
np.in1d(m,[1,2,3],invert=True) # array([False, False, False,  True,  True])

m[np.in1d(m,1)] # array([1])  - > return the index at which it is present
m[np.in1d(m,10)] # array([])  - > return an empty array





# CLIP

# numpy.clip() function is used to Clip (limit) the values in an array.

array([110, 530,  28,  50,  38,  37,  94,  92,   5,  30,  68,   9,  78, 2,  21])

np.clip(a,a_min=25,a_max=75)
# returns  array([75, 75, 28, 50, 38, 37, 75, 75, 25, 30, 68, 25, 75, 25, 25])

'''

if the value is excedding the max_value it will result it as max value assigned
and if the value is less than the min_value it will result it as min value assigned

'''





