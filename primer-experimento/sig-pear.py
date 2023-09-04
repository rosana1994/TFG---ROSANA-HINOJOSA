import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Read the data from the file (excluding the first row and first column)
data = pd.read_csv('p-values-matrix.txt', delimiter='\t', header=None)

# Function to calculate the significance of Pearson correlation coefficients
def calculate_correlation_significance(matrix):
    n = matrix.shape[1]  # Number of variables

    # Create an empty matrix to store p-values
    p_value_matrix = np.zeros((n, n))

    # Calculate p-values for each pair of variables
    for i in range(n):
        for j in range(i + 1, n):
            r, p_value = pearsonr(matrix.iloc[:, i], matrix.iloc[:, j])
            p_value_matrix[i, j] = p_value
            p_value_matrix[j, i] = p_value  # Since the matrix is symmetric

    return p_value_matrix

# Calculate the significance matrix
significance_matrix = calculate_correlation_significance(data)

# Save the significance matrix to a file
np.savetxt('correlation_significance.txt', significance_matrix, delimiter='\t', fmt='%.4f')

# Print or further analyze the significance matrix as needed
print(significance_matrix)
