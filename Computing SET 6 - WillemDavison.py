#importing necesary modules
import numpy as np
import matplotlib.pyplot as plt
#generating random numbers from the given distribution
z = np.random.normal (0,2,5000)
print ("The mean calculated from the random numbers is:{:.3f}".format(np.mean(z)))
print ("The standard deviation calculated from the random numbers is:{:.3f}".format(np.std(z)))
x=np.arange(-9,9.1,0.5)
#plotting histogram
plt.hist(z, bins=x, rwidth=0.75)
x1=np.arange(-9,9.01,0.1)
dN=(5000/(np.std(z)*np.sqrt(2*np.pi)))*np.exp(-x1*x1/(2*np.std(z)*np.std(z)))*0.5
#plotting distribution curve
plt.plot(x1,dN,"r")
#labeling axis and giving a title
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.title("Graph showing expected distribution (red) and randomly generated distribution (blue).")
#%%#
y=z[0:500:1]
#starting new figure
plt.figure()
#plotting new histogram from first 500 random numbers
plt.hist(y, bins=x, rwidth=0.75)
#plotting new distribution curve
dNy=(500/(np.std(y)*np.sqrt(2*np.pi)))*np.exp(-x1*x1/(2*np.std(y)*np.std(y)))*0.5
plt.plot(x1,dNy,"r")