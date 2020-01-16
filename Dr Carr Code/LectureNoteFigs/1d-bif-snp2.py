import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
x = np.arange(-1.5, 1.5, 0.01)
f1 = 1-x+x**3

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, f1)


ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel("$x$",fontsize=16)
ax.set_ylabel("$f(x)$",fontsize=16)
ax.yaxis.labelpad=-2
#ax.set_xticks([-2,-1,0,1,2])

#ax.set_yticks([-1.0,-0.5,0,0.5,1.0])
#ax.set_xlim([-1.1,1.1])

#ax.plot(-1,-0.666,'bo',markersize=15)
#ax.plot(1,0.666,'bo',fillstyle='none',markersize=15)

ax.text(0.63,1.2,'increase $r$',fontsize=16)
ax.text(0.63,0.13,'decrease $r$',fontsize=16)

ax.arrow(0.577, 1, 0, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.arrow(0.577, 0.5, 0, -0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

ax.set_title("$f(x)=r+sx+x^3, s<0$",fontsize=16)

fig.savefig("1d-bif-snp2.pdf")
plt.show()

