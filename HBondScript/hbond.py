import time
import numpy as np;
import seaborn as sns;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc


#basedirectiory
#peptide = "EAAAK"
peptide = "EAIAK"
path = "../" + str(peptide) + "/"
outputfilename = str(peptide) + "hbonddata.csv"
figurename = str(peptide) + "hbond.png"


#array of temperature values of temperatures 
#temperatures = [5, 20, 37, 50, 75, 100, 150, 200]
temperatures = [5, 20, 37, 50, 75, 100, 125, 150, 200]
tempno = len(temperatures)

AverageBlocks = 10
BlockLength = 1000
timeaverages = np.zeros([AverageBlocks])
Lastblocks = 8
#calculae timepoints per block


#initialize heatmap matrix
hbonddata = np.zeros([tempno,5])
#put temperature values in the array
hbonddata[:,0] = temperatures

#load data for each temperature
for index,temp in enumerate(temperatures):	
	#create filename
	thisfilename =  str(path) + str(temp) + "C/" + str(temp) + "Chbonds.dat"
	#print thisfilename
	newdata = np.genfromtxt(thisfilename, delimiter=" ")
	timesteps = newdata.shape[0]
	#calculae timepoints per block
	BlockLength = timesteps / AverageBlocks

	#do loop for each block
	for i in range(AverageBlocks):
		#select the time data for current block, average over it, and save the average for that block	
		timeaverages[i] = np.mean(newdata[i*BlockLength:(i+1)*BlockLength,1])	
	
	#take the average no of hbonds from the last 8 blocks	
	hbonddata[index,1] = np.mean(timeaverages[(AverageBlocks-Lastblocks):AverageBlocks])
	#and calculate the stdev
	hbonddata[index,2] = np.std(timeaverages[(AverageBlocks-Lastblocks):AverageBlocks])


#calculate standard error and 96% confidence interval
hbonddata[:,3] = hbonddata[:,2] / float(np.sqrt(Lastblocks))
hbonddata[:,4] = hbonddata[:,3] * 1.96

#plot figure
plt.scatter(hbonddata[:,0],hbonddata[:,1])
plt.errorbar(hbonddata[:,0],hbonddata[:,1],yerr=hbonddata[:,4], linestyle="None")
plt.xlabel("Temperature (" + u'\N{DEGREE SIGN}' + "C)")
plt.ylabel("No. of Hydrogen bonds")
plt.savefig(figurename)
#plt.show()



#save the hbonddata with a header to a csv
np.savetxt(outputfilename, hbonddata, delimiter=",", header="temperature,hbonds,std,se,96%CI", comments='')
	





