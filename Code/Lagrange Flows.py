import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")
from scipy.integrate import odeint

#Data for plotting
global mu
mu = 0.3
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
initial=[0.1, 0, 10, 0]
states=odeint(motion,initial,t)
flow1=ax.plot(states[:,0],states[:,1])[0]

#Plot Other Masses:
ax.plot(-mu,0,'bo',markersize=5)
ax.plot(1 - mu,0,'bo',markersize=5)

ax.set_title(r"Flow Diagram of Object placed at N",fontsize=16)
ax.set_xlabel("$x$",fontsize=15)
ax.set_ylabel("$y$",fontsize=15)

#fig.savefig("2d-rabbits-sheep.pdf")
plt.show()

