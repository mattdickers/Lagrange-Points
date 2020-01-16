import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x1 = np.arange(-1.2, 1.2, 0.001)
r1 = x1+x1**3


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(r1, x1,linestyle='--',color='royalblue')

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$r$",fontsize=16)
ax.set_ylabel("$x^*$",fontsize=16)
ax.yaxis.labelpad=-2
ax.xaxis.labelpad=-2
#ax.set_xticks([-0.3849,0,0.3849])
#ax.set_xticklabels(["$-r_c$","0","$r_c$"],fontsize=16)

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
#ax.set_xlim([-1.1,1.1])

ax.set_title("Bifurcation/fixed point diagram, $s>0$",fontsize=16)

fig.savefig("1d-bif-snp3.pdf")
plt.show()

