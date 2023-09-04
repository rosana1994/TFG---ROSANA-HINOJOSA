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
data = pd.read_csv('correlation_significance.txt', delimiter='\t', header=None)


# Exclude diagonal and upper-right part of the correlation matrix
mask = np.triu(np.ones_like(data, dtype=bool))

# Find the maximum correlation value for setting the color scale
max_corr_value = data.values[~mask].max()

# Set the figure size (adjust as needed)
plt.figure(figsize=(10, 8))

# Create a heatmap with values and smaller font size
sns.heatmap(data, cmap=sns.color_palette("ch:start=.2,rot=-.3", as_cmap=True), square=True,
            mask=mask, vmin=0, vmax=max_corr_value,
            annot=True, fmt=".2f", annot_kws={"size": 8},
            xticklabels=test_names, yticklabels=test_names)

# Add labels and title
plt.title("")



# Save the heatmap as an image file
plt.savefig('corre_significance.png')

# Display the heatmap
plt.show()

