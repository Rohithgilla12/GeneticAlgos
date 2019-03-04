
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import random

def eggHolder(x,y):
    return (-(y+47)*np.sin(np.sqrt(np.abs((x/2)+(y+47))))- (x*np.sin(np.sqrt(np.abs(x-y-47)))))

