# Program to do a polynomial fit 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

def sliderCallback(val):
    global n
    n=val
    axesHandleFit.set_ydata(fitData(x,y,val)[1])
    plt.draw()
    
def radioCallback(val):
    axesHandleDat.set_data(getData(val))
    ax.relim()
    ax.autoscale_view()
    global x,y
    x,y=getData(val)
    axesHandleFit.set_data(fitData(x,y,n))
    plt.draw()

def getData(f):
    d=np.loadtxt(f)
    x = d[:,0]
    y = d[:,1]
    return x,y

def fitData(x,y,n):
    # Calculate and plot the fit
    # Calculate polynomial fit
    p = np.polyfit(x,y,n)
    # Plot the line of best fit
    # We could just use the values in x to determine values y for the best-fit
    # curve, but the results aren't very smooth if there aren't many points.
    # Ensure that the plot is always calculated using 100 points, whatever the
    # range of x in the data file.
    xfit = np.linspace(min(x),max(x),100)
    yfit = np.polyval(p,xfit)
    return xfit,yfit


# Plot the data as red points, and add labels to the plot.
plt.figure(figsize=(8,5))
ax=plt.axes([0.3,0.3,0.6,0.6])
plt.title('Polynomial fit (select order and data file)')
plt.xlabel('x')
plt.ylabel('y')

f="data.txt"
n=2
x,y=getData(f)
xfit,yfit=fitData(x,y,n)

axesHandleDat,=plt.plot(x,y,'r*')
axesHandleFit,=plt.plot(xfit,yfit)

sliderHandle=widgets.Slider(plt.axes([0.36,0.08,0.54,0.07]),"Value of n",1,10,valinit=2,valfmt="%i")
sliderHandle.on_changed(sliderCallback)

radioHandle=widgets.RadioButtons(plt.axes([0.03,0.55,0.2,0.35]),("data.txt","data1.txt","data2.txt"))
radioHandle.on_clicked(radioCallback)