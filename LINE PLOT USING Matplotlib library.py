#DATA VISUALISATION:Use libraries like Matplotlib to create visualizations of data. 
#You can use any dataset that you find interesting and create graphs, charts, and other visualizations.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [3, 6, 2, 7, 1]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Line plot')

# Display the plot
plt.show()
