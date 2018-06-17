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
outputfilename = str(peptide) + "ahelix.csv"
figurename = str(peptide) + "ahelix.png"


#array of temperature values of temperatures 
temperatures = [5, 20, 37, 50, 75, 100, 125, 150, 200]
tempno = len(temperatures)

AverageBlocks = 10
BlockLength = 1000
timeaverages = np.zeros([AverageBlocks])
Lastblocks = 8
#calculae timepoints per block


#initialize heatmap matrix
helixdata = np.zeros([tempno,5])
#put temperature values in the array
helixdata[:,0] = temperatures

#load data for each temperature
for index,temp in enumerate(temperatures):	
	#create filename
	thisfilename =  str(path) + str(temp) + "C/Helixpercentage.csv"
	#print thisfilename
	newdata = np.genfromtxt(thisfilename, delimiter=",")
	timesteps = newdata.shape[0]
	#calculae timepoints per block
	BlockLength = timesteps / AverageBlocks

	#do loop for each block
	for i in range(AverageBlocks):
		#select the time data for current block, average over it, and save the average for that block	
		timeaverages[i] = np.mean(newdata[i*BlockLength:(i+1)*BlockLength,1])	
	
	#take the average no of hbonds from the last 8 blocks	
	helixdata[index,1] = np.mean(timeaverages[(AverageBlocks-Lastblocks):AverageBlocks])
	#and calculate the stdev
	helixdata[index,2] = np.std(timeaverages[(AverageBlocks-Lastblocks):AverageBlocks])


#calculate standard error and 96% confidence interval
helixdata[:,3] = helixdata[:,2] / float(np.sqrt(Lastblocks))
helixdata[:,4] = helixdata[:,3] * 1.96

#plot the data and save to file
plt.scatter(helixdata[:,0],helixdata[:,1])
plt.errorbar(helixdata[:,0],helixdata[:,1],yerr=helixdata[:,4], linestyle="None")
plt.ylim([0,1])
plt.xlabel("Temperature (" + u'\N{DEGREE SIGN}' + "C)")
plt.ylabel(r'$\alpha$' + "-helix ratio")
plt.savefig(figurename)
#plt.show()

#save the hbonddata with a header to a csv
np.savetxt(outputfilename, helixdata, delimiter=",", header="temperature,helicity,std,se,96%CI", comments='')
	





