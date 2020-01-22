import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x = np.arange(-1.5, 1.5, 0.01)
f1 = -x**2

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, f1)


ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$x$",fontsize=16)
ax.set_ylabel("$\dot{x}$",fontsize=16)
ax.yaxis.labelpad=-2
#ax.set_xticks([-2,-1,0,1,2])

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
ax.set_ylim([-2.0,0.5])

#ax.plot(-1,-0.666,'bo',markersize=15)
#ax.plot(-1,0,'bo',fillstyle='none',markersize=15)
plt.text(0,0,u'\u25D0',size=18,ha='center',va='center',rotation=180)
#ax.plot(0,0,'bo',markersize=15)
ax.arrow(0.0, 0, -0.5,0, head_width=0.2, head_length=0.1, fc='k', ec='k')
ax.arrow(1.2, 0, -0.5,0, head_width=0.2, head_length=0.1, fc='k', ec='k')
#ax.arrow(1.0, 0, -0.5,0, head_width=0.2, head_length=0.1, fc='k', ec='k')

ax.set_title("$r=0$",fontsize=16)

fig.savefig("1d-bif-tc2.pdf")
plt.show()
