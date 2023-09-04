import numpy as np

# Read p-values from the file
p_values_matrix = np.genfromtxt("p-values-matrix.txt", delimiter="\t")

# Set the threshold values
lower_threshold = 0.001
upper_threshold = 0.9990

# Initialize a boolean array to store whether each sequence failed any test
sequence_failed = np.any((p_values_matrix < lower_threshold) | (p_values_matrix > upper_threshold), axis=1)

# Calculate the number of sequences that failed at least one test
num_failed_sequences = np.sum(sequence_failed)

print(f"Number of sequences that failed at least one test: {num_failed_sequences}")
