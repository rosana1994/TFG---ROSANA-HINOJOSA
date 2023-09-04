import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Read the data from the file
data = pd.read_csv('p-values-matrix.txt', sep='\t')

# Drop rows with missing values
data = data.dropna()

# Calculate the correlation matrix using Pearson correlation
corr_matrix = data.corr()

# Create a mask to hide the upper triangle (including the diagonal)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Create a colormap with a clear gradient
cmap = sns.cubehelix_palette(start=0.7, rot=0, dark=0, light=1, reverse=False, as_cmap=True)

# Set the test names
test_names = data.columns.tolist()

# Create the correlation heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap=cmap, fmt='.2f', square=True, mask=mask,
                      xticklabels=test_names, yticklabels=test_names)
heatmap.tick_params(axis='both', labelsize=6)
plt.title('Correlation Heatmap')
plt.savefig("correlation_heatmap.png")

# Calculate the p-value matrix
pvalue_matrix = pd.DataFrame(index=corr_matrix.index, columns=corr_matrix.columns, dtype=float)
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        x = data[corr_matrix.columns[i]]
        y = data[corr_matrix.columns[j]]
        corr, p_val = pearsonr(x, y)
        pvalue_matrix.iloc[i, j] = p_val

# Convert p-value matrix to float
pvalue_matrix = pvalue_matrix.astype(float)

# Create the p-value heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(pvalue_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, mask=mask,
                      xticklabels=test_names, yticklabels=test_names)
heatmap.tick_params(axis='both', labelsize=6)
plt.title('P-value Heatmap')
plt.savefig("pvalue_heatmap.png")
