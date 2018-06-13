import time
import numpy as np;
import seaborn as sns;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


#basedirectiory
path = "/"

#array of temperature values of temperatures 
temperatures = [5, 20, 50, 75, 100, 150, 200]
tempno = len(temperatures)

#initialize heatmap matrix
data = np.zeros([1000,tempno])

print data.shape

#load data for each temperature
for temp in temperatures:
	#create filename
	thisfilename =  str(path) + "KDE" + str(temp) + "C.csv"
	#print thisfilename
	newdata = np.genfromtxt(thisfilename, delimiter=",")
	print newdata




ax1 = sns.heatmap(data, cmap="PRGn", robust=True, square=True, fmt="d", yticklabels=myyticklabels, xticklabels=myxticklabels)
ax1.set_aspect('equal','box-forced')
ax1.set_xticklabels(myxticklabels)
ax1.set_yticklabels(myyticklabels)
plt.savefig('mytest.png')





