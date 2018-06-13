import time
import numpy as np;
import seaborn as sns;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#basedirectiory
path = "../EAAAK/"

#array of temperature values of temperatures 
temperatures = [5, 20, 50, 75, 100, 150, 200]
tempno = len(temperatures)

#initialize heatmap matrix
data = np.zeros([1000,tempno])

print data.shape

tempiter = 0
#load data for each temperature
for temp in temperatures:	
	#create filename
	thisfilename =  str(path) + str(temp) + "C/" + "KDE" + str(temp) + "C.csv"
	#print thisfilename
	newdata = np.genfromtxt(thisfilename, delimiter=",")
	data[:,tempiter] = newdata
	tempiter += 1
	

#print data


ax = sns.heatmap(data, cmap="hot")
#ax1 = sns.heatmap(data, cmap="PRGn", robust=True, square=True, fmt="d")
#ax1.set_aspect('equal','box-forced')
#ax1.set_xticklabels(myxticklabels)
#ax1.set_yticklabels(myyticklabels)
plt.show()
plt.savefig('mytest.png')





