import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.io import wavfile
from scipy import signal

print("\nDone!")


randomData = pd.read_csv(r"C:\Users\Mateo\Desktop\Neurotech\data\one_calm.csv")
print(randomData.head())

channel1 = []
channel2 = []
channel3 = []
channel4 = []

with open("data/one_calm.csv", "r") as data:
    for line in data:
        line = line.split(",")
        channel1.append(float(line[0]))

for point in range(len(channel1)):
    if(point%2 != 0):
        channel1[point] = channel1[point-1]

# Plot the data
time = np.arange(0, len(channel1), 1)

plt.plot(time, channel1)
plt.xlabel("Time Sample")
plt.ylabel("μV")
plt.show()
plt.clf()

