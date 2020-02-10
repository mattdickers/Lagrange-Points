import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")

eqtn = r"$f(x)=-\frac{\left(1-\mu\right)\left(x+\mu\right)}{\left|\left(x+\mu\right)\right|^{3}}-\frac{\mu\left(x+\mu-1\right)}{\left|\left(x+\mu-1\right)^{3}\right|}$"

plt.grid()

mu = 0.25

plt.axhline(linewidth=1, color='k')
plt.axvline(linewidth=1, color='k')

def function(x, mu):
    y = (((1 - mu)*(x + mu))/(abs(x + mu))**3) + ((mu*(x + mu - 1))/(abs(x + mu - 1)**3))
    return y

P1 = np.arange(-2.5, -0.3, 0.01)
plt.plot(P1, -function(P1, mu), 'k', label=eqtn)

P2 = np.arange(-0.2, 0.7, 0.01)
plt.plot(P2, -function(P2, mu), 'k')

P3 = np.arange(0.8, 2.5, 0.01)
plt.plot(P3, -function(P3, mu), 'k')

x = np.arange(-2.5, 2.5, 0.01)
y = np.arange(-2.5, 2.5, 0.01)

plt.plot(P1, -P1, 'r', label=r"$f(x) = x$")
plt.plot(np.concatenate((np.arange(-0.3, -0.2, 0.01), P2)), -np.concatenate((np.arange(-0.3, -0.2, 0.01), P2)), 'r')
plt.plot(np.concatenate((np.arange(0.7, 0.8, 0.01), P3)), -np.concatenate((np.arange(0.7, 0.8, 0.01), P3)), 'r')

plt.ylim(30, -30)

crosses1 = np.argwhere(np.diff(np.sign(P1 - function(P1, mu)))).flatten()
plt.plot(P1[crosses1], -P1[crosses1], 'ro')

crosses2 = np.argwhere(np.diff(np.sign(P2 - function(P2, mu)))).flatten()
plt.plot(P2[crosses2], -P2[crosses2], 'ro')

crosses3 = np.argwhere(np.diff(np.sign(P3 - function(P3, mu)))).flatten()
plt.plot(P3[crosses3], -P3[crosses3], 'ro')
print("Crosses at: ("+str(P1[crosses1])+","+str(P1[crosses1])+"), ("+str(P2[crosses2])+","+str(P2[crosses2])+"), ("+str(P3[crosses3])+","+str(P3[crosses3])+")")

plt.title(r"Plot for $\mu=%.2f$" % (mu,))
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.legend(loc="upper left")
plt.savefig("Plot.svg")
plt.savefig("Plot.png")
print("Plot saved")
plt.show()