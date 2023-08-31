import re
import glob

# Los archivos tienen el formato test_results_i.txt con i desde 1 hasta 100000
file_pattern = 'test_results_*.txt'

# Se hace una lista con todos los nombres de los archivos que tienen este formato
file_names = glob.glob(file_pattern)

# Se ordenan 
file_names.sort(key=lambda name: int(re.search(r'\d+', name).group()))

# Estos son los nombres de los tests y los p-valores asociados a ellos
test_names = [
    'smarsa_BirthdaySpacings',
    'smultin_Multinomial',
    'sknuth_Gap',
    'sknuth_SimpPoker',
    'sknuth_CouponCollector',
    'sknuth_MaxOft',
    'svaria_WeightDistrib',
    'smarsa_MatrixRank',
    'sstring_HammingIndep',
    'swalk_RandomWalk1'
]
p_value_counts = [1, 1, 1, 1, 1, 2, 1, 1, 1, 5]

# Lista vacía para almacenar los valores
p_value_matrix = []

# Iteramos sobre cada archivo
for file_name in file_names:
    # Se lee
    with open(file_name, 'r') as file:
        content = file.read()

    # p_valores normales
    p_values = re.findall(r'p-value of test\s+:\s+([\d.e-]+)', content)

    # Si están en notación científica se pasa a decimal
    p_values = [float(p) if 'e' in p else p for p in p_values]

    # Se añade el p-valor a la fila
    p_value_matrix.append(p_values)

# Se escribe en el archivo la matrix
with open('p-values-matrix.txt', 'w') as file:
    for row in p_value_matrix:
        # Los p-valores con 4 valores decimales 
        formatted_row = [f'{p:.4f}' if isinstance(p, float) else p for p in row]
        file.write('\t'.join(formatted_row) + '\n')
