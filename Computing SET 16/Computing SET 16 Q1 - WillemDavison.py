# Program to do a polynomial fit 

import numpy as np
import matplotlib.pyplot as plt

# Define a 2D array to fit
f="data.txt"
dat=np.loadtxt(f)
# Pick order of polynomial
n = 2

# Define x, y data and plot data points
x = dat[:,0]
y = dat[:,1]
# Plot the data as red points, and add labels to the plot.
plt.figure()
plt.plot(x,y,'r*')
plt.xlabel('x')
plt.ylabel('y')

# Calculate and plot the fit
# Calculate polynomial fit
p = np.polyfit(x,y,n)
# Title, with value of n.
plt.title('Polynomial fit of order ' + str(n) +" using data from file data.txt called f in code")
# Plot the line of best fit
# We could just use the values in x to determine values y for the best-fit
# curve, but the results aren't very smooth if there aren't many points.
# Ensure that the plot is always calculated using 100 points, whatever the
# range of x in the data file.
xfit = np.linspace(min(x),max(x),100)
yfit = np.polyval(p,xfit)
plt.plot(xfit,yfit)