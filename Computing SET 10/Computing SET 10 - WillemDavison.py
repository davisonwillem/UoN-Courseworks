import numpy as np
import matplotlib.pyplot as plt
x=float(input("Please enter a number x such that 0 < x < 1:"))
while x<=0 or x>=1:
    x=float(input("Try again:"))
print("x =",x,"& ln(1+x)=",np.log(1+x))
#%%
val=0
vals=np.zeros([12,])
for i in np.arange(1,13):
    val=val+((-1)**(i+1))*(x**i)*(1/i)
    vals[i-1]=val
xs=np.arange(1,13)
plt.figure("Figure")
plt.plot(xs,vals)
plt.plot(xs,val*np.ones([12,]),"--")
plt.xlabel("$n$")
plt.ylabel("Value of expansion up to term $n$")
plt.title("Plot of expansion of $ln(1+x)$")
if x==0.5:
    plt.savefig("Computing SET 10 - Expansion.jpg")
#%%
print("The value of the expansion including all terms with magnitude larger than 10^-8 is shown converging below:")
val1=0
i=1
while np.abs(((-1)**(i+1))*(x**i)*(1/i)) > 10**-8:
    val1=val1+((-1)**(i+1))*(x**i)*(1/i)
    print("n=",i,", the expansion up to this value of n is {:.9}".format(val1))
    i=i+1
#If I was to use a for loop instead of a while loop, the number of iterations in the expansion would have to be
#worked out first e.i. the value of n where the expansion term is less than 10^-8. This is why it is easier to use
#a while loop.