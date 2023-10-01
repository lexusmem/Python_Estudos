import numpy as np
import array as arr

# ↓↓↓↓↓↓↓ARRAY↓↓↓↓↓↓↓
# No python possui array padrão
# porem não recomendado

# Array padrão Python:
teste_array_python = arr.array('d', [1, 3.5])
print(teste_array_python)

# Quando for utilizar array
# É utilizado a biblioteca numpay

# Array Numpy:
teste_numpay_python = np.array([1, 3.5])
print(teste_numpay_python)
teste_numpay_python += 3.75
print(teste_numpay_python)
