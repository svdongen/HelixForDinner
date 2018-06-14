import time
import numpy as np;
import seaborn as sns;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc


#basedirectiory
peptide = "EAIAK"
path = "../" + str(peptide) + "/"

ylabels = [" "]*1000
ylabels[0] = 0
ylabels[249] = 0.25
ylabels[499] = 0.5
ylabels[749] = 0.75
ylabels[999] = 1

#array of temperature values of temperatures 
#temperatures = [5, 20, 50, 75, 100, 125, 150, 200]
temperatures = [5, 20, 50, 75, 100]
tempno = len(temperatures)

#initialize heatmap matrix
data = np.zeros([1000,tempno])

tempiter = 0
#load data for each temperature
for temp in temperatures:	
	#create filename
	thisfilename =  str(path) + str(temp) + "C/" + "KDE" + str(temp) + "C.csv"
	#print thisfilename
	newdata = np.genfromtxt(thisfilename, delimiter=",")
	data[:,tempiter] = newdata
	tempiter += 1
	
#flip data in the helixity axis

data = np.flip(data,axis=0)	

ax = sns.heatmap(data, cmap="Purples", fmt="d")
ax.set_xticklabels(temperatures)
ax.set_yticklabels(ylabels)
ax.tick_params(axis='both', which='major', labelsize=9)
plt.xlabel("Temperature (" + u'\N{DEGREE SIGN}' + "C)")
plt.ylabel(r'$\alpha$' + "-helix ratio")
#plt.show()
plt.savefig(str(peptide) + ".png", dpi=300)





