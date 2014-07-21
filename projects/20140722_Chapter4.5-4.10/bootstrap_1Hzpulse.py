# Bootstrapping example:  Estimate parameter uncertainty

# Script adapted from boostrap_fig4.3.py by Jake VanderPlas
# Adapted by M. DeCesar for UWM python class, 2014-07-22

import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt

from astroML.resample import bootstrap
from astroML.stats import sigmaG


#--------------------------------------------
# Open and read data file
infile = open('data02_14Jul22_1Hzpulse.dat','r')
lines = infile.readlines()
infile.close()


#--------------------------------------------
# Assign values to data array
data = np.zeros(len(lines))
for i in range(0,len(lines)):
    line = lines[i].strip('\n')
    data[i] = float(line)


#------------------------------------------------------------
# Extract some basic information about your data
m = len(data)  # number of data points
n = 10000      # number of bootstraps
print np.median(data)
s = np.std(data)
print s


#------------------------------------------------------------
# Compute bootstrap resamplings of data
mu1_bootstrap = bootstrap(data, n,  np.std, kwargs=dict(axis=1, ddof=1))
mu2_bootstrap = bootstrap(data, n, sigmaG, kwargs=dict(axis=1))


#------------------------------------------------------------
# Addition by M. DeCesar
# To take a look at what the bootstrap output is, uncomment lines below
"""
print len(mu1_bootstrap)
print mu1_bootstrap
print len(mu1_bootstrap)
print mu2_bootstrap
"""

#------------------------------------------------------------
# Compute the theoretical expectations for the two distributions; s=0.01
x = np.linspace(0.0, 0.02, num=m)     ## len(x) = m

sigma1 = s / np.sqrt(2 * (m - 1))   ## Standard error of mean, eq 3.35
pdf1 = norm(s, sigma1).pdf(x)       ## PDF of norm dist at x; length = m

sigma2 = 1.06*s / np.sqrt(m)    ## Sigma from inner 50% quantile; eq. 3.36-3.38
pdf2 = norm(s, sigma2).pdf(x)   ## PDF of norm dist at x; length = m



#----------------------------------------------------------------------
# Set up your plot style.  (Can also do this at the top.)
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)


#------------------------------------------------------------
# Plot the results
fig, ax = plt.subplots(figsize=(5, 3.75))

ax.hist(mu1_bootstrap, bins=50, normed=True, histtype='step',
        color='blue', ls='dashed', label=r'$\sigma\ {\rm (std. dev.)}$')
ax.plot(x, pdf1, color='gray')

ax.hist(mu2_bootstrap, bins=50, normed=True, histtype='step',
        color='red', label=r'$\sigma_G\ {\rm (quartile)}$')
ax.plot(x, pdf2, color='gray')

ax.set_xlim(0.008, 0.012)

ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$p(\sigma|x,I)$')

ax.legend()

plt.show()
