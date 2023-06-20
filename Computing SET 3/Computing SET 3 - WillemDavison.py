#--------a
#Willem Davison, SET 3 Coursework
#--------b
import numpy as np
import matplotlib.pyplot as plt
#--------j
plt.figure("Final Figure",dpi=300)
#--------c
n1 = np.arange (4,19,1)
#--------di
n2 = np.linspace (4,18,15)
#linspace gives floats by default where as arange gives intergers
#--------dii
n3 = np.linspace (4,18,15,dtype=int)
#this array is made of integers
#--------e
qn = np.array([6.558,8.206,9.880,11.50,13.14,14.82,16.40,18.04,
                19.68,21.32,22.96,24.60,26.24,27.88,29.52])
#--------f
plt.plot(n3,qn,'.',color='m')
#--------g
plt.title("Graph showing charge against number of electrons on an oil drop")
plt.xlabel("$n$")
plt.ylabel("$qn /10^-19$")
#--------h
l1 = np.array([0,20])
l2 = np.array([0.0285,32.7885])
plt.plot(l1,l2)
#--------i
plt.legend(("Data", "Line of best fit"))
#--------j
plt.savefig("Computing SET 3 - Final Figure.jpg")