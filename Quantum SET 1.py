import numpy as np
import matplotlib.pyplot as plt

#%%#

#b)

fig1=plt.figure()
x=np.linspace(-4,4,1000)
si0=np.pi**(-0.25)*np.exp(-0.5*x**2)
plt.plot(x,si0)

V=0.5*x**2
plt.plot(x,V)

#%%#

#e)

fig2=plt.figure()
si0k=np.fft.fft(si0)/1000
si0k=np.fft.fftshift(si0k)
fvals=np.linspace(0,999,1000)-500
plt.xlim(-10,10)
plt.plot(fvals,np.absolute(si0k)**2)

#%%#

#f)

from scipy.integrate import simps as intg

fig3=plt.figure()
x=np.linspace(-4,4,1000)
si0=np.pi**(-0.25)*np.exp(-0.5*x**2)
plt.plot(x,si0)

V=0.5*x**2
plt.plot(x,V)

dx=0.008
E=0.4
psifin=1
i=1
while np.absolute(psifin) >=0.001:
    x=-4
    psi0=0
    psi1=10**-6
    psifin=1
    while x<4:
        psi2=2*psi1-2*dx**2*psi1*(E-(x**2)/2)-psi0
        psi0=psi1
        psi1=psi2
        x=x+dx
    psifin=psi2
    print("Iteration:",i)
    E=E+0.001
    i=i+1
E=E-0.001
print("E is: ~",E)

x=-4
psi0=0
psi1=10**-6
psifin=1
fullpsi=np.array([])
while x<4:
    psi2=2*psi1-2*dx**2*psi1*(E-(x**2)/2)-psi0
    psi0=psi1
    psi1=psi2
    x=x+dx
    fullpsi=np.append(fullpsi,np.absolute(psi2))
normaliser=intg(fullpsi)

x=-4
psi0=0
psi1=10**-6
psifin=1
while x<4:
    j=0
    while j<20:
        psi2=2*psi1-2*dx**2*psi1*(E-(x**2)/2)-psi0
        psi0=psi1
        psi1=psi2
        x=x+dx
        j=j+1
    plt.plot(x,normaliser*psi2,'.')