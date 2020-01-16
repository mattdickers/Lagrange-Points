
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
r1 = np.arange(0.0, 1.0, 0.001)
r2 = np.arange(1.0, 3.0, 0.001)
f1a=0.0*r1
#f1b=r1
f2a=0.0*r2
f2b=r2-1

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.plot(r1, f1a,color='royalblue',linewidth=3)
#ax.plot(r1, f1b,color='royalblue',linestyle='--',linewidth=2)
ax.plot(r2, f2a,color='royalblue',linestyle='--',linewidth=4)
ax.plot(r2, f2b,color='royalblue',linewidth=2)

ax.grid()


ax.set_xlabel("$N_0$",fontsize=16)
ax.set_ylabel("$n$",fontsize=16)
ax.yaxis.labelpad=-5
ax.xaxis.labelpad=-7
ax.set_xticks([0,1])
ax.set_xticklabels(["$0$","$k/G$"],fontsize=16)

ax.text(1.8,0.85,'laser',fontsize=16,rotation=45)
ax.text(0.3,0.05,'lamp',fontsize=16)

ax.set_yticks([0])

#ax.set_xlim([-1.1,1.1])

ax.set_title("The lasing threshold")

fig.savefig("1d-bif-laser.pdf")
plt.show()

