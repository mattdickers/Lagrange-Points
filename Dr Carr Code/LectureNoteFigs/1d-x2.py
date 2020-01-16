
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x = np.arange(-2.2, 2.2, 0.01)
f = x**2-1

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, f)

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$x$",fontsize=12)
ax.set_ylabel("$\dot{x}=f(x)$",fontsize=12)
ax.set_xticks([-2,-1,0,1,2])

# ax.set_yticks([-1.0,-0.5,0,0.5,1.0])

ax.plot(-1,0,'bo',markersize=15)
ax.plot(1,0,'bo',fillstyle='none',markersize=15)


ax.arrow(1, 0, -0.5, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(1, 0, 0.6, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(1, 0.0, -1.3, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(-2.2, 0.0, 0.4, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')

ax.set_title("Flow diagram for $\dot{x}=x^2-1$")

fig.savefig("1d-x2.pdf")
plt.show()

