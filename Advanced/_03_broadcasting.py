
'''

The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

The smaller array is “broadcast” across the larger array so that they have compatible shapes.

'''


# Diff Shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)

print(a)
print(b)

print(a+b)

# BroadCasting Rules 

'''
1. Make the two arrays have the same number of dimensions.

If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.
2. Make each dimension of the two arrays the same size.

If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.


 In short the shorter dimension array begin to enlarge and repeat itself in
 such a way that it matches the shape of the larger array.
 Then as per ur desired operation the two arrays are operated upon.

'''

'''

for example is broadcasting rules violates

 an array with size (3,4) and another array with size(3)

 NOTE : 1 is to always added in the front .

 -> the size(3) will become (1,3) and now
    it will increase by (3,3) which is not matching with the 1st array
    hence boardcasting is not possible at any cost .

 an array with size (3,4) and another array with size(4,3)

 -> size there is no 1 in the dimension of any array so growing will not being done
    hence broadcasting is not possible .

'''


