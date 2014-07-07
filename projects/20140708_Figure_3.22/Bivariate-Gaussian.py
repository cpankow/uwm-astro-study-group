import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from astroML.stats import bivariate_normal
from matplotlib.patches import Ellipse


#define the variables (given in the book)
sigma1 = 2
sigma2 = 1
alpha = np.pi/4
sigmax = 1.58
sigmay = 1.58
sigmaxy = 1.50

#seed for duplicable results
np.random.seed(0)

#since we won't be giving the program values to plot, we start off with an
#empty array which will center our resulting plot at zero
mu = np.array([0,0])

#create the bivariate distribution with 100,000 samples
x = bivariate_normal(mu, sigma1, sigma2, alpha, size=100000, \
           return_cov=False)


#plot 2d histogram
fig = plt.figure()
ax = fig.add_subplot(111)

H, bins = np.histogramdd(x, bins=2*[np.linspace(-4.5, 4.5, np.sqrt(100000))])
#adding cmap=plt.cm.binary to plt.imshow after H makes plot black and white
#for color options, or instructions on how to make your own, see
#http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
ax.imshow(H, cmap=plt.cm.Purples, extent=(-4.5, 4.5, -4.5, 4.5), \
          interpolation='nearest')

#plot the ellipses
for j in (1, 2, 3):
    ell = Ellipse(mu, j*sigma1, j*sigma2, angle=alpha*180./np.pi)
    #if this next step is omitted, the ellipses will be filled in, not just
    #an outline, which will obscure the data
    ell.set_facecolor('none')
    ax.add_patch(ell)

plt.show()

#plt.oplot(ellipse(mu, sigma1, sigma2, angle=alpha)
