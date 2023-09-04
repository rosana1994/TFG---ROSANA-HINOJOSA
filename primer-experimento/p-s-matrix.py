import pandas as pd
import numpy as np

# Read the p-values matrix from the file
data = pd.read_csv('p-values-matrix.txt', delimiter='\t', header=None)

# Define the threshold for passing the test
threshold = 0.01

# Create a pass-fail matrix by applying a condition to the p-values
pass_fail_matrix = (data >= threshold).astype(int)

# Save the pass-fail matrix to a file (if needed)
pass_fail_matrix.to_csv('pass-fail-matrix.txt', sep='\t', index=False, header=False)

# Display or further analyze the pass-fail matrix as needed
print(pass_fail_matrix)
