# Program to plot Fermat's spiral and floret positions

import numpy as np
import matplotlib.pyplot as plt
import P2Cdef as p2c

#%% Floret positions
# Specify number of florets to plot
nmax = 20

# Create figure
fig=plt.figure(figsize=(7,7))

def florets(nmax,ndiff):
    # Parameter to alter positions of florets (=0 for positions that line on a
    # Fermat spiral)
    n = np.arange(1,nmax+1)
    rf = np.sqrt(n)
    # Define the Golden Mean
    phi = (1 + np.sqrt(5))/2
    thetaf = (2*np.pi/phi**2+ndiff)*n
    
    # Convert to Cartesians
    xf,yf=p2c.polar2cart(rf,thetaf)
    
    return(xf,yf)

# Plot floret positions
xf,yf=florets(20,0)
plt.plot(xf,yf,'ro')
plt.title('Fermat spiral')

#%% Fermat spiral

# Define the Golden Mean
phi = (1 + np.sqrt(5))/2
# (Actually this is defined in the first part so doesn't need to be
# redefined here, but you will need to include it in your function.)

# Define theta and r
theta = np.linspace(0,50,500)
r = np.sqrt(phi**2*theta/(2*np.pi))

# Convert theta and r to Cartesian coordinates
x,y=p2c.polar2cart(r,theta)

# Plot Fermat spiral
plt.plot(x,y)

#%% Floret plot

fig=plt.figure(figsize=(12,8))
plt.subplots_adjust(wspace=0.4,hspace=0.4,top=0.85)
#f1=fig.add_subplot(231)
i=1
while i<7:
    xf,yf=florets(20,np.round(-0.35+0.1*i,4))
    fig.add_subplot(2,3,i)
    plt.title("ndiff = "+str(np.round(-0.35+0.1*i,4)))
    plt.plot(xf,yf,'ro')
    i=i+1
plt.savefig("Computing SET 14 - FloretPlots.jpg")