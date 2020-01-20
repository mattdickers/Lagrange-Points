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

# Data for plotting

def f(state ,t):
    x,y=state  # unpack state vector
    xdot=3*x-x**2-2*y*x
    ydot=2*y-y**2-x*y
    return xdot,ydot

t=np.arange(0.0,20.0,0.001)    # time steps

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)

fig, ax = plt.subplots()

ax.grid()
plt.axvline(0,color='black')
plt.axhline(0,color='black')

# flow lines from different intitial conditions

#more or less separatrix
initial1=[0.01,0.04295]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=0.4)
add_arrow(flow1,position=1.75)

initial1=[0.01,0.02]
states1=odeint(f,initial1,t)
flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
add_arrow(flow1,position=1.0)

#initial1=[0.0003,0.01]
#states1=odeint(f,initial1,t)
#flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
#add_arrow(flow1,position=0.2)

# more or less separatrix
#initial1=[3.5,2.4605]
#states1=odeint(f,initial1,t)
#flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
#add_arrow(flow1,position=2.0)
#add_arrow(flow1,position=0.5)

#initial1=[1.5,2.5]
#states1=odeint(f,initial1,t)
#flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
#add_arrow(flow1,position=1.0)

#initial1=[3.5,1.0]
#states1=odeint(f,initial1,t)
#flow1=ax.plot(states1[:,0],states1[:,1],color='royalblue')[0]
#add_arrow(flow1,position=3.01)

#lines along axis -- do like this to keep same style
#xa1=np.arange(0.0,3.0,0.1)
#ya1=xa1*0.0
#flow1=ax.plot(xa1,ya1,color='royalblue')[0]
#add_arrow(flow1)

#xa1=np.arange(3.5,3.0,-0.1)
#ya1=xa1*0.0
#flow1=ax.plot(xa1,ya1,color='royalblue')[0]
#add_arrow(flow1)

#ya1=np.arange(0.0,2.5,0.1)
#xa1=ya1*0.0
#flow1=ax.plot(xa1,ya1,color='royalblue')[0]

#ya1=np.arange(2.3,2.0,-0.1)
#xa1=ya1*0.0
#flow1=ax.plot(xa1,ya1,color='royalblue')[0]
#add_arrow(flow1)


#ya1=np.arange(1.2,1.4,0.1)
#xa1=ya1*0.0
#flow1=ax.plot(xa1,ya1,color='royalblue')[0]
#add_arrow(flow1)


ax.set_xlabel("$x$",fontsize=12)
ax.set_ylabel("$y$",fontsize=12)

ax.plot(3,0,'bo',markersize=15)
ax.plot(0,2,'bo',markersize=15)
ax.plot(0,0,'bo',fillstyle='none',markersize=15)
ax.plot(1,1,'bo',fillstyle='none',markersize=15)

#ax.text(-0.2,0.75,r'$\theta^*=\pi/2$',fontsize=16)
#ax.text(-1.55,-0.05,r'$\theta^*=\pi$',fontsize=16)

#ax.set_aspect('equal')

#ax.arrow(0, 0, 1.5, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k',color='royalblue')
#ax.arrow(1, 0, 0.6, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
#ax.arrow(1, 0.0, -1.3, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
#ax.arrow(-2.2, 0.0, 0.4, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')

ax.set_title(r"Connect the dots",fontsize=16)

#fig.savefig("2d-rabbits-sheep.pdf")
plt.show()

