import numpy as np
import matplotlib.pyplot as plt

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
theta1 = np.arange(0,np.pi,0.01)
x1=np.cos(theta1)
y1=np.sin(theta1)
theta2= np.arange(np.pi,2*np.pi,0.01)
x2=np.cos(theta2)
y2=np.sin(theta2)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
circle_top=ax.plot(x1, y1,color='royalblue')[0]
add_arrow(circle_top)
circle_bottom=ax.plot(x2, y2,color='royalblue')[0]
add_arrow(circle_bottom,direction='left')

ax.grid()

#plt.axvline(0,color='black')
#plt.axhline(0,color='black')

#ax.set_xlabel("$x$",fontsize=12)
#ax.set_ylabel("$\dot{x}=f(x)$",fontsize=12)

#ax.set_xticks([-2,-1,0,1,2])
#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
plt.axis('off')

ax.plot(-1,0,'bo',markersize=15)
ax.plot(1,0,'bo',fillstyle='none',markersize=15)

ax.text(1.12,-0.05,r'$\theta^*=0$',fontsize=16)
ax.text(-1.55,-0.05,r'$\theta^*=\pi$',fontsize=16)

ax.set_aspect('equal')

#ax.arrow(1, 0, -0.5, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
#ax.arrow(1, 0, 0.6, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
#ax.arrow(1, 0.0, -1.3, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
#ax.arrow(-2.2, 0.0, 0.4, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')

ax.set_title(r"Flow diagram ona circle for $\dot{\theta}=\sin\theta$",fontsize=16)

fig.savefig("1d-circle1.pdf")
plt.show()

