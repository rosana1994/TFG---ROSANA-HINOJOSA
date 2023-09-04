import numpy as np
from scipy import stats

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

# Read data from file
data = []
with open("p-values-matrix.txt", "r") as file:
    for line in file:
        values = line.strip().split("\t")
        if len(values) == 15:  # Ignore lines with missing values
            data.append([float(val) for val in values])

# Convert data to a NumPy array
data = np.array(data)

# Sample size (number of values to randomly select)
sample_size = 500

# Perform Kolmogorov-Smirnov test for each dataset with a random sample
for i, column_name in enumerate(test_names):
    print("Dataset:", column_name)
    
    # Randomly sample 10,000 values from the column
    random_sample = np.random.choice(data[:, i], size=sample_size, replace=False)
    
    # Perform the Kolmogorov-Smirnov test on the random sample
    statistic, p_value = stats.kstest(random_sample, 'uniform')
    
    print("Kolmogorov-Smirnov statistic:", statistic)
    print("p-value:", p_value)
    print()
