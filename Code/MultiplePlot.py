import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")
from scipy.integrate import odeint
from matplotlib.collections import LineCollection

from tkinter.colorchooser import *

def RGBtoFloat(rgb):
    return (int(rgb[0])/255, int(rgb[1])/255, int(rgb[2])/255)

masses = True
axes = False
velocity = True
darkTheme = True

if not velocity:
    #colour = (255, 255, 0)
    colour = askcolor()[0]
else:
    colour = (0, 0, 0)

if darkTheme:
    plt.style.use('dark_background')
    pointColour = 'w'
else:
    pointColour = 'k'

mu = 2.5289e-5
ax = plt.gca()

def Orbit(initial, mu, colour):
    #Data for plotting
    t=np.arange(0.0,100.0,0.001)  # time steps

    def motion(state ,t):
        x, y, vx, vy = state  # unpack state vector
        xdot = vx
        ydot = vy
        vxdot = -((1-mu)*(x+mu)/((x+mu)**2 + y**2)**(3/2)) - (mu*(x+mu-1))/(((x+mu-1)**2 + y**2)**(3/2)) - x + 2*vy
        vydot = -((y*(1-mu)/(((x+mu)**2 + y**2)**(3/2)))) - ((y*mu)/(((x+mu-1)**2 + y**2)**(3/2))) - y - 2*vx
        return xdot, ydot, vxdot, vydot

    #Plot Flow Lines:
    states=odeint(motion,initial,t)

    if velocity:
        #Plot with velocity gradient:
        vel = np.sqrt(np.square(states[:,2]) + np.square(states[:,3]))
        points = np.array([states[:,0], states[:,1]]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        norm = plt.Normalize(vel.min(), vel.max())
        lc = LineCollection(segments, cmap='plasma', norm=norm)
        lc.set_array(vel)
        lc.set_linewidth(0.75)
        line = ax.add_collection(lc)
        if axes:
            cbar = plt.colorbar(line, ax=ax)
            cbar.ax.set_ylabel('Magnitude of Veclocity', rotation='vertical', fontsize=15)

    else:
        flow=plt.plot(states[:,0],states[:,1], color=RGBtoFloat(colour), linewidth=0.75)[0]


size = 10
#Plot Orbits
Orbit([-1, 0, 1, 0], mu, colour)


#Plot Masses
if masses:
    plt.plot(-mu,0, pointColour+'o' ,markersize=((1 - mu)*size))
    plt.plot(1 - mu,0, pointColour+'o', markersize=(mu * size))

#Labels
if axes:
    plt.grid()
    plt.legend(loc='upper right')
    plt.title(r"Plot of the Orbit of a mass $m_3$", fontsize=16)
    plt.xlabel("$x$", fontsize=15)
    plt.ylabel("$y$", fontsize=15)
    textstr = '\n'.join((
            r'Initial Conditions',
            r'$x=0.80$',
            r'$y=0.10$',
            r'$v_y=0.00$',
            r'$\mu=0.50$'))

    props = dict(boxstyle='round', facecolor='white', alpha=0.5)

    plt.text(0.05, 0.95, textstr, transform=ax.transAxes,
            verticalalignment='top', bbox=props)
else:
    plt.axis('off')

plt.show()



