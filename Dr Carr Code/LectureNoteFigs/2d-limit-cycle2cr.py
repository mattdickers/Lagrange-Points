
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x = np.arange(0, 1.5, 0.01)
f = 0.5*(2*x-1)**2-0.25*(2*x-1)**4-0.25

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, f)

ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.set_xlabel("$r$",fontsize=12)
ax.set_ylabel("$\dot{r}$",fontsize=12)
ax.set_ylim([-0.5,0.5])


#ax.plot(1,0,'bo',fillstyle='none',markersize=15)
ax.plot(0,0,'bo',markersize=15,color='k')
plt.text(1,0,u'\u25D0',size=20,ha='center',va='center',rotation=180)

ax.arrow(1, 0, -0.5, 0.0, head_width=0.03, head_length=0.08, fc='k', ec='k')
ax.arrow(1.5, 0, -0.1, 0.0, head_width=0.03, head_length=0.08, fc='k', ec='k')

ax.set_title(r"Half Stable",fontsize=16)

fig.savefig("2d-limit-cycle2cr.pdf")
plt.show()

