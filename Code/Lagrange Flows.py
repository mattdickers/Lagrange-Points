import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Data for plotting
global mu
mu = 0.7

def f(state ,t):
    x, y, vx, vy = state  # unpack state vector
    xdot = vx
    ydot = vy
    vxdot = -((1-mu)*(x+mu)/((x+mu)**2 + y**2)**(3/2)) - (mu*(x+mu-1))/(((x+mu-1)**2 + y**2)**(3/2)) - x + 2*vy
    vydot = -((y*(1-mu)/(((x+mu)**2 + y**2)**(3/2)))) - ((y*mu)/(((x+mu-1)**2 + y**2)**(3/2))) - y - 2*vx
    return xdot, ydot, vxdot, vydot

t=np.arange(0.0,20.0,0.001)  # time steps

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)

fig, ax = plt.subplots()

ax.grid()
#plt.axvline(0,color='black')
#plt.axhline(0,color='black')

# flow lines from different intitial conditions

#more or less separatrix
initial1=[0.1, 0, 0, 10]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
#add_arrow(flow1,position=0.4)
#add_arrow(flow1,position=1.75)

ax.set_xlabel("$x$",fontsize=12)
ax.set_ylabel("$y$",fontsize=12)

ax.plot(3,0,'bo',markersize=15)
ax.plot(0,2,'bo',markersize=15)
ax.plot(0,0,'bo',fillstyle='none',markersize=15)
ax.plot(1,1,'bo',fillstyle='none',markersize=15)

ax.set_title(r"Flow Diagram of Object placed at N",fontsize=16)

#fig.savefig("2d-rabbits-sheep.pdf")
plt.show()

