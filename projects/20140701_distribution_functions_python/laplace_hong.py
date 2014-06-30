#!/usr/bin/env python

# Run this code with
# python laplace_hong.py

from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Generate a Laplace distribution with mu = 0, and delta = 1.
# Compute and print out the first few moments.
dist = stats.laplace(0, 1.0)
mean, var, skew, kurt = dist.stats(moments='mvsk')
print "Laplace distribution with mu = 0 and delta = 1.0: "
print "mean =", mean[()]
print "variance =", var[()]
print "skew =", skew[()]
print "kurtosis =", kurt[()], "\n"

# Four random draws
# Calculate and print out the mean and variance
# Save each draw in a file
N_arr = np.array([10, 100, 1000, 10000]) 
r = [[],[],[],[]]
for i in np.arange(0, len(N_arr)):
	N = N_arr[i]
	r[i] = dist.rvs(N)
	print "%d Random Samples from Laplace Distribution:" % N
	print "mean =", r[i].mean() 
	print "variance =", r[i].var(), "\n"
	np.savetxt('laplace_samples_%d.txt' % N, r[i], fmt='%1.7f')

# Make plots
matplotlib.rcParams.update({'font.size':20})
fig, ax = plt.subplots(1, 1)
for i in np.arange(0, len(N_arr)):
        N = N_arr[i] 
	nBins = 3*np.floor(np.sqrt(N))
	hist, bin_edges = np.histogram(r[i], bins=nBins, density=True)
	ax.hist(r[i], nBins, normed=True, histtype='stepfilled', alpha=0.3+i*0.1, label='%d' % N)
plt.title("Laplace Distribution with $\mu = 0$ and $\Delta = 1.0$", size = 18)
plt.legend(loc = 0)
plt.show()


