
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,t):
    return np.sin(x)

fig, ax = plt.subplots()

t=np.arange(0.0,4.0,0.01)

# stable fixed points
x0s=[ -12*np.pi/4,-4*np.pi/4,4*np.pi/4,12*np.pi/4] 
for x0 in x0s:
    xs=odeint(f,x0,t)
    ax.plot(t,xs,color='black',linewidth=2)

# unstable fixed points
x0s=[ -8*np.pi/4,-0*np.pi/4,8*np.pi/4] 
for x0 in x0s:
    xs=odeint(f,x0,t)
    ax.plot(t,xs,color='black',linewidth=2,linestyle='--')

#others
x0s=[ -11*np.pi/4,-10*np.pi/4,-9*np.pi/4,-7*np.pi/4,-6*np.pi/4,-5*np.pi/4, -3*np.pi/4,-2*np.pi/4,-1*np.pi/4,1*np.pi/4,2*np.pi/4,3*np.pi/4,5*np.pi/4,6*np.pi/4,7*np.pi/4,9*np.pi/4,10*np.pi/4,11*np.pi/4] 
for x0 in x0s:
    xs=odeint(f,x0,t)
    ax.plot(t,xs,color='royalblue')




    
ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black',linewidth=1)

ax.set_xlabel("$t$",fontsize=12)
ax.set_ylabel("$x$",fontsize=12)
ax.set_yticks([-3*np.pi,-2*np.pi,-np.pi,0,np.pi,2*np.pi,3*np.pi])
ax.set_yticklabels(["$-3\pi$","$-2\pi$","$-\pi$","$0$","$\pi$","$2\pi$","$3\pi$"])

ax.set_title("Time flow for $\dot{x}=\sin(x)$ for different values of $x(0)$")

fig.savefig("1d-sin2.pdf")
plt.show()

