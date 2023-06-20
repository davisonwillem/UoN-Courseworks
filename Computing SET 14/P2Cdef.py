import numpy as np
import matplotlib.pyplot as plt

def polar2cart(r,theta):
    """
    This function takes 2 values for polar coordinates, r & theta, and converts them to cartesian coordinates, x & y.
    
    It can also take multiple values at once using: np.array([val1,val2,...])
    
    To use this function type: polar2cart(~r VALUE~,~theta VALUE~)
    """
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return(x,y)
    
x,y=polar2cart(np.array([5,2,22]),np.array([0.25*np.pi,3,77]))
