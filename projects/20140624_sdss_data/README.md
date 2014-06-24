# Week 3 (6/24/2014) -- SDSS Data Handling

 * Presenters: Sarah Caudill (physarah (at) g + mail , com)
 * Topics: Introduction to Data Handling Using SDSS

## Preliminaries

Have you successfully installed all the code? You can check in the following ways:

 * What [Python](https://www.python.org) do you have? It should be version 2.6.x - 2.7.x. In your terminal, type:
```
$ python --version
Python 2.7.1
```
 * Do you have the basic packages for mathematical and scientific computing? These are [Numpy](http://www.numpy.org), [Scipy](http://www.scipy.org), and [matplotlib](http://matplotlib.org). What versions do you have? It should be Numpy >= 1.4, Scipy >= 0.7, and matplotlib >= 0.99. In your terminal, open an ipython session and check the versions:
```
$ ipython

In [1]: import numpy

In [2]: print numpy.__version__
1.6.1

In [3]: import scipy

In [4]: print scipy.__version__
0.10.0

In [5]: import matplotlib

In [6]: print matplotlib.__version__
1.1.0
```
 * Do you have the packages for machine learning in python? This is the [scikit-learn](http://scikit-learn.org) software. What version do you have? It should be scikit-learn >= 0.10. In your ipython session, type:
```
In [7]: import sklearn

In [8]: print sklearn.__version__
0.15.0b1
```
 * Do you have the core astronomy packages? This is [astropy](http://www.astropy.org). What version do you have? It should be astropy >= 0.2.5. In your ipython session, type:
```
In [9]: import astropy

In [10]: print astropy.__version__
0.3.2
```
 * Finally, do you have the software meant to accompany this book for machine learning and data mining? This is the [astroML](http://www.astroml.org/index.html) software. In your ipython session, type:
```
In [11]: import astroML

In [12]: print astroML.__version__
0.2
```

## SDSS Data

The Sloan Digital Sky Survey (SDSS) is a photometric and spectroscopic survey using a 2.5m telescope at Apache Point Observatory, New Mexico. The telescope has two instruments for large volume imaging and spectroscopic data.

Photometric data exists in five bands: u, g, r, i, and z. Photometry exists for 357 million unique sources in ~12000 deg^2 of sky. 
