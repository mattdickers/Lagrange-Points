# saddle node bifurcation diagram 1 (dx/dt = r+x^2)

import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x = np.arange(-2.5, 2.5, 0.01)
f1 = x-x**3/3

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, f1)


ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$x$",fontsize=16)
ax.set_ylabel("$U(x)$",fontsize=16)
ax.yaxis.labelpad=-2
#ax.set_xticks([-2,-1,0,1,2])

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
#ax.set_xlim([-1.1,1.1])

ax.plot(-1,-0.666,'bo',markersize=15)
ax.plot(1,0.666,'bo',fillstyle='none',markersize=15)

ax.set_title("$r<0$",fontsize=16)

fig.savefig("1d-bif-snex1.pdf")
plt.show()

