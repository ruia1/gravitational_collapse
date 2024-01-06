'''
ver : Python 3.7.3 64-bit
last change : 24/1/7 3:35 AM
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a = 1.0

m = 1.0
p = 0.0
n = 3.0 * m / 4 / a ** 3
rho = n
U = 0
r = a
t_stop = 1.14

def osModel(t,state):
    r,rho,n,U = state
    dstate = np.zeros_like(state)
    dr,drho,dn,dU = dstate
    S = n * r ** 2

    dr = U
    dS = -U / r * S
    dn = dS / (r ** 2) -2 * n * dr / r
    drho = rho * dn / n
    dU = -m/(r ** 2)

    dstate = np.array([dr,drho,dn,dU])
    return dstate

dt = 0.01
t = np.arange(0, t_stop, dt)

state = np.array([r,rho,n,U])

y = np.empty((len(t), 4))
y[0] = np.array([r,rho,n,U])
flg = True
for i in range(1, len(t)):
    y[i] = y[i-1] + osModel(t[i-1],y[i-1]) * dt
    if flg and y[i,0]<=0:
        print(t[i],y[0])

fig = plt.figure(figsize=(5,4))

ax = fig.add_subplot(111)
ax.plot(t,y[:,0],label="r")

plt.legend()

plt.show()