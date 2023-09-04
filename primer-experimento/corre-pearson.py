import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define the column names
test_names = [
    'smarsa_BirthdaySpacings',
    'smultin_Multinomial',
    'sknuth_Gap',
    'sknuth_SimpPoker',
    'sknuth_CouponCollector',
    'sknuth_MaxOft 1',
    'sknuth_MaxOft 2',
    'svaria_WeightDistrib',
    'smarsa_MatrixRank',
    'sstring_HammingIndep',
    'swalk_RandomWalk1 1',
    'swalk_RandomWalk1 2',
    'swalk_RandomWalk1 3',
    'swalk_RandomWalk1 4',
    'swalk_RandomWalk1 5',
]

# Read the data from the file
data = pd.read_csv('p-values-matrix.txt', delimiter='\t', header=None)

# Calculate the Pearson Correlation Matrix
correlation_matrix = data.corr(method='pearson')

# Exclude diagonal and upper-right part of the correlation matrix
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Find the maximum correlation value for setting the color scale
max_corr_value = correlation_matrix.values[~mask].max()

# Set the figure size (adjust as needed)
plt.figure(figsize=(10, 8))

# Create a heatmap with values and smaller font size
sns.heatmap(correlation_matrix, cmap=sns.cubehelix_palette(as_cmap=True), square=True,
            mask=mask, vmin=0, vmax=max_corr_value,
            annot=True, fmt=".2f", annot_kws={"size": 8},
            xticklabels=test_names, yticklabels=test_names)

# Add labels and title
plt.title("")

# Save the correlation matrix as a .txt file with 4 decimal places
correlation_matrix.round(4).to_csv('correlation_matrix.txt', sep='\t', float_format='%.4f', index=True, header=True)

# Save the heatmap as an image file
plt.savefig('correlation_heatmap.png')

# Display the heatmap
plt.show()


