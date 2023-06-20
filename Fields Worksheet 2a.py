import numpy as np
import matplotlib.pyplot as plt

#%%#

#14a)

w=np.arange (-2,2,0.1)
x,y=np.meshgrid(w,w)
F=np.exp(-x**2-y**2)
plt.contour(x,y,F)

#14b)

u=-2*x*np.exp(-x**2-y**2)
v=-2*y*np.exp(-x**2-y**2)
plt.quiver(x,y,u,v)

#14c)

fig1=plt.figure()
grad=np.gradient(F)
plt.quiver(x,y,grad[1],grad[0])
plt.show()

#14d)

fig2=plt.figure()
th=np.arange(0,361,20)*np.pi/180
r0=np.arange(0.2,1.2,0.2)
[theta,r]=np.meshgrid(th,r0)
x=r*np.cos(theta)
y=r*np.sin(theta)
Fm=np.sqrt(4*np.exp(-2*(x**2+y**2))*(x**2+y**2))
u=-Fm*2*x*np.exp(-x**2-y**2)
v=-Fm*2*y*np.exp(-x**2-y**2)
plt.quiver(x,y,u,v)
plt.show()

#%%#

#15)

w=np.arange (-2,2,0.1)
x,y=np.meshgrid(w,w)
F=-2*(x+y)*np.exp(-x**2-y**2)
plt.contour(x,y,F)