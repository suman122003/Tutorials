# simple single plot
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 * np.exp(-x)

x=np.linspace(0,10,40)
fx = f(x)
plt.plot(x,fx)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('simple 2D plot')
plt.show()
