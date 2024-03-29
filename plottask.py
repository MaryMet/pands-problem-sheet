# plot task - Week 08
# Author : MAry Metcalfe

import matplotlib.pyplot as plt # using matplot
import numpy as np    # importing numpy

mean = 5  # mean of the values is 5
stdev = 2 # standard deviation is 2
norm_data= mean + stdev *np.random.normal(size = 1000) # defining what we want in the histogram

plt.hist(norm_data, color = "yellow", edgecolor = "black", label = "normdata") # plot the normal data in a histogram - personalied to stand out
plt.legend() # putting the histogram into the legend - as per feedback

xpoints = np.array(range(1,10)) # numbers to be cubed on the x axis
ypoints = xpoints * xpoints * xpoints # cubes on the y axis

plt.plot(xpoints, ypoints, label = "xcubed", color = "red", ls = ":", lw ="2") # using your lectures this week - intersections show the cubes
plt. legend()
plt.title ("Number Cubed", color = "green") #use w3 schools to help me make it pretty
plt.xlabel ("Number", color ="green")
plt.ylabel ("Number Cubed", color ="green")
plt.show() 