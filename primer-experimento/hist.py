import numpy as np
import matplotlib.pyplot as plt

# Lee tus datos desde el archivo 'data.txt'
data = np.genfromtxt('p-values-matrix.txt', delimiter='\t')

# Nombres de las pruebas
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

# Crear 15 subplots (uno para cada columna)
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(15, 10))
fig.subplots_adjust(hspace=0.5)

for i, ax in enumerate(axes.flatten()):
    if i < data.shape[1]:
        ax.hist(data[:, i], bins=20, edgecolor='k')
        ax.set_title(f'{test_names[i]}')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frecuencia')

# Ajusta el espacio entre los subplots
plt.tight_layout()

# Mostrar los histogramas
plt.show()
