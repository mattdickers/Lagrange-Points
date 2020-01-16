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


ax.set_xlabel("$x$",fontsize=12)
ax.set_ylabel("$y$",fontsize=12)

ax.plot(3,0,'bo',markersize=15)
ax.plot(0,2,'bo',markersize=15)
ax.plot(0,0,'bo',fillstyle='none',markersize=15)
ax.plot(1,1,'bo',fillstyle='none',markersize=15)

#ax.text(-0.2,0.75,r'$\theta^*=\pi/2$',fontsize=16)
#ax.text(-1.55,-0.05,r'$\theta^*=\pi$',fontsize=16)

#ax.set_aspect('equal')
ax.set_xlim([-0.1,3.6])
ax.set_ylim([-0.1,2.6])

ax.arrow(0, 0, 0.3, 0.3, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(0, 0, 0.1, 0.4, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(0, 0, 0.4, 0.1, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')

ax.arrow(3, 0.4, 0, -0.3, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(3.3, 0.3, -0.2, -0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(2.7, 0.3, 0.2, -0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')

ax.arrow(0.4, 2, -0.3, 0, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(0.3, 2.3, -0.2, -0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(0.3, 1.7, -0.2, 0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')

ax.arrow(1, 1, -0.2, 0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(1, 1, 0.2, -0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(0.7, 0.7, 0.2, 0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')
ax.arrow(1.3, 1.3, -0.2, -0.2, head_width=0.05, head_length=0.1, fc='royalblue', ec='royalblue',color='royalblue')




ax.set_title(r"Fixed points and their stabilities",fontsize=16)

fig.savefig("2d-just-nodes.pdf")
plt.show()

