from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


mu=0.5
top = 1

def potential(x, y, mu):
    return (0.5 * (x ** 2 + y ** 2)) + ((1 - mu) / np.sqrt((x + mu) ** 2 + y ** 2)) + (
                mu / np.sqrt((x + mu - 1) ** 2 + y ** 2))

x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)

x, y = np.meshgrid(x, y)
z = potential(x, y, mu)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x, y, -z, 50)
ax.invert_xaxis()
ax.set_xlabel(r'$x$', fontsize=15)
ax.set_ylabel(r'$y$', fontsize=15)
if top == 1:
    ax.view_init(elev=90., azim=90)
    ax.w_zaxis.line.set_lw(0.)
    ax.set_zticks([])
    ax.dist = 7
else:
    ax.set_zlabel(r'$z$', fontsize=15)
ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16)

plt.show()
