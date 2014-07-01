import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

#seed the random number program
seed = 0
np.random.seed(0)

#Generate a poisson distribution, create four data sets with 10, 100,
#1000, and 10000 random numbers, and save each data set to its own file.
samples1 = np.random.poisson(5, size=10)
np.savetxt('10-Poisson-values.txt', samples1, fmt='%1.7f')

samples2 = np.random.poisson(5, size=100)
np.savetxt('100-Poisson-values.txt', samples2, fmt='%1.7f')

samples3 = np.random.poisson(5, size=1000)
np.savetxt('1000-Poisson-values.txt', samples3, fmt='%1.7f')

samples4 = np.random.poisson(5, size=10000)
np.savetxt('10000-Poisson-values.txt', samples4, fmt='%1.7f')


#Generate four histogram plots, one for each data set, and display them all
#simultaneously

#The first plot will be in the top left
plt.figure(1)
plt.subplot(2,2,1) #(number of rows, number of colums, figure number)
count1, bins1, ignored1 = plt.hist(samples1, 12, facecolor = 'blue',
     normed=False)
#Label the axes and title the plot
plt.xlabel('Value')
plt.ylabel('Counts')
plt.title('N=10')

#Calculate the mean, mode, variance, skew, and kurtosis, then print them
mean1, var1, skew1, kurt1 = poisson.stats(5, moments='mvsk')
mode1 = np.bincount(samples1)
print'For N=10, the average value is ', samples1.mean(), ', the mode is ',\
    np.argmax(mode1), ', the variance is ', samples1.var(), ', the skew is ', skew1, \
    ', and the kurtosis is ', kurt1
print 


#The second plot will be on the top right
plt.subplot(2,2,2)
count2, bins2, ignored2 = plt.hist(samples2, 12, facecolor = 'green',
        normed = False)
#Label the axes and title the plot
plt.xlabel('Value')
plt.ylabel('Counts')
plt.title('N=100')
#Calculate the mean, mode, variance, skew, and kurtosis, then print them
mean2, var2, skew2, kurt2 = poisson.stats(5, moments='mvsk')
mode2 = np.bincount(samples2)
print'For N=100, the average value is ', samples2.mean(), 'the mode is ', \
    np.argmax(mode2), ', the variance is ',samples2.var(), ', the skew is ', skew2, \
    ', and the kurtosis is ', kurt2
print  


#The third plot will be on the bottom left
plt.subplot(2,2,3)
count3, bins3, ignored3 = plt.hist(samples3, 12, facecolor = 'red',
        normed = False)
#Label the axes and title the plot
plt.xlabel('Value')
plt.ylabel('Counts')
plt.title('N=1000')
#Calculate the mean, mode, variance, skew, and kurtosis, then print them
mean3, var3, skew3, kurt3 = poisson.stats(5, moments='mvsk')
mode3 = np.bincount(samples3)
print'For N=1000, the average value is ', samples3.mean(), 'the mode is',\
    np.argmax(mode3), ', the variance is ', samples3.var(), ', the skew is ', skew3, \
    ', and the kurtosis is ', kurt3
print  


#The fourth plot will be on the bottom right
plt.subplot(2,2,4)
count4, bins4, ignored4 = plt.hist(samples4, 12, facecolor = 'yellow',
        normed = False)
#Label the axes and title the plot
plt.xlabel('Value')
plt.ylabel('Counts')
plt.title('N=10000')
#Calculate the mean, mode, variance, skew, and kurtosis, then print them
mean4, var4, skew4, kurt4 = poisson.stats(5, moments='mvsk')
mode4 = np.bincount(samples4)
print'For N=10000, the average value is ', samples4.mean(), 'the mode is ', \
    np.argmax(mode4), ', the variance is ', samples4.var(), ', the skew is ', skew4, \
    ', and the kurtosis is ', kurt4
print  


#Show all the plots
plt.show()

#The skew and kurtosis should be the same for all four data sets.

#You will probably need to adjust the spacing so the plots don't overlap.
#You can do this by clicking the spacing controls button, and moving the
#wspace and hspace sliders to the right until the plots no longer overlap.
         
