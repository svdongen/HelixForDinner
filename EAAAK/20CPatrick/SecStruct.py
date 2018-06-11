import numpy as np
import time
import matplotlib.pyplot as plt


#load the timeline file
inputfilename = "20CSecondarystructure.txt"
outputfilename = "Helixpercentage.csv"
finaldatafilename = "AverageHelix.csv"
#set number of lines that make up the header
headerlines = 9
peptidesize = 15
#set how many time blocks to calculate a time average
AverageBlocks = 10
#select how many blocks will be used to calculate the final average, starting from the final block
Lastblocks = 8

#load data from file into numpy array
data2d = np.genfromtxt(inputfilename, delimiter=" ", skip_header=headerlines, dtype=object)
#delete columns 2 to 4, as they contain no info
#leave the residue number and the structure type
data2d = np.column_stack((data2d[:,0],data2d[:,4]))

#calculate number of timepoints from the number of rows
timesteps = data2d.shape[0] / peptidesize

#stack the 2d array into the third time dimension
#so first axis is the number of columns of the text file, second axis is the 15 residues, third axis is the time axis
data = np.reshape(data2d,(timesteps, peptidesize, data2d.shape[1]))

#change value of the structure column to '1' if structure is 'H' for helix, if not, change to '0'
data[data[:,:,1] == 'H', 1] = 1
data[data[:,:,1] != 1, 1] = 0

#and now convert fromt string to int
data = data.astype(np.int)

#average over the residue dimension, axis 1
average = data.mean(axis=(1))

timedataaverage = np.zeros([timesteps,2])
timedataaverage[:,0]  = np.arange(timesteps)
timedataaverage[:,1]  = average[:,1]

#save average to csv
np.savetxt(outputfilename, timedataaverage, delimiter=',')

#plot percentage of helix against time
#plt.plot(timedataaverage[:,0],timedataaverage[:,1])
#plt.ylim([0,1])
#plt.show()


timeaverages = np.zeros([AverageBlocks])

#calculae timepoints per block
BlockLength = timesteps / AverageBlocks

#do loop for each block
for i in range(AverageBlocks):
	#select the time data for current block, average over it, and save the average for that block	
	timeaverages[i] = np.mean(timedataaverage[i*BlockLength:(i+1)*BlockLength,1])	
	

with open(finaldatafilename, "w") as finaldatafile:
	#calculate the average of the blocks and the stdev	
	finaldatafile.write("average," + str(np.mean(timeaverages[(AverageBlocks-Lastblocks):AverageBlocks])) + ",STD," + str(np.std(timeaverages[(AverageBlocks-Lastblocks):AverageBlocks])) + "\n\n")
#and write the average value for each block
with open(finaldatafilename, "a") as finaldatafile:
	for i in range(AverageBlocks):
		finaldatafile.write("Block " + str(i+1) + "," + str(timeaverages[i]) + "\n")
	
	

			
	
	
