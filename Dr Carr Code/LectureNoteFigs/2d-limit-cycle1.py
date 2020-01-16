import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def add_arrow(line, position=None, direction='right', size=30, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.mean()
    # find closest index
    start_ind = np.argmin(np.absolute(xdata - position))
    if direction == 'right':
        end_ind = start_ind + 1
    else:
        end_ind = start_ind - 1

    line.axes.annotate('',
        xytext=(xdata[start_ind], ydata[start_ind]),
        xy=(xdata[end_ind], ydata[end_ind]),
        arrowprops=dict(arrowstyle="-|>", color=color),
        size=size
    )

# A stable spiral fixed point

def f(state ,t):
    x,y=state  # unpack state vector
    xdot=x*(1-x**2-y**2)-y
    ydot=y*(1-x**2-y**2)+x
    return xdot,ydot

t=np.arange(0.0,12.0,0.001)    # time steps

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)

fig, ax = plt.subplots()

ax.grid()
plt.axvline(0,color='black')
plt.axhline(0,color='black')
#plt.axis('off')
#ax.set_xticklabels([])
#ax.set_yticklabels([])
ax.set_xlim([-1.5,1.5])
ax.set_ylim([-1.5,1.5])

# flow lines from different intitial conditions

initial1=[0,0.1]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=-0.5)

initial1=[0,-0.1]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=0.5)

initial1=[1.5,0.0]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=1.2)

initial1=[0,1.5]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=0.9)

initial1=[-1.5,0.0]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=-1.2)

initial1=[0,-1.5]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=-0.9)


ax.set_xlabel("$x$",fontsize=12)
ax.set_ylabel("$y$",fontsize=12)

ax.plot(0,0,'bo',fillstyle='none',markersize=15)
#ax.plot(0,0,'bo',fillstyle='none',markersize=15)

ax.set_aspect('equal')

ax.set_title(r"Stable Limit Cycle",fontsize=16)

fig.savefig("2d-limit-cycle1.pdf")
plt.show()

