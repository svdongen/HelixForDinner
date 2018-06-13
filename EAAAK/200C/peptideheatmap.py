import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns;


#load the timeline file
temperature = 200
inputfilename = str(temperature) + "CSecondarystructure.txt"
outputfilename = "Helixpercentage.csv"
finaldatafilename = "AverageHelix.csv"
#set number of lines that make up the header
headerlines = 9
peptidesize = 15
window = 100

xtickmarks = np.linspace(1,15,15)
xtickmarks = xtickmarks.astype(int)

# The grid we'll use for plotting
x_grid = np.linspace(0, 1, 1000)

# use estimated bandwidth for the KDE
bandwidth = 0.05

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


def fMovingAvererage(data, windowlength):
	average = np.sum(data) / float(windowlength)	
	return average
	

#initialize empty matrix for data
averageddata = np.zeros([timesteps,peptidesize])

#loop through all peptides
for i in range(peptidesize):
	#and through the entire time series
	for j in range(window,timesteps-window):
		#do moving average		
		averageddata[j,i] = fMovingAvererage(data[(j-window):(j+window),i,1],2*window)
		

#plot heatmap of time-peptide coordinates with average helix values
ax = sns.heatmap(averageddata, cmap="Purples")
ax.set_xticklabels(xtickmarks)
ax.set_yticklabels([])
ax.tick_params(axis='both', which='major', labelsize=9)
plt.xlabel("Peptide")
plt.ylabel("Time")
plt.savefig(str(temperature) +'Cpeptideheatmap.png')

	
	
