# Author: Jake VanderPlas
# Edited by M. DeCesar for UWM python class, 2014-07-22
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

from astroML.resample import bootstrap
from astroML.stats import sigmaG

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

m = 1000  # number of points
n = 10000  # number of bootstraps

#------------------------------------------------------------
# sample values from a normal distribution
np.random.seed(123)
data = norm(0, 1).rvs(m)  ## m random draws from normal dist; see 3.3

#------------------------------------------------------------
# Addition by M. DeCesar
# Take a look at your data
xx = np.linspace(1,m,num=m)
plt.figure()
plt.plot(xx,data)
plt.xlabel('Data Bin')
plt.ylabel('Data Value')
plt.title('Sample Values from a Normal Distribution')
#plt.savefig('normdist_sample')
plt.show()

#------------------------------------------------------------
# Compute bootstrap resamplings of data
mu1_bootstrap = bootstrap(data, n,  np.std, kwargs=dict(axis=1, ddof=1))
mu2_bootstrap = bootstrap(data, n, sigmaG, kwargs=dict(axis=1))

#------------------------------------------------------------
# Addition by M. DeCesar
# Take a look at what the bootstrap output is
print len(mu1_bootstrap)
print mu1_bootstrap
print len(mu1_bootstrap)
print mu2_bootstrap

#------------------------------------------------------------
# Compute the theoretical expectations for the two distributions
x = np.linspace(0.8, 1.2, 1000)     ## len(x) = m

sigma1 = 1. / np.sqrt(2 * (m - 1))  ## Standard error of mean, eq 3.35
pdf1 = norm(1, sigma1).pdf(x)       ## PDF of norm dist at x; length = m

sigma2 = 1.06 / np.sqrt(m)    ## Width of "perfect" Gaussian, eq. 3.36-3.38
pdf2 = norm(1, sigma2).pdf(x) ## PDF of norm dist at x; length = m

#------------------------------------------------------------
# Plot the results
fig, ax = plt.subplots(figsize=(5, 3.75))

ax.hist(mu1_bootstrap, bins=50, normed=True, histtype='step',
        color='blue', ls='dashed', label=r'$\sigma\ {\rm (std. dev.)}$')
ax.plot(x, pdf1, color='gray')

ax.hist(mu2_bootstrap, bins=50, normed=True, histtype='step',
        color='red', label=r'$\sigma_G\ {\rm (quartile)}$')
ax.plot(x, pdf2, color='gray')

ax.set_xlim(0.82, 1.18)

ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$p(\sigma|x,I)$')

ax.legend()

plt.show()
