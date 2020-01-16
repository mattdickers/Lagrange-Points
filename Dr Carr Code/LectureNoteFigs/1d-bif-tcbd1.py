# pitchfork bifurcation diagram 1 (dx/dt = sx+x^3)

import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r1 = np.arange(-1.0, 0.0, 0.001)
r2 = np.arange(0, 01.0, 0.001)
f1a=0.0*r1
f1b=r1
f2a=0.0*r2
f2b=r2

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.plot(r1, f1a,color='royalblue',linewidth=3)
ax.plot(r1, f1b,color='royalblue',linestyle='--',linewidth=2)
ax.plot(r2, f2a,color='royalblue',linestyle='--',linewidth=4)
ax.plot(r2, f2b,color='royalblue',linewidth=2)

ax.grid()


ax.set_xlabel("$r$",fontsize=16)
ax.set_ylabel("$x^*$",fontsize=16)
ax.yaxis.labelpad=-5
#ax.set_xticks([-2,-1,0,1,2])

ax.text(0.5,0.55,'stable',fontsize=16,rotation=35)
ax.text(-0.5,-0.37,'unstable',fontsize=16,rotation=35)
ax.text(-0.5,0.05,'stable',fontsize=16)
ax.text(0.3,0.05,'unstable',fontsize=16)

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
#ax.set_xlim([-1.1,1.1])

ax.set_title("Transcritical Bifurcation")

fig.savefig("1d-bif-tcbd1.pdf")
plt.show()

