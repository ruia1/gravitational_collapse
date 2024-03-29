'''
ver : Python 3.7.3 64-bit
last change : 24/2/8
'''

import numpy as np
import matplotlib.pyplot as plt
#from scipy.integrate import solve_ivp

a = 1.0
da = 0.01
len_a = int(a/da-1)

m = np.arange(da,a,da)
p = 0.0
n = np.array([4.0  / 3 * np.pi / len_a for i in range(len_a)])
rho = np.copy(n)
U = np.array([0.0 for i in range(len_a)])
r = np.array([(i + 1) * da for i in range(len_a)])

t_stop = 10.0

def dash(x:np.ndarray, dx, before_x = None, after_x = None):
    dash_x = np.zeros_like(x)
    if before_x == None:
        dash_x[0] = (x[1] - x[0])/dx
    else:
        dash_x[0] = (x[1] - before_x)/(2*dx)
    
    for i in range(1,len(x)-1):
        dash_x[i] = (x[i+1] - x[i-1])/(2*dx)
    
    if after_x == None:
        dash_x[-1] = (x[-1] - x[-2])/dx
    else:
        dash_x[-1] = (after_x - x[-2])/(2*dx)

    return dash_x

def osModel(t,state,m,dash_r,dash_U):
    r,rho,n,U = state
    dstate = np.zeros_like(state)
    dr,drho,dn,dU = dstate
    S = n * r ** 2
    remove_nan = lambda x:np.where(np.isnan(x)|np.isinf(x),0,x)

    dr = remove_nan(U)
    dS = remove_nan(-dash_U / dash_r * S)
    dn = remove_nan(dS / (r ** 2) -2 * n * dr / r)
    drho = remove_nan(rho * dn / n)
    dU = remove_nan(-m/(r ** 2))

    dstate = np.array([dr,drho,dn,dU])
    return dstate

dt = 0.0001
t = np.arange(0, t_stop, dt)

state = np.array([r,rho,n,U])

y = np.empty((len(t),4,len_a)) #y[time,state,a]
y[0] = np.array([r,rho,n,U])
flg = True
for i in range(1, len(t)):
    dash_r = dash(y[i-1,0],da)
    dash_U = dash(y[i-1,3],da)
    for j in range(len_a):
        y[i,:,j] = y[i-1,:,j] + osModel(t[i-1],y[i-1,:,j],m[j],dash_r[j],dash_U[j]) * dt
    if y[i,0,-1]<=0.001:
        print(t[i],y[i:0])
        #print(y[:,0,-1])
        #print(y[:,0,len_a//2])
        stop_t = i
        t_stop = t[i]
        break
y[:,0] = np.where(y[:,0]<0, None, y[:,0])
fig = plt.figure(figsize=(5,4))

ax = fig.add_subplot(111)
ax.plot(t[:stop_t],y[:stop_t,0,-1],label="r a=1.0")
ax.plot(t[:stop_t],y[:stop_t,0,len_a//2],label="r a=0.5")
ax.plot(t[:stop_t],y[:stop_t,0,0],label="r a=0.0")


plt.legend()
plt.show()