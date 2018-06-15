import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd

headerlines = 9
window = 100
saltbridgefilelist = ["saltbr-GLU2-LYS16","saltbr-GLU12-LYS11","saltbr-GLU12-LYS16","saltbr-GLU2-LYS6","saltbr-GLU2-LYS11","saltbr-GLU7-LYS6","saltbr-GLU7-LYS11","saltbr-GLU7-LYS16","saltbr-GLU12-LYS6"]

finaldata = np.zeros([10002,2])
specificdata = np.zeros([10002,2])
timesteps = 10002
timearray = np.linspace(1,timesteps,timesteps)
hbondfilename = "hbonds.csv"

print timearray

#import helix data
helixity = np.genfromtxt("Helixpercentage.csv", delimiter=",")

def fMovingAvererage(data, windowlength):
	average = np.sum(data) / float(windowlength)	
	return average
	
#load hydrogen data
hbonds = np.genfromtxt(hbondfilename, delimiter=" ")

#loop over all files for each saltbridge possiblity
for currentbridge in saltbridgefilelist:	
	#load current saltbridge file
	with open(currentbridge+".dat", "r") as currentfile:
		currentdata = np.genfromtxt(currentfile, delimiter=" ")
		
		
	plotdatama = np.zeros([10002,2])
	helixityma = np.zeros([10002,2])
	hbondsma = np.zeros([10002,2])
	
	#do moving averages
	for j in range(window,timesteps-window):
		#do moving average		
		plotdatama[j,1] = fMovingAvererage(currentdata[(j-window):(j+window),1],2*window)
	for j in range(window,timesteps-window):
		#do moving average		
		helixityma[j,1] = fMovingAvererage(helixity[(j-window):(j+window),1],2*window)	
	for j in range(window,timesteps-window):
		#do moving average		
		hbondsma[j,1] = fMovingAvererage(hbonds[(j-window):(j+window),1],2*window)
	
	
	
	plotdatama[:,1] = plotdatama[:,1] / float(np.max(plotdatama[:,1]))
	hbondsma[:,1] = hbondsma[:,1] / float(np.max(hbondsma[:,1]))
	
	plt.plot(timearray,helixityma[:,1])
	plt.plot(timearray,plotdatama[:,1])
	plt.plot(timearray,hbondsma[:,1])
	plt.show()	
			
	#convert distances below 1 to a '1' for a salt bridge, above 4 to a 0 for no bridge
	#count with a loop
	for i in range(currentdata.shape[0]):
		#if distance is less than 4 Angstrom, add one more count to the number of salt bridges at that time.	
		specificdata[i,0] = i
		if currentdata[i,1] <= 4:
			finaldata[i,1] +=1
			specificdata[i,1] = 1
			
	if currentbridge == "saltbr-GLU2-LYS6":
		np.savetxt("test.csv", specificdata, delimiter=",")		
		
np.savetxt("saltbrdigedata.csv", finaldata, delimiter=",")
		
		

