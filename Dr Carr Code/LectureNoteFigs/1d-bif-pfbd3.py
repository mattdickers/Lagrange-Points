# pitchfork bifurcation diagram 1 (dx/dt = sx+x^3)

import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r1 = np.arange(-0.4, 0.0, 0.001)
r2 = np.arange(-0.25, 0.0, 0.001)
r3 = np.arange(-0.25, 0.3, 0.001)
r4 = np.arange(0.0, 0.3, 0.001)
f1=0.0*r1
f4=0.0*r4
f2a=np.sqrt((1-np.sqrt(1+4*r2))*0.5)
f2b=-np.sqrt((1-np.sqrt(1+4*r2))*0.5)
f3a=np.sqrt((1+np.sqrt(1+4*r3))*0.5)
f3b=-np.sqrt((1+np.sqrt(1+4*r3))*0.5)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.plot(r1, f1,color='royalblue',linewidth=3)
ax.plot(r2, f2a,color='royalblue',linestyle='--',linewidth=2)
ax.plot(r2, f2b,color='royalblue',linestyle='--',linewidth=2)
ax.plot(r3, f3a,color='royalblue',linewidth=2)
ax.plot(r3, f3b,color='royalblue',linewidth=2)
ax.plot(r4, f4,color='royalblue',linestyle='--',linewidth=4)

ax.grid()


ax.set_xlabel("$s$",fontsize=16)
ax.set_ylabel("$x^*$",fontsize=16)
ax.yaxis.labelpad=-5
#ax.set_xticks([-2,-1,0,1,2])

#ax.text(0.5,0.75,'stable',fontsize=16,rotation=30)
#ax.text(0.5,-0.6,'stable',fontsize=16,rotation=-30)
#ax.text(0.2,0.05,'unstable',fontsize=16)
#ax.text(-0.55,0.05,'stable',fontsize=16)

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
#ax.set_xlim([-1.1,1.1])

ax.set_title("Bifurcation diagram for $\dot{x}=sx+x^3-x^5$")

fig.savefig("1d-bif-pfbd3.pdf")
plt.show()

