import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r = np.arange(-1, 1, 0.001)
s = -np.power(abs(r)*1.5*np.sqrt(3),0.6666)
s2=1.0+r*0.0

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(r,s,linewidth=2)
ax.fill_between(r,s,s2,color='aliceblue',alpha=0.7)

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$r$",fontsize=16)
ax.set_ylabel("$s$",fontsize=16)
ax.yaxis.labelpad=-2
ax.xaxis.labelpad=-2
#ax.set_xticks([-0.3849,0,0.3849])
#ax.set_xticklabels(["$-r_c$","0","$r_c$"],fontsize=16)

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
ax.set_ylim([-2,1.2])

h1=0.2
ax.text(-0.9,0.5,'Phase A: 1 fixed point',fontsize=16,color='blue')
ax.plot(-0.5,h1,'bo',fillstyle='none',markersize=12)
ax.arrow(-0.5, h1, 0.2, 0, head_width=0.07, head_length=0.05, fc='k', ec='k')
ax.arrow(-0.5, h1, -0.2, 0, head_width=0.07, head_length=0.05, fc='k', ec='k')
ax.plot([-0.9,-0.1],[h1,h1],color='black')

ax.text(-0.55,-1.55,'Phase B: 3 fixed points',fontsize=16,color='blue')
h2=-1.85
ax.plot(-0.75,h2,'bo',fillstyle='none',markersize=12)
ax.plot(-0.5,h2,'bo',markersize=12)
ax.plot(-0.25,h2,'bo',fillstyle='none',markersize=12)
ax.arrow(-0.75, h2, 0.1, 0, head_width=0.07, head_length=0.05, fc='k', ec='k')
ax.arrow(-0.75, h2, -0.1, 0, head_width=0.07, head_length=0.05, fc='k', ec='k')
ax.arrow(-0.25, h2, 0.1, 0, head_width=0.07, head_length=0.05, fc='k', ec='k')
ax.arrow(-0.25, h2, -0.1, 0, head_width=0.07, head_length=0.05, fc='k', ec='k')
ax.plot([-0.94,-0.06],[h2,h2],color='black')

#ax.plot(-1,-0.666,'bo',markersize=15)
#ax.plot(1,0.666,'bo',fillstyle='none',markersize=15)

ax.set_title("Bifurcation diagram",fontsize=16)

fig.savefig("1d-bif-snp6.pdf")
plt.show()

