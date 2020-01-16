# pitchfork bifurcation diagram 1 (dx/dt = sx+x^3)

import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r = np.arange(0.0, 1.0, 0.001)
f1 = np.sqrt(r)
f2= -np.sqrt(r)
f3=0.0*r
rp = np.arange(-1.0, 0.0, 0.01)
f4=0.0*rp

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.plot(r, f1,color='royalblue',linewidth=2)
ax.plot(r, f2,color='royalblue',linewidth=2)
ax.plot(r, f3,color='royalblue',linestyle='--',linewidth=4)
ax.plot(rp, f4,color='royalblue',linewidth=3)

ax.grid()


ax.set_xlabel("$s$",fontsize=16)
ax.set_ylabel("$x^*$",fontsize=16)
ax.yaxis.labelpad=-5
#ax.set_xticks([-2,-1,0,1,2])

ax.text(0.5,0.75,'stable',fontsize=16,rotation=30)
ax.text(0.5,-0.6,'stable',fontsize=16,rotation=-30)
ax.text(0.2,0.05,'unstable',fontsize=16)
ax.text(-0.55,0.05,'stable',fontsize=16)

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
ax.set_xlim([-1.1,1.1])

ax.set_title("Bifurcation diagram for super-critical pitchfork bifurcation",fontsize=16)

fig.savefig("1d-bif-pfbd2.pdf")
plt.show()

