'''
ver : Python 3.7.3 64-bit
last change : 24/1/4 5:30 AM
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a = 1.0

m = 1.0
p = 0.0
n = 3.0 * m / 4 / a^3
rho = n
U = 0
r = a
t_stop = 100.0

def osModel(t,r,rho,n,U):
    dr,drho,dn,dU = np.zeros_like([r,rho,n,U])
    S = n * r^2

    dr = U
    dS = -U / r * S
    dn = dS / r^2 -2 * n * dr / r
    drho = rho * dn / n
    dU = -m/r^2

    return [dr,drho,dn,dU]

dt = 0.01
t = np.arange(0, t_stop, dt)
