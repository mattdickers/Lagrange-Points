# saddle node bifurcation diagram 1 (dx/dt = r+x^2)

import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r = np.arange(-1.0, 0.0, 0.001)
f1 = np.sqrt(-r)
f2= -np.sqrt(-r)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(r, f1,color='royalblue',linestyle='--')
ax.plot(r, f2,color='royalblue')

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$r$",fontsize=16)
ax.set_ylabel("$x^*$",fontsize=16)
ax.yaxis.labelpad=-5
#ax.set_xticks([-2,-1,0,1,2])

ax.text(-0.5,0.8,'unstable',fontsize=16,rotation=-35)
ax.text(-0.5,-0.7,'stable',fontsize=16,rotation=30)

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
ax.set_xlim([-1.1,1.1])

ax.set_title("Bifurcation diagram for $\dot{x}=r+x^2$",fontsize=16)

fig.savefig("1d-bif-snbd1.pdf")
plt.show()

