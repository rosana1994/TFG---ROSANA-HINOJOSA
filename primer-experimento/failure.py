import numpy as np

# Read p-values from the file
p_values_matrix = np.genfromtxt("p-values-matrix.txt", delimiter="\t", missing_values='NA')

# Remove missing values from the matrix
p_values_matrix = np.ma.masked_invalid(p_values_matrix)

# Set the threshold values
lower_threshold = 0.001
upper_threshold = 0.9990

# Initialize the failure counts for each test
failure_counts = np.zeros(p_values_matrix.shape[1], dtype=int)

# Iterate over each column (test)
for i in range(p_values_matrix.shape[1]):
    test_p_values = p_values_matrix[:, i].compressed()  # Remove missing values
    
    # Count the number of failures for the current test
    failures = np.sum((test_p_values < lower_threshold) | (test_p_values > upper_threshold))
    
    # Update the failure count for the current test
    failure_counts[i] = failures

# Print the failure counts for each test
for i, count in enumerate(failure_counts):
    print(f"Test {i+1}: {count} sequences failed")

