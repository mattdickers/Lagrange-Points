import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r = np.arange(-1, 1, 0.001)
s = -np.power(abs(r)*1.5*np.sqrt(3),0.6666)


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(r,s)

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

ax.set_title("Bifurcation diagram",fontsize=16)

fig.savefig("1d-bif-snp5.pdf")
plt.show()

