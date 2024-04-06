import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1000  # Número de muestras
N0 = 1.0  # Varianza (potencia) del ruido

# Generar ruido blanco gaussiano
def noise(N0,N):
    sigma = np.sqrt(N0)  # Desviación estándar
    ruido = np.random.normal(0, sigma, N)
    return ruido

# # Crear arreglo de tiempo
# t = np.arange(N)

# # Graficar
# plt.figure(figsize=(10, 5))
# plt.plot(t, ruido)
# plt.title('Ruido Blanco Gaussiano (AWGN)')
# plt.xlabel('Tiempo')
# plt.ylabel('Amplitud')
# plt.grid(True)
# plt.show()
