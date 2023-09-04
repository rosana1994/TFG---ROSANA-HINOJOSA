import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Lee tus datos desde el archivo 'data.txt'
data = np.genfromtxt('p-values-matrix.txt', delimiter='\t')

# Nombres de las pruebas (columnas)
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

# Crear una figura
plt.figure(figsize=(10, 6))

# Iterar a través de las columnas y trazar la ECDF de cada una
for i in range(data.shape[1]):
    # Calcular la ECDF de los datos
    x = np.sort(data[:, i])
    y = np.arange(1, len(x) + 1) / len(x)
    plt.step(x, y, label=test_names[i])

# Trazar la función de distribución acumulada teórica para una distribución uniforme
x_uniform = np.linspace(0, 1, 100)  # Valores x para la CDF uniforme
y_uniform = np.linspace(0, 1, 100)  # Valores y para la CDF uniforme
plt.plot(x_uniform, y_uniform, label='Uniforme Teórica', linestyle='--', color='black')

# Configurar etiquetas y leyenda
plt.xlabel('Valor')
plt.ylabel('Probabilidad acumulada')
plt.title('Funciones Empíricas de Distribución Acumulada (ECDF)')
plt.legend(loc='best')

# Mostrar la gráfica
plt.grid(True)
plt.show()
