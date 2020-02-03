import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")
from scipy.integrate import odeint
import random

from matplotlib.collections import LineCollection

def LagrangeFlowPlot(initial, mu):
    #Data for plotting
    t=np.arange(0.0,20.0,0.001)  # time steps

    def motion(state ,t):
        x, y, vx, vy = state  # unpack state vector
        xdot = vx
        ydot = vy
        vxdot = -((1-mu)*(x+mu)/((x+mu)**2 + y**2)**(3/2)) - (mu*(x+mu-1))/(((x+mu-1)**2 + y**2)**(3/2)) - x + 2*vy
        vydot = -((y*(1-mu)/(((x+mu)**2 + y**2)**(3/2)))) - ((y*mu)/(((x+mu-1)**2 + y**2)**(3/2))) - y - 2*vx
        return xdot, ydot, vxdot, vydot

    fig, ax = plt.subplots()
    ax.grid()

    #Plot Flow Lines:
    states=odeint(motion,initial,t)

    #Plot with velocity gradient:
    vel = np.sqrt(np.square(states[:,2]) + np.square(states[:,3]))
    points = np.array([states[:,0], states[:,1]]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = plt.Normalize(vel.min(), vel.max())
    lc = LineCollection(segments, cmap='plasma', norm=norm)
    lc.set_array(vel)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)
    cbar = fig.colorbar(line, ax=ax)
    cbar.ax.set_ylabel('Veclocity', rotation='vertical', fontsize=15)

    #Can be used to plot if not using velcoity gradient:
    #flow=ax.plot(states[:,0],states[:,1])[0]


    #Plot Other Masses:
    ax.plot(-mu,0,'bo',markersize=10)
    ax.plot(1 - mu,0,'bo',markersize=10)

    ax.set_title(r"Flow Diagram of the mass $m_3$",fontsize=16)
    ax.set_xlabel("$x$",fontsize=15)
    ax.set_ylabel("$y$",fontsize=15)

    textstr = '\n'.join((
        r'Initial Conditions',
        r'$x=%.2f$' % (initial[0],),
        r'$y=%.2f$' % (initial[1],),
        r'$v_x=%.2f$' % (initial[2],),
        r'$v_y=%.2f$' % (initial[3],),
        r'$\mu=%.2f$' % (mu,)))

    props = dict(boxstyle='round', facecolor='white', alpha=0.5)

    ax.text(0.05, 0.95, textstr, transform=ax.transAxes,
            verticalalignment='top', bbox=props)

num = 10
for plot in range(1,num + 1):

    randX = random.randint(-5, 5)
    randY = random.randint(-5, 5)
    randVX = random.randint(-5, 5)
    randVY = random.randint(-5, 5)
    randMu = round(random.random(),2)

    LagrangeFlowPlot([randX, randY, randVX, randVY], randMu)

    #print("x: ",randX)
    #print("y: ",randY)
    #print("vx: ",randVX)
    #print("vy: ",randVY)
    #print("mu: ",randMu)

    plt.savefig("Plots\\"+str(plot)+".png")
    print("Plot",str(plot),"saved")