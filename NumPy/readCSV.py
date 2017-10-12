# Internet Usage per Minute
# http://vincentarelbundock.github.io/Rdatasets/datasets.html
# A time series of the numbers of users connected to the Internet through a server every minute.

import numpy as np
import matplotlib.pyplot as plt

from numpy import genfromtxt
my_data = genfromtxt('internetUsage.csv', delimiter=',')

k = my_data.astype(int)
print("The Data:")
print("---------")
print(k)
print("---------")

print("Average Values:")
print(np.average(k,axis=0))
print("Mean Values:")
print(np.mean(k,axis=0))
print("Max Values:")
print(np.max(k,axis=0))
print("Min Values:")
print(np.min(k,axis=0))
print("Median Values:")
print(np.median(k,axis=0))
print("Standard Deviation Values:")
print(np.std(k,axis=0))
print("Variance Values:")
print(np.var(k,axis=0))

plt.plot(k)
plt.xlabel('Minutes')
plt.ylabel('Number of Connected Users')
plt.title('Internet Usage per Minute')
plt.grid(True)
plt.savefig("internet_usage.png")
plt.show()
