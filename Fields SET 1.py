import numpy as np
import matplotlib.pyplot as plt

#a)

x=np.arange(-2,3,0.1)
h=np.exp(-x**2)+0.5*np.exp(-(x-1.5)**2)
plt.plot(x,h)

#b)

w=np.arange(-2,3,0.1)
x,y=np.meshgrid(w,w)
h=np.exp(-x**2-y**2)+0.5*np.exp(-(x-1.5)**2-2*y**2)
plt.contour(x,y,h,np.arange(0.1,1.01,0.1))

#c)

#\textbf{\nabla}h=(-2xe^{-x^{2}-y^{2}}-(x-1.5)e^{-(x-1.5)^{2}-2y^{2}})\textbf{i}+(-2ye^{-x^{2}-y^{2}}-2ye^{-(x-1.5)^{2}-2y^{2}})\textbf{j}

#d)

ax=plt.axes()
w=np.arange(-2,3,0.1)
x,y=np.meshgrid(w,w)
h=np.exp(-x**2-y**2)+0.5*np.exp(-(x-1.5)**2-2*y**2)
plt.contour(x,y,h,np.arange(0.1,1.01,0.1))

w=np.arange(-2,3,0.3)
x,y=np.meshgrid(w,w)
u=-2*x*np.exp(-x**2-y**2)-(x-1.5)*np.exp(-(x-1.5)**2-2*y**2)
v=-2*y*np.exp(-x**2-y**2)-2*y*np.exp(-(x-1.5)**2-2*y**2)
plt.quiver(x,y,u,v)
ax.set_aspect('equal')

#e)

ax=plt.axes()
w=np.arange(-2,3,0.1)
x,y=np.meshgrid(w,w)
h=np.exp(-x**2-y**2)+0.5*np.exp(-(x-1.5)**2-2*y**2)
plt.contour(x,y,h,np.arange(0.1,1.01,0.1))

w=np.arange(-2,3,0.3)
x,y=np.meshgrid(w,w)
h=np.exp(-x**2-y**2)+0.5*np.exp(-(x-1.5)**2-2*y**2)
v,u=np.gradient(h)
plt.quiver(x,y,u,v)
ax.set_aspect('equal')

#f)

ax=plt.axes()
w=np.arange(-2,3,0.1)
X,Y=np.meshgrid(w,w)
h=np.exp(-X**2-Y**2)+0.5*np.exp(-(X-1.5)**2-2*Y**2)
plt.contour(X,Y,h,np.arange(0.1,1.01,0.1))

#print(plt.contour(X,Y,h,np.arange(0.1,1.01,0.1)).allsegs)[0]

c=plt.contour(X,Y,h,np.arange(0.1,1.01,0.1))
n=0
while n<10:
    x,y=c.allsegs[n][0][:,0],c.allsegs[n][0][:,1]
    u=-2*x*np.exp(-x**2-y**2)-(x-1.5)*np.exp(-(x-1.5)**2-2*y**2)
    v=-2*y*np.exp(-x**2-y**2)-2*y*np.exp(-(x-1.5)**2-2*y**2)
    plt.quiver(x,y,u,v)
    n=n+1
ax.set_aspect('equal')