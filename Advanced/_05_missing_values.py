import numpy as np


# Working with missing values -> np.nan
a = np.array([1,2,3,4,np.nan,6])

np.isnan(a) # return the boolean array where the nan values are present

a[~np.isnan(a)] # remove all the nan values from the array



