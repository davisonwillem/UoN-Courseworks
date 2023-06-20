import numpy as np
results=np.array([[54,56,72,34],[1,0,0,3],[0,1,0,0]])
names=np.array([["Amy","Bob","Carol","Dave"]])
progress=np.logical_and(results[0]>=40,results[2]==0)
print("The non-progressing students are as follows:")
for i in [0,1,2,3]:
    if progress[i]==False:
        print (names[0,i],":  Average:",results[0,i],", Soft Fails:",results[1,i],", Hard Fails:",results[2,i])
row=int(input("Enter a row (1, 2, 3 or 4):"))
print (names[0,row-1],":  Average:",results[0,row-1],", Soft Fails:",results[1,row-1],", Hard Fails:",results[2,row-1])
#%%
print("For ax^2 + bx + c,")
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
c=int(input("Enter a value for c:"))
disc=b**2-4*a*c
if disc>0:
    print("The two real roots are:",(-b+disc**0.5)/2*a,(-b-disc**0.5)/2*a)
elif disc==0:
    print("The single real root is:",-b/2*a)
else:
    print("The roots of this polynomial are complex.")
print("For ax^2 + bx + c,")
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
c=int(input("Enter a value for c:"))
print("The root(s) of this quadratic are: ",np.roots([a,b,c]))