import time
import numpy as np;
import seaborn as sns;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc

hbondfilename = "hbonds.dat"

#array of temperature values of temperatures 
#temperatures = [5, 20, 37, 50, 75, 100, 150, 200]
temperatures = [5, 20, 37, 50, 75, 100, 125, 150, 200]
tempno = len(temperatures)


for temp in temperatures:
	currentfilename = str(temp) + "C/" + str(hbondfilename)
	print currentfilename
	data = np.genfromtxt(currentfilename)
	print data.shape
