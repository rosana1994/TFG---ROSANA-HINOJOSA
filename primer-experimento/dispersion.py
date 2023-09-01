import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('p-values-matrix.txt', delimiter='\t', header=None)


sns.set(style='ticks')
sns.pairplot(data, plot_kws={'s': 2})


plt.tight_layout()
plt.savefig('dispersion_matrix.png')  # Save the plot as an image file
plt.show()
