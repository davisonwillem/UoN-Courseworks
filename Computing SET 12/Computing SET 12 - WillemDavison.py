import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

xs=np.linspace(-2,2,100)
ys=np.linspace(-2,2,100)
xg,yg=np.meshgrid(xs,ys)

m1=0.8
m2=0.2
x1=0.5
x2=0.5
U=m1/np.sqrt((xg+x1)**2+yg**2)+m2/np.sqrt((xg-x2)**2+yg**2)+0.5*(m1+m2)*(xg**2+yg**2)
fig=plt.figure(figsize=(10,8))
ax=fig.gca()
contourplot1=ax.contour(xg,yg,U)

contourplot2=ax.contour(xg,yg,U,np.arange(1.5,2.11,0.2))
ax.clabel(contourplot2)

fig=plt.figure(figsize=(13,8))
ax=fig.gca(projection="3d")
surf=ax.plot_surface(xg,yg,U,cmap=cm.viridis)
fig.colorbar(surf,shrink=0.4,aspect=5,pad=0.1)

BinaryStars=plt.imread("BinaryStarsAlbireo.jpg")
fig=plt.figure(figsize=(10,8))
plt.imshow(BinaryStars)
plt.title("Binary Star system Albireo:")
plt.axis("off")