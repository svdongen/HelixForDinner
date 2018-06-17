import time
import numpy as np;
import seaborn as sns;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc


#basedirectiory
peptides = ["EAAAK", "EAIAK"]
figurename = "hbondcompare.png"

dataone = np.genfromtxt(str(peptides[0]) + "hbonddata.csv", delimiter=",")
datatwo = np.genfromtxt(str(peptides[1]) + "hbonddata.csv", delimiter=",")

#plot figure
#first peptide
plt.scatter(dataone[:,0],dataone[:,1])
plt.errorbar(dataone[:,0],dataone[:,1],yerr=dataone[:,4], linestyle="None")
#second peptide
plt.scatter(datatwo[:,0],datatwo[:,1])
plt.errorbar(datatwo[:,0],datatwo[:,1],yerr=datatwo[:,4], linestyle="None")

plt.xlabel("Temperature (" + u'\N{DEGREE SIGN}' + "C)")
plt.ylabel("No. of Hydrogen bonds")
plt.legend(peptides)
plt.savefig(figurename)
#plt.show()









