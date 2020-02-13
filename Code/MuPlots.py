import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")


x = np.arange(0.05, 0.95, 0.05)
L1s = np.array([0.715, 0.609, 0.52, 0.438, 0.361, 0.286, 0.213, 0.142, 0, -0.071, -0.142, -0.213, -0.286, -0.361, -0.438, -0.52, -0.69, -0.715])
L2s = np.array([1.228, 1.26, 1.27, 1.271, 1.266, 1.257, 1.245, 1.231, 1.198, 1.181, 1.162, 1.143, 1.123, 1.103, 1.083, 1.062, 1.042, 1.021])
L3s = np.array([-1.021, -1.042, -1.062, -1.083, -1.103, -1.123, -1.143, -1.162, -1.198, -1.215, -1.231, -1.245, -1.257, -1.266, -1.271, -1.27, -1.26, -1.228])
L45s = np.array([0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0, -0.05, -0.1, -0.15, -0.2, -0.25, -0.3, -0.35, -0.4])


plt.plot(x, L1s, '.', label='L1')
plt.plot(x, L2s, '.', label='L2')
plt.plot(x, L3s, '.', label='L3')
plt.plot(x, L45s, '.', label='L4 and L5')
plt.xlabel(r'$\mu$')
plt.ylabel(r'$\mu(x)$')
plt.title(r'Plot of the $x$ positions of $L_1$ - $L_5$ as a function of $\mu$')
plt.grid()
plt.legend()
plt.savefig('MuPlot.png')
plt.savefig('MuPlot.svg')
plt.show()