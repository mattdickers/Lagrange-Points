from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")

cmaps = ['plasma', 'rainbow', 'gist_rainbow']
cmapType = cmaps[0]
top = 0
axes = 0


def potential(x, y, mu):
    return (0.5*(x**2 + y**2)) + ((1-mu)/np.sqrt((x + mu)**2 + y**2)) + (mu/np.sqrt((x + mu - 1)**2 + y**2))

mu=0.25
x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)

x, y = np.meshgrid(x, y)
z = potential(x, y, mu)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x, y, z, 50, cmap=cmapType)
ax.invert_xaxis()
ax.set_xlabel(r'$x$', fontsize=15)
ax.set_ylabel(r'$y$', fontsize=15)

if axes == 'On':
    ax.set_xlabel(r'$x$', fontsize=15)
    ax.set_ylabel(r'$y$', fontsize=15)
    ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16)
    if top != 1:
        ax.set_zlabel(r'$z$', fontsize=15)
    ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16)
else:
    plt.axis('off')

if top == 1:
    ax.view_init(elev=90., azim=90)
    ax.w_zaxis.line.set_lw(0.)
    ax.set_zticks([])
    dist = 7
else:
    ax.set_zlabel(r'$z$', fontsize=15)

Lx = np.array([x[14][17], x[14][24], x[14][7], x[8][17], x[20][17]])
Ly = np.array([y[14][17], y[14][24], y[14][7], y[8][17], y[20][17]])
ax.scatter(Lx[0], Ly[0]+0.075, 2, 'filled', color='pink', label=r'$L_1$')
ax.scatter(Lx[1], Ly[1]+0.075, 2, 'filled', color='pink', label=r'$L_2$')
ax.scatter(Lx[2], Ly[2]+0.075, 2, 'filled', color='pink', label=r'$L_3$')
ax.scatter(Lx[3], Ly[3]+0.075, 2, 'filled', color='pink', label=r'$L_4$')
ax.scatter(Lx[4], Ly[4]+0.075, 2, 'filled', color='pink', label=r'$L_5$')

if axes:
    plt.legend(loc='center left')
plt.savefig('pinkplot3D.png')
#plt.show()
