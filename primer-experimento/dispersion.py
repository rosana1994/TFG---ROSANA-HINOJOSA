import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read the data from file
data = pd.read_csv('p-values-matrix.txt', delimiter='\t', header=None)

# Create a pairplot with custom settings
sns.set(style='ticks')
custom_kws = {'s': 10, 'color': '#007ACC'}  # Custom point size and color

# Create a grid of subplots
grid = sns.PairGrid(data, diag_sharey=False)
grid.map_upper(plt.scatter, **custom_kws)  # Scatter plot for upper triangle
grid.map_diag(sns.histplot, kde_kws={'color': 'red'})  # Histograms on the diagonal

# Remove upper-right triangle by setting the axis off
for i, j in zip(*np.triu_indices_from(grid.axes, 1)):
    grid.axes[i, j].set_visible(False)

# Adjust the layout and display the plot
plt.tight_layout()
plt.savefig('dispersion_matrix.png')  # Save the plot as an image file
plt.show()
