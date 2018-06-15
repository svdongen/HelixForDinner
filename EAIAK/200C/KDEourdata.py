import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from scipy.stats import gaussian_kde
from scipy.stats.distributions import norm
from sklearn.model_selection import GridSearchCV

# The grid we'll use for plotting
x_grid = np.linspace(0, 1, 1000)

#calculates the pdf from input data and input grid            
def kde_sklearn(x, x_grid, bandwidth=0.2, **kwargs):
    """Kernel Density Estimation with Scikit-learn"""
    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(x[:, np.newaxis])
    # score_samples() returns the log-likelihood of the samples
    log_pdf = kde_skl.score_samples(x_grid[:, np.newaxis])
    return np.exp(log_pdf)


#datafile
temperature = 200
datafilename = "Helixpercentage.csv"
KDEfilename = "KDE" + str(temperature) + "C.csv"
figfilename = "Distribution" + str(temperature) + "C.png"

#load file
data = np.genfromtxt(datafilename, delimiter=",")

# use estimated bandwidth for the KDE
bandwidth = 0.05

fig, ax = plt.subplots(1, 1, sharey=True, tight_layout=True)
                
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
ax.hist(data[:,1], bins=16, normed=1)
pdf = kde_sklearn(data[:,1], x_grid, bandwidth=bandwidth)
ax.plot(x_grid, pdf, color='black', alpha=0.5, lw=3)

plt.ylabel('Probablity density')
plt.xlabel('Alpha helix ratio')

#save KDE data
np.savetxt(KDEfilename, pdf, delimiter=",")

ax.set_xlim(0,1)

plt.savefig(figfilename, dpi=300)
#plt.show()
			
	
	
