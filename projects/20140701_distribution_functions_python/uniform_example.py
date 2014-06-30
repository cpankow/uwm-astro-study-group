#!/usr/bin/env python

# Run this code with
# python uniform_example.py

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Generate a uniform continuous distribution
# between 0 and 1. Compute and print out the
# first few moments.
dist = stats.uniform(0,1)
mean, var, skew, kurt = dist.stats(moments='mvsk')
print "Uniform distribution from 0 to 1"
print "mean=", mean[()]
print "variance=", var[()]
print "skew=", skew[()]
print "kurtosis=", kurt[()], "\n"

# 10 random draws
r1 = dist.rvs(10)
print "10 Random Samples from Uniform Distrib"
print "mean=", r1.mean()
print "variance=", r1.var(), "\n"
np.savetxt('rd_10_uniform.txt', r1, fmt='%1.7f')

# 100 random draws
r2 = dist.rvs(100)
print "100 Random Samples from Uniform Distrib"
print "mean=", r2.mean()
print "variance=", r2.var(), "\n"
np.savetxt('rd_100_uniform.txt', r2, fmt='%1.7f')

# 1000 random draws
r3 = dist.rvs(1000)
print "1000 Random Samples from Uniform Distrib"
print "mean=", r3.mean()
print "variance=", r3.var(), "\n"
np.savetxt('rd_1000_uniform.txt', r3, fmt='%1.7f')

# 10000 random draws
r4 = dist.rvs(10000)
print "10000 Random Samples from Uniform Distrib"
print "mean=", r4.mean()
print "variance=", r4.var(), "\n"
np.savetxt('rd_10000_uniform.txt', r4, fmt='%1.7f')

fig, ax = plt.subplots(1, 1)
ax.hist(r1, normed=True, histtype='stepfilled', alpha=0.8, label='10')
ax.hist(r2, normed=True, histtype='stepfilled', alpha=0.6, label='100')
ax.hist(r3, normed=True, histtype='stepfilled', alpha=0.4, label='1000')
ax.hist(r4, normed=True, histtype='stepfilled', alpha=0.2, label='10000')
ax.legend(loc='upper left', frameon=False)
plt.show()
