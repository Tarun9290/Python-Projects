#DATA VISUALISATION:creating a scatter plot using Seaborn library:

import seaborn as sns
import pandas as pd

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Add labels and title
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Tip vs. Total Bill')

# Display the plot
plt.show()
