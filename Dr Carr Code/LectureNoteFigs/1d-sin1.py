
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
t = np.arange(-3.5, 7.0, 0.01)
s = np.sin(t)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$x$",fontsize=12)
ax.set_ylabel("$\dot{x}=f(x)$",fontsize=12)
ax.set_xticks([-np.pi,0,np.pi,2*np.pi])
ax.set_xticklabels(["$-\pi$","$0$","$\pi$","$2\pi$"])
ax.set_yticks([-1.0,-0.5,0,0.5,1.0])

ax.plot(-np.pi,0,'bo',markersize=15)
ax.plot(0,0,'bo',fillstyle='none',markersize=15)
ax.plot(np.pi,0,'bo',markersize=15)
ax.plot(2*np.pi,0,'bo',fillstyle='none',markersize=15)

ax.arrow(0, 0, np.pi/2, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(0, 0, -np.pi/2, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(2*np.pi, 0.0, -np.pi/2, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(2*np.pi, 0.0, 0.5, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(-np.pi, 0.0, -0.5, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')

ax.set_title("Flow diagram for $\dot{x}=\sin(x)$")

fig.savefig("1d-sin1.pdf")
plt.show()

