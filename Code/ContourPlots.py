from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")

cmaps = ['plasma', 'rainbow', 'gist_rainbow']

def potential(x, y, mu):
    return (0.5*(x**2 + y**2)) + ((1-mu)/np.sqrt((x + mu)**2 + y**2)) + (mu/np.sqrt((x + mu - 1)**2 + y**2))

mu=0.5
x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)

x, y = np.meshgrid(x, y)
z = potential(x, y, mu)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x, y, z, 50, cmap=cmaps[0])
ax.set_xlabel(r'$x$', fontsize=15)
ax.set_ylabel(r'$y$', fontsize=15)
ax.set_zlabel(r'$z$', fontsize=15)
ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16)
plt.show()