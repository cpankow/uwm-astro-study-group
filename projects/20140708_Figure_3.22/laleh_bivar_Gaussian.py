import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from astroML.stats import bivariate_normal
from matplotlib.patches import Ellipse

sigma1 = 2
sigma2 = 1
alpha = np.pi/4
sigmax = 1.58
sigmay = 1.58
sigmaxy = 1.50

np.random.seed(0)

mu = np.array([0,0])
x = bivariate_normal(mu, sigma1, sigma2, alpha, size=1000000, return_cov=False)

fig = plt.figure()
ax = fig.add_subplot(111)
H, bins = np.histogramdd(x, bins=2*[np.linspace(-6, 6, 2 * np.sqrt(1000000))])

ax.imshow(H, cmap=plt.cm.Purples, extent=(-4.5, 4.5, -4.5, 4.5), interpolation='nearest')

for j in (1, 2, 3):
    ell = Ellipse(mu, j*sigma1, j*sigma2, angle=alpha*180./np.pi)
    ell.set_facecolor('none')
    ax.add_patch(ell)
plt.show()

