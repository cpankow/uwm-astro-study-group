from matplotlib import pylab as plt
import emcee
import random
import numpy as np

niteration = 2000
observeddata = np.loadtxt('orbit_obsv_data')
M = 1.0
#a = 1000
#e = 0.1
amin = 1000 - 0.5
amax = 1000 + 0.5
emin = 0.1 - 1e-3
emax = 0.1 + 1e-3
def eval_chisquared(moddata, obsdata):
	npts = len(obsdata)
	tarr = obsdata[:,0]
	xobs = obsdata[:,1]
	yobs = obsdata[:,2]
	simgar = obsdata[:,3]
	xmod = moddata[:,1]
	ymod = moddata[:,2]
	dx = xmod - xobs
	dy = ymod - yobs
	chisquared = np.sum((dx**2 + dy**2)/simgar**2)
	return chisquared

nEval = 0
def lnprob(param):
    global M
    global nEval
    if param[0]<amin or param[0]>amax or param[1]<emin or param[1]>emax: 
	return -np.inf
    else:
        print nEval
        a = param[0]
	e = param[1]
        b = a*(1-e**2)**0.5
	omega = (M/a**3)**0.5
	p = 2.0*np.pi/omega
	t = observeddata[:, 0]
	ma = omega*t
	ea = ma + e*np.sin(ma)
	x = a*(np.cos(ea) - e)
	y = b*np.sin(ea)
	modeldata = np.zeros((len(observeddata), 3))
	for i in np.arange(0, len(observeddata)):
		modeldata[i, 0] = t[i]
		modeldata[i, 1] = x[i]
                modeldata[i, 2] = y[i]
        chisquared = eval_chisquared(modeldata, observeddata) 
        nEval+=1
        lnprob = -0.5*chisquared 
        print "Iteration", nEval, ": Chi2", chisquared, " and params ", param
        return lnprob

ndim = 2
nwalkers = 10
p0 = []
for i in np.arange(0, nwalkers):
	p0.append([random.uniform(amin, amax), random.uniform(emin, emax)])
print "p0", p0
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, threads = 4)
sampler.run_mcmc(p0, niteration) 
print "sampler.acceptance_fraction.mean is", sampler.acceptance_fraction.mean()


f = open("parameterLnprob.txt", 'a')
for ii in range(nwalkers):
    for jj in range(niteration):
        f.write('\t'.join([str(sampler.chain[ii,jj,kk]) for kk in range(ndim)]))
        f.write('\t%e\t'%(sampler.lnprobability[ii,jj]))
        f.write('\n')
f.close()

np.savetxt("samplerFlatChain.txt", sampler.flatchain)


