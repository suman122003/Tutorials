import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xm, ym = np.meshgrid(x, y)
Z = np.sin(np.sqrt(xm**2+ym**2))

#fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(xm, ym, Z, 50, cmap='binary')
plt.show()