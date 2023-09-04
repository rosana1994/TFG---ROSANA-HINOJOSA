import numpy as np

# Load the pass-fail matrix from a file
pass_fail_matrix = np.loadtxt('pass-fail-matrix.txt', dtype=int)

# Define the test names
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

# Initialize an empty correlation matrix
num_tests = len(test_names)
correlation_matrix = np.zeros((num_tests, num_tests))

# Calculate the correlation matrix
for i in range(num_tests):
    for j in range(num_tests):
        if i == j:
            continue
        # Find sequences that fail the first test
        fail_first_test = pass_fail_matrix[:, i] == 0

        # Find sequences that fail both tests
        fail_both_tests = np.logical_and(fail_first_test, pass_fail_matrix[:, j] == 0)

        # Calculate the correlation
        correlation = np.sum(fail_both_tests) / np.sum(fail_first_test)

        # Store the correlation in the matrix
        correlation_matrix[i, j] = correlation

# Print the correlation matrix
print("Asymmetric Correlation Matrix:")
print(correlation_matrix)
