import numpy as np
import matplotlib.pyplot as plt

mu=0.5

x = np.arange(-4, 4, 0.2)
y = (((1-mu)*(x+mu))/(abs((x+mu)**3))) + ((mu*(x+mu-1))/(abs((x+mu-1)**3)))
#Split plot so that we dont have the lines between points and things

plt.plot(x,y)
y=x
plt.plot(x,y)
plt.show()