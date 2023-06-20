#%%

#Question 1a

import numpy as np
import matplotlib.pyplot as plt

z=np.arange(100,901,20)
v=37*(np.exp((250-z)/60)-2*np.exp((250-z)/120))

figa=plt.figure(figsize=(10,7))
plt.plot(z,v)
plt.xlabel("Atom-Molecule Separation / pm")
plt.ylabel("Morse Potential / meV")
plt.title("Plot of Morse Potential against Separation")
plt.savefig("Potential.jpg")

#%%

#Question 1ci

f=37/60*(np.exp((250-z)/60)-np.exp((250-z)/120))

figc=plt.figure(figsize=(10,7))
plt.plot(z,f)
plt.xlabel("Atom-Molecule Separation / pm")
plt.ylabel("Tip-Sample Force / meVm$^{-1}$")
plt.title("Plot of Force against Separation")
plt.savefig("Force.jpg")

#%%

#Question 1cii

plt.plot(z,-np.gradient(v,z))

plt.legend(("Hand Derived","Numpy Gradient Function"))

#%%

#Question 1d

df=-617.506*(np.exp((250-z)/60)-2*np.exp((250-z)/120))
figd=plt.figure(figsize=(10,7))
plt.plot(z,df)
plt.xlabel("Atom-Molecule Separation / pm")
plt.ylabel("Frequency Shift / s$^{-1}$")
plt.title("Plot of Frequency Shift against Separation")
plt.savefig("Frequency.jpg")