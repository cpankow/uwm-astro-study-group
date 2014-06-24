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

Photometric data:
 * exists in five bands: u, g, r, i, and z.
 * exists for 357 million unique sources in ~12,000 sq.deg. of sky.
 * precision is 0.01-0.02 mag.
 * faint limit is r~22.5.

Spectroscopic Data Release 7:
 * includes 1.6 million spectra: 900,000 galaxies, 120,000 quasars, 460,000 stars
 * wavelength coverage of 3800-9200 Angstroms

Stripe 82 observations:
 * includes many observations of same patch of sky.
 * allows for study of time-varying phenomena: asteroids, variable stars, quasars, supernovae
 * provided us with catalog of nonvarying stars with excellent precision

Data from SDSS is accessed via their [Catalog Archive Server (CAS)](http://cas.sdss.org/astrodr7/en/tools/search/sql.asp) using SQL queries. More on that below. We will not directly use CAS (although you can) but will instead use a set of astroML tools to get the data for these examples.

## SQL Queries

SDSS uses an [SQL-based search engine](http://cas.sdss.org/astrodr7/en/help/docs/sql_help.asp) to get data from CAS. SQL is the [Structured Query Language](http://en.wikipedia.org/wiki/SQL), a standard way of retrieving data from databases.

Let's break down the query on page 16 of the book. It is an SQL query to assemble a catalog of ~330,000 sources detected in SDSS images in the region bounded by 0deg < Right Ascension (RA) < 10deg and -1deg < Declination (DECL) < 1deg.

First, let's just design a query to select RA and DECL values from the PhotoTag table in CAS. This particular table includes a subset of the most popular data columns from the main table PhotoObjAll.
```sql
SELECT
  round(p.ra,6) as ra, round(p.dec,6) as dec
INTO mydb.SDSSimagingSample
FROM PhotoTag p
```
Here we have used SELECT to specify which parameters to retrieve and FROM to say that we want to get those parameters from the PhotoTag table (which we alias as "p"). The parameters that we want are the RA and DECL of all entries in PhotoTag. We use the round() function to say that we want these values to 6 decimal places. Finally, we want to put these into another table called mydb.SDSSimagingSample and the columns in this table will be called ra and dec too.

Now, let's design the query to only give us 0deg < RA < 10deg and -1deg < DECL < 1deg as we had originally wanted.
```sql
SELECT
  round(p.ra,6) as ra, round(p.dec,6) as dec
INTO mydb.SDSSimagingSample
FROM PhotoTag p
WHERE
   p.ra > 0.0 and p.ra < 10.0 and p.dec > -1 and p.dec < 1
```
Here we have used the WHERE clause to specify these limitations on the extracted data. Now our table mydb.SDSSimagingSample will only have entries for these RA and DECL ranges.

Now, what if we want mostly stars, quasars, and galaxies. Well, the PhotoTag table has a column called type that tells us whether a source is unresolved (type=6, mostly stars and quasars) and resolved (type=3, mostly galaxies). We can add another WHERE clause:
```sql
SELECT
  round(p.ra,6) as ra, round(p.dec,6) as dec,
  p.type
INTO mydb.SDSSimagingSample
FROM PhotoTag p
WHERE
   p.ra > 0.0 and p.ra < 10.0 and p.dec > -1 and p.dec < 1
   and (p.type = 3 OR p.type = 6)
```

Too remove other junk entries from the query, you need to include processing flag information that warns of possible problems with the object, image, and/or with the measurement of various quantities. The flags are a bit mysterious at a glance but lots of information can be found on the [SDSS website](http://www.sdss.org/dr7/products/catalogs/flags.html). The example in the book selects out ISOLATED objects ((p.flags & '16') = 0), removes objects with DEBLENDED_AS_MOVING or SATURATED flags ((p.flags & '4295229440') = 0), and selects out PRIMARY objects (p.mode = 1).

```sql
SELECT
  round(p.ra,6) as ra, round(p.dec,6) as dec,
  p.type,
  (case when (p.flags & '16') = 0 then 1 else 0 end) as ISOLATED
INTO mydb.SDSSimagingSample
FROM PhotoTag p
WHERE
  p.ra > 0.0 and p.ra < 10.0 and p.dec > -1 and p.dec < 1
  and (p.type = 3 OR p.type = 6) and
  (p.flags & '4295229440') = 0 and
  p.mode = 1
```
Note the use of the [case statement](http://msdn.microsoft.com/en-us/library/ms181765.aspx) for the ISOLATED flag.

Finally, there are alot more columns that you can select out of the PhotoTag table. You can get the r band extinction (extinction_r), model magnitudes that have not been interstellar medium correct (modelMag_X), the errors on those model magnitudes (modelMagErr_X), the point spread function magnitudes (psfMag_X), and the errors on those psf magnitudes (psfMagErr_X).
```sql
SELECT
  round(p.ra,6) as ra, round(p.dec,6) as dec,
  p.run,
  round(p.extinction_r,3) as rExtSFD,
  round(p.modelMag_u,3) as uRaw,
  round(p.modelMag_g,3) as gRaw,
  round(p.modelMag_r,3) as rRaw,
  round(p.modelMag_i,3) as iRaw,
  round(p.modelMag_z,3) as zRaw,
  round(p.modelMagErr_u,3) as uErr,
  round(p.modelMagErr_g,3) as gErr,
  round(p.modelMagErr_r,3) as rErr,
  round(p.modelMagErr_i,3) as iErr,
  round(p.modelMagErr_z,3) as zErr,
  round(p.psfMag_u,3) as uRawPSF,
  round(p.psfMag_g,3) as gRawPSF,
  round(p.psfMag_r,3) as rRawPSF,
  round(p.psfMag_i,3) as iRawPSF,
  round(p.psfMag_z,3) as zRawPSF,
  round(p.psfMagErr_u,3) as upsfErr,
  round(p.psfMagErr_g,3) as gpsfErr,
  round(p.psfMagErr_r,3) as rpsfErr,
  round(p.psfMagErr_i,3) as ipsfErr,
  round(p.psfMagErr_z,3) as zpsfErr,
  p.type,
  (case when (p.flags & '16') = 0 then 1 else 0 end) as ISOLATED
INTO mydb.SDSSimagingSample
FROM PhotoTag p
WHERE
  p.ra > 0.0 and p.ra < 10.0 and p.dec > -1 and p.dec < 1
  and (p.type = 3 OR p.type = 6) and
  (p.flags & '4295229440') = 0 and
  p.mode = 1 and 
  p.modelMag_r < 22.5 
```

## Getting SDSS Data: An Example

The astroML tool called fetch_sdss_galaxy_colors that we use in the example called galaxy_colors will return a record array. In this example, we will see an array called data where each element of data is a record that contains eight items. Those record items (aka field names) are 'u', 'g', 'r', 'i', 'z', 'specClass', 'redshift', and 'redshift_err'. The field names are an attribute of the dtype object defining the record structure and you can see these by typing:
```
In [11]: data.dtype.names
Out[11]: ('u', 'g', 'r', 'i', 'z', 'specClass', 'redshift', 'redshift_err')
```

## Concerning Chapter 2

Chapter 2 discusses several packages that can aid in faster computation on massive data sets. These may prove useful for later data handling. There are a few things to note:

 * Within the ipython interpreter, there are a number of "magic functions" marked by a % sign. Two important ones for determining run time are
  * %time
  * %timeit
