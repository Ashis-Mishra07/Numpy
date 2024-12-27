# plotting a 2D plot
import matplotlib.pyplot as plt
import numpy as np


# x = y
x = np.linspace(-10,10,100) # makes 100 points between -10 and 10
y = x

plt.plot(x,y)



# y = x^2
x = np.linspace(-10,10,100)
y = x**2

plt.plot(x,y)



# y = sin(x)
x = np.linspace(-10,10,100)
y = np.sin(x)

plt.plot(x,y)



# y = xlog(x)
x = np.linspace(-10,10,100)
y = x * np.log(x)

plt.plot(x,y)



# sigmoid
x = np.linspace(-10,10,100)
y = 1/(1+np.exp(-x))

plt.plot(x,y)