# Here the question is why choosing numpy over python list

# In terms of SPEED

# List
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time 

start = time.time()
for i in range(len(a)):
  c.append(a[i] + b[i])
print(time.time()-start)

#Numpy
import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()
c = a + b
print(time.time()-start)

# Numpy is faster than python list
# Numpy is implemented in C so static files made whose size is fixed
# while in python list, it is implemented in python so dynamic files made whose size is not fixed

# IN Numpy , the elements are stored directly in the memomy but int python list
# the elements are stored in memory address 



# In terms of MEMORY

# Python
a = [i for i in range(10000000)]
import sys

sys.getsizeof(a) # return  bytes 

# Numpy
a = np.arange(10000000,dtype=np.int8)
sys.getsizeof(a)



'''
# NOTE


for knowing the time difference 
import time
time.time()


for knowing the memory size
import sys
sys.getsizeof()

'''









