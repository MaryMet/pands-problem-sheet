# plot task - Week 08
# Author : MAry Metcalfe

import matplotlib.pyplot as plt # using matplot
import numpy as np    # importing numpy

xpoints = np.array(range(1,10))
ypoints = xpoints * xpoints * xpoints

plt.plot(xpoints, ypoints, label = "xcubed", color = "red", ls = ":", lw ="2")

plt. legend()
plt.title ("Number Cubed", color = "green")
plt.xlabel ("Number", color ="green")
plt.ylabel ("Number Cubed", color ="green")

#data = rand(1, 1000)
#num_bins =10
#histogram (data, num_bins)
#xpoints("Data Value", Colour ="purple")
#ypoints("Count", Color = "red")

#mu = mean(data)   
##stdev = std(data)


#plt.hist()
plt.show()  