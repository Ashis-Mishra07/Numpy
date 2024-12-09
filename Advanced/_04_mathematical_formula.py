import numpy as np


# Sigmoid
def sigmoid(array):
  return 1/(1 + np.exp(-(array)))


a = np.arange(100)

sigmoid(a)


# Mean Squared Error

'''

for the two set of array with actual and predicted value 
it will calculate the difference between the two arrays and then square it , 
it will give me an array of numbers , then it will calculate its mean .

'''

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
  return np.mean((actual - predicted)**2)

mse(actual,predicted)


# Binary Cross Entropy

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def bce(actual, predicted):
    epsilon = 1e-15  # Small value to avoid log(0)
    predicted = np.clip(predicted, epsilon, 1 - epsilon)  # Clip predicted values to [epsilon, 1-epsilon]
    return -np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))


bce(actual, predicted)


