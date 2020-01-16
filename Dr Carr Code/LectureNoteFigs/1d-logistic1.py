
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x = np.arange(0, 1.5, 0.01)
f = x*(1-x)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, f)

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$N$",fontsize=12)
ax.set_ylabel("$\dot{N}$",fontsize=12)
ax.set_xticks([0,0.5,1,1.5,2])
ax.set_xticklabels(["0","","$k$","",""])
ax.set_yticks([-0.3,-0.2,-0.1,0,0.1,0.2,0.3])
ax.set_yticklabels(["","","",0,"","",""])
ax.set_ylim([-0.32,0.32])

ax.plot(1,0,'bo',markersize=15)
ax.plot(0,0,'bo',fillstyle='none',markersize=15)


ax.arrow(0, 0, 0.5, 0.0, head_width=0.03, head_length=0.08, fc='k', ec='k')
ax.arrow(1.5, 0, -0.1, 0.0, head_width=0.03, head_length=0.08, fc='k', ec='k')

ax.set_title("Flow diagram for the logistic equation $\dot{x}=rN(1-N/k)$")

fig.savefig("1d-logistic1.pdf")
plt.show()

