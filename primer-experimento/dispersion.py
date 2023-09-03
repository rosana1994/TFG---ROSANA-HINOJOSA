import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from file
data = pd.read_csv('data.txt', delimiter='\t', header=None)

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

# Set column names for the first 15 columns
data.columns = test_names[:15]

# Create a grid of subplots
g = sns.PairGrid(data, corner=True)

# Map the lower diagonal plots
g.map_lower(sns.scatterplot, s=2, color='#50A5DA')

# Map the diagonal plots
g.map_diag(sns.histplot, color='#5093DA')

# Adjust the layout and display the plot
plt.tight_layout()
plt.savefig('dispersion_matrix.png')  # Save the plot as an image file
plt.show()
