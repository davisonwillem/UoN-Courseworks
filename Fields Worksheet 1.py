import numpy as np
import matplotlib.pyplot as plt

#%%#

#3)

ax=plt.axes(projection='3d')
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
x,y=np.meshgrid(X,Y)
h=1
F=h*np.exp(-x**2-y**2)
ax.plot_surface(x,y,F)
plt.show()

#%%#

#4a)

ax=plt.axes()
w=np.arange(-50,50.1,0.05)
x,y=np.meshgrid(w,w)
V=1/(np.sqrt(x**2+y**2))
ax.contour(x,y,V)
plt.show()

#%%#

#4b)

ax=plt.axes()
w=np.arange(-50,50.1,0.05)
x,y=np.meshgrid(w,w)
V=1/(np.sqrt(x**2+y**2))
c = np.arange(0.01, 0.1, 0.01)
ax.contour(x,y,V,levels=c)
ax.set_aspect('equal')
plt.show()

#%%#

#5a)

th=np.arange(0,361,20)*np.pi/180
r0=np.arange(0.2,1.2,0.2)
theta,r=np.meshgrid(th,r0)
X=r*np.cos(theta)
Y=r*np.sin(theta)
x,y=np.meshgrid(X,Y)
a=1
u=-y*a/(x**2+y**2)
v=x*a/(x**2+y**2)
plt.quiver(x,y,u,v)

#%%#

#5b)

th=np.arange(0,361,20)*np.pi/180
r0=np.arange(0.2,1.2,0.2)
theta,r=np.meshgrid(th,r0)
X=r*np.cos(theta)
Y=r*np.sin(theta)
x,y=np.meshgrid(X,Y)
a=100
u=-y*a/(x**2+y**2)+1
v=x*a/(x**2+y**2)+1
plt.quiver(x,y,u,v)