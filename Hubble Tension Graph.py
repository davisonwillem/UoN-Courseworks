import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure()

Planck=67.4
Gaia=73.3
BAO1=67
BAO2=67.6
Lensing1=75
Lensing2=82.4
GW1=70

x=[1,1,2,2.1,3,3.1,4,4.1]
y=[67.4,73.3,67,67.6,75,82.4,70]

y_errormin=[0.5,1.04,3.2,1.1,6,8.3,8]
y_errormax=[0.5,1.04,3.2,1.1,7,8.4,12]
y_error=[y_errormin,y_errormax]
    
plt.errorbar(x[0],y[0],yerr=[[0.5],[0.5]],xerr=0,fmt='o',ecolor='r',color='r',capsize=4)
plt.errorbar(x[1],y[1],yerr=[[1.04],[1.04]],xerr=0,fmt='o',ecolor='b',color='b',capsize=4)
plt.errorbar(x[2],y[2],yerr=[[3.2],[3.2]],xerr=0,fmt='o',ecolor='g',color='g',capsize=4)
plt.errorbar(x[3],y[3],yerr=[[1.1],[1.1]],xerr=0,fmt='o',ecolor='g',color='g',capsize=4)
plt.errorbar(x[4],y[4],yerr=[[6],[7]],xerr=0,fmt='o',ecolor='purple',color='purple',capsize=4)
plt.errorbar(x[5],y[5],yerr=[[8.3],[8.4]],xerr=0,fmt='o',ecolor='purple',color='purple',capsize=4)
plt.errorbar(x[6],y[6],yerr=[[8],[12]],xerr=0,fmt='o',ecolor='orange',color='orange',capsize=4)

plt.ylabel('$H_0$   (kms$^{-1}$ Mpc$^{-1}$)')
r=mpatches.Patch(color='r',label='Planck')
b=mpatches.Patch(color='b',label='Gaia')
g=mpatches.Patch(color='g',label='BAO')
p=mpatches.Patch(color='purple',label='Lensing')
o=mpatches.Patch(color='orange',label='GW')
plt.legend(handles=[r,b,g,p,o])
plt.xticks(color="w")
ax=plt.gca()
ax.get_xaxis().set_visible(False)

plt.savefig("C:/Users/davis/Pictures/TensionGraph.png",dpi=1200)