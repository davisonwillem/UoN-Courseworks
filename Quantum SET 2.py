import numpy as np
import matplotlib.pyplot as plt

#%%#

#1a)

L=6e-9
x=np.arange(0,L+1e-10,1e-10)
u1=np.sqrt(2/L)*np.sin(np.pi*x/L)
u2=np.sqrt(2/L)*np.sin(2*np.pi*x/L)

plt.plot(x,np.zeros((61,1)))
plt.plot(x,np.zeros((61,1))+4e8)
plt.plot((0,0),(7.5e8,0))
plt.plot(x,np.absolute(u1)**2)
plt.plot(x,np.absolute(u2)**2+4e8)
plt.xlabel("x")
plt.xticks([0,L],['0','L'])
plt.yticks([0,4e8],['|$U_{1}$(x)|$^2$','|$U_{2}$(x)|$^2$'])

#%%#

#1c)

from scipy.integrate import trapz

L=6e-9
x=np.arange(0,L+1e-10,1e-10)
u1=np.sqrt(2/L)*np.sin(np.pi*x/L)
u2=np.sqrt(2/L)*np.sin(2*np.pi*x/L)
psi=(u1+u2)/np.sqrt(2)

plt.plot(x,psi)
plt.xlabel("x")
plt.ylabel("$\Psi(x,t = 0)$")
plt.xticks([0,L],['0','L'])

c1=trapz(u1*psi,x)
c2=trapz(u2*psi,x)
print("C1:",c1,"    C2:",c2)