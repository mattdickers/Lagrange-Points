import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-np.pi, np.pi, 0.01)
s = 1.0-np.sin(t)


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()

ax.plot(t,s,color='royalblue')


ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black')

ax.set_xlabel(r"$\theta$",fontsize=12)
ax.set_ylabel(r"$\dot{\theta}$",fontsize=12)
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
ax.set_xticklabels(["$-\pi$","$-\pi/2$","0","$\pi/2$","$\pi$"])
ax.set_yticks([-1.0,-0.5,-0,0.5,1,1.5,2.0,2.5])

#ax.plot(-np.pi,0,'bo',markersize=15)
#ax.plot(0,0,'bo',fillstyle='none',markersize=15)
#ax.plot(np.pi,0,'bo',markersize=15)
#ax.plot(2*np.pi,0,'bo',fillstyle='none',markersize=15)

plt.text(np.pi/2,0,u'\u25D0',size=18,ha='center',va='center')

ax.arrow(-2.5, 0, 1, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(-0.5, 0, 1, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')
ax.arrow(np.pi/2, 0, 1, 0.0, head_width=0.1, head_length=0.2, fc='k', ec='k')

ax.set_title(r"$\dot{\theta}=\omega-a\sin\theta, a=\omega$",fontsize=16)

fig.savefig("1d-circle2b-unwrapped.pdf")
plt.show()

