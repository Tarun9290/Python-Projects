#DATA VISUALISATION:creating a bar chart using Plotly library:

import plotly.graph_objs as go

# Sample data
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 7, 14, 5, 8]

# Create a bar chart
fig = go.Figure(data=[go.Bar(x=x, y=y)])

# Add labels and title
fig.update_layout(title='Bar chart', xaxis_title='X-axis label', yaxis_title='Y-axis label')

# Display the plot
fig.show()
