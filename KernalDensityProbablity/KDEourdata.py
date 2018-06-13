import numpy as np
import time
import matplotlib.pyplot as plt

from sklearn.neighbors import KernelDensity
from scipy.stats import gaussian_kde
from scipy.stats.distributions import norm

from sklearn.model_selection import GridSearchCV

# The grid we'll use for plotting
x_grid = np.linspace(0, 1, 1000)

# Draw points from a bimodal distribution in 1D
np.random.seed(0)
x = np.concatenate([norm(-1, 1.).rvs(400),
                    norm(1, 0.3).rvs(100)])
pdf_true = (0.8 * norm(-1, 1).pdf(x_grid) +
            0.2 * norm(1, 0.3).pdf(x_grid))
            
def kde_sklearn(x, x_grid, bandwidth=0.2, **kwargs):
    """Kernel Density Estimation with Scikit-learn"""
    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(x[:, np.newaxis])
    # score_samples() returns the log-likelihood of the samples
    log_pdf = kde_skl.score_samples(x_grid[:, np.newaxis])
    return np.exp(log_pdf)


#datafile
datafilename = "Helixpercentage.csv"


#load file
rawdata = np.genfromtxt(datafilename, delimiter=",")
data = np.zeros([1000])
data = rawdata[:,1]

grid = GridSearchCV(KernelDensity(), {'bandwidth': np.linspace(0.1, 1.0, 20)}, cv=5, verbose=10) # 20-fold cross-validation
grid.fit(data[:, None])
print grid.best_params_

bandwidth = 0.01



fig, ax = plt.subplots(1, 1, sharey=True, tight_layout=True)


pdf = kde_sklearn(data, x_grid, bandwidth=bandwidth)
ax.plot(x_grid, pdf, color='blue', alpha=0.5, lw=3)
#ax.fill(x_grid, pdf_true, ec='gray', fc='gray', alpha=0.4)
ax.set_xlim(0,1)


plt.show()
			
	
	
