import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('traces.csv', delimiter=',', unpack=True) # load the data from the text file using comma as separator and unpack it into x and y arrays

plt.plot(x,y, label='Data from trace.txt') # plot x and y values with a label
plt.xlabel('x') # set the label for x axis
plt.ylabel('y') # set the label for y axis
plt.title('Plotting data from a text file') # set the title for the plot
plt.legend() # show the legend
plt.show() # show the plot
