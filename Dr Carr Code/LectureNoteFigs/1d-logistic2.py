
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,t):
    return x*(1-x)

fig, ax = plt.subplots()

t=np.arange(0.0,5.2,0.01)


#others
x0s=[ 0.1,0.25,0.5,0.75,1.5,2.0] 
for x0 in x0s:
    xs=odeint(f,x0,t)
    ax.plot(t,xs,color='royalblue')

# stable fixed points -- note plot after others so it can be seen
x0s=[ 1] 
for x0 in x0s:
    xs=odeint(f,x0,t)
    ax.plot(t,xs,color='black',linewidth=2)




    
ax.grid()

plt.axvline(0,color='black')
plt.axhline(0,color='black',linewidth=1)

ax.set_xlabel("$t$",fontsize=12)
ax.set_ylabel("$N$",fontsize=12)
ax.set_yticks([0,0.5,1,1.5,2.0])
ax.set_yticklabels(["0","$k/2$","$k$","$3k/2$","$2k$"])
ax.tick_params(labelbottom='off')
ax.set_xlim([-0.1,5.2])

ax.set_title("Time evolution for logistic equation $\dot{N}=rN(1-N/k)$")

fig.savefig("1d-logistic2.pdf")
plt.show()

