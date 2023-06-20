import numpy as np
import matplotlib.pyplot as plt

#%%#

#5a)

r=np.arange(0.3,4,0.01)
a=0

fig1=plt.figure()
while a<3:
    veff=r**2+a*r**-2
    plt.plot(r,veff)
    a=a+1
plt.xlabel('r')
plt.ylabel('Veff')
plt.legend(('psi1','psi2','psi3'))
plt.title('Plot of Veff taking natural units')

#%%#

#5b)

r=np.arange(0,4,0.01)
cp1=1-np.exp(-r**2)
cp2=1-(r**2+1)*np.exp(-r**2)
cp3=1-(5*r**4+6*r**2+8)*np.exp(-r**2)/8

fig2=plt.figure()
plt.plot(r,cp1)
plt.plot(r,cp2)
plt.plot(r,cp3)
plt.xlabel('r')
plt.ylabel('P')
plt.legend(('psi1','psi2','psi3'))
plt.title('Plot of cumulative probability taking natural units')

#%%#

#5c)

r=np.arange(0,4,0.01)
p1=np.exp(-r**2)
p2=np.exp(-r**2)*r**2
p3=np.exp(-r**2)*r**4

fig3=plt.figure()
plt.plot(r,p1)
plt.plot(r,p2)
plt.plot(r,p3)
plt.xlabel('r')
plt.ylabel('P')
plt.legend(('psi1','psi2','psi3'))
plt.title('Plot of radial probability taking natural units')

#%%#

#7)

from scipy.optimize import fsolve

cp150=fsolve(lambda x : 1-np.exp(-x**2) - 0.5,0.1)
cp250=fsolve(lambda x : 1-(x**2+1)*np.exp(-x**2) - 0.5,0.1)
cp350=fsolve(lambda x : 1-(5*x**4+6*x**2+8)*np.exp(-x**2)/8 - 0.5,0.1)

print('Radius for 50% probability for psi1:',cp150)
print('Radius for 50% probability for psi2:',cp250)
print('Radius for 50% probability for psi3:',cp350)