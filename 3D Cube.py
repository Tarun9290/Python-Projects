#3D CUBE CODE IN PYTHON

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure() 
ax = Axes3D(fig) 

# creating array of points for cube 
points = [[1, 1, 1],  
          [1, 1, -1], 
          [1, -1, 1], 
          [1, -1, -1], 
          [-1, 1, 1], 
          [-1, 1, -1], 
          [-1, -1, 1], 
          [-1, -1, -1]] 

# creating edges of cube 
edges = [[0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 3],  
         [2, 6], [3, 7], [4, 5], [4, 6], [5, 7], [6, 7]] 

# plotting cube 
for edge in edges: 
	ax.plot3D(*zip(points[edge[0]], points[edge[1]]), color='b') 

# show plot 
plt.show()