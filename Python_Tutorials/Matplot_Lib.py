# This file is used to demonstrate the use of Matplotlib library in Python.
import matplotlib.pyplot as plt
import numpy as np

#Using the numpy library to generate some data for the graph
x = np.arange(6, 20+1, 2)
print(x)

#Having a function to generate the y values for the graph
y = x**3+x**2-190
print(y)

z = x**2+x-30


#Common Methods used in Matplotlib.Pyplot with regards to plotting a graph and visualizing data.                                                                                                                  
plt.plot(x, y, z)
plt.plot(x, y, 'b--')   #b-- is the color of the line in the graph
plt.plot(x, y, 'ro')    #ro is the color of the points in the graph
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph of y = x^3+x^2-190')
plt.grid()
plt.plot(x, y, marker='o', color='r', linestyle='--', linewidth=2, markersize=6)#This is the same as the above 3 lines of code but this time with the marker size and line width.

plt.show()      #To display the graph graphically.