import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")
from scipy.integrate import odeint

mu = 0.5
ax = plt.gca()

def Orbit(initial, mu, colour, label):
    #Data for plotting
    t=np.arange(0.0,20.0,0.001)  # time steps

    def motion(state ,t):
        x, y, vx, vy = state  # unpack state vector
        xdot = vx
        ydot = vy
        vxdot = -((1-mu)*(x+mu)/((x+mu)**2 + y**2)**(3/2)) - (mu*(x+mu-1))/(((x+mu-1)**2 + y**2)**(3/2)) - x + 2*vy
        vydot = -((y*(1-mu)/(((x+mu)**2 + y**2)**(3/2)))) - ((y*mu)/(((x+mu-1)**2 + y**2)**(3/2))) - y - 2*vx
        return xdot, ydot, vxdot, vydot

    #Plot Flow Lines:
    states=odeint(motion,initial,t)
    
    flow=plt.plot(states[:,0],states[:,1],str(colour), label=label)[0]


size = 10
#Plot Orbits
Orbit([0.80, 0.10, -1.00, 0.00], mu, 'b', label=r'$v_x=-1.00$')
Orbit([0.80, 0.10, -1.10, 0.00], mu, 'r', label=r'$v_x=-1.10$')
Orbit([0.80, 0.10, -1.20, 0.00], mu, 'g',label=r'$v_x=-1.20$')

#Plot Masses
plt.plot(-mu,0, 'ko' ,markersize=((1 - mu)*size))
plt.plot(1 - mu,0, 'ko', markersize=(mu * size))

#Labels
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

plt.show()



