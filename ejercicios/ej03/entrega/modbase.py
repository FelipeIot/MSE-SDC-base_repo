import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

from banco import *
from ruido import *

def generar_senal_aleatoria(n: int):
    # Generar n muestras aleatorias binarias (0 o 1)
    senal = np.random.randint(2, size=n)
    # Convertir los valores 0 a -1
    senal[senal == 0] = -1
    return senal

def insertar_ceros_entre_elementos(senal, m):
    senal_con_ceros = np.zeros(len(senal) + (len(senal) - 1) * m)
    senal_con_ceros[::m+1] = senal
    return senal_con_ceros

def canal(n:int):
    # Crear un array de ceros de longitud n
    canal = np.zeros(n)
    # Establecer el primer elemento como 1
    canal[0] = 1
    return canal

Fs = 16000000  # Hz
periodo = 1 / Fs
NSAMPLE = 16
NINPUT = 10
Fo = Fs/NSAMPLE
N0 = 0.05  # Varianza (potencia) del ruido

# Generar la señal aleatoria
b_signal = generar_senal_aleatoria(NINPUT)

d_signal = insertar_ceros_entre_elementos(b_signal, NSAMPLE)
t_d = np.arange(0, len(d_signal)) / Fs

# Generar señales sinusoidal, cuadrada y triangular
t_sinusoidal, sinusoidal_signal = sinusoidal(Fs, Fo, 2, NSAMPLE, 0)
t_cuadrada, cuadrada_signal = cuadrada(Fs, Fo, 2, NSAMPLE)
t_triangular, triangular_signal = triangular(Fs, Fo, 2, NSAMPLE)

# Convolver las señales generadas con d_signal
x_sinusoidal = np.convolve(sinusoidal_signal, d_signal, mode='same')
x_cuadrada = np.convolve(cuadrada_signal, d_signal, mode='same')
x_triangular = np.convolve(triangular_signal, d_signal, mode='same')

# Aplicar canal y ruido a las señales convolucionadas
h_signal_sinusoidal = np.convolve(x_sinusoidal, canal(len(x_sinusoidal)), mode='same')
n_signal_sinusoidal = noise(N0, len(h_signal_sinusoidal))
c_signal_sinusoidal = x_sinusoidal + n_signal_sinusoidal

h_signal_cuadrada = np.convolve(x_cuadrada, canal(len(x_cuadrada)), mode='same')
n_signal_cuadrada = noise(N0, len(h_signal_cuadrada))
c_signal_cuadrada = x_cuadrada + n_signal_cuadrada

h_signal_triangular = np.convolve(x_triangular, canal(len(x_triangular)), mode='same')
n_signal_triangular = noise(N0, len(h_signal_triangular))
c_signal_triangular = x_triangular + n_signal_triangular


# Plotear todas las señales
plt.figure(figsize=(10, 8))

# Senoidal
plt.subplot(3, 1, 1)
plt.stem(np.arange(len(x_sinusoidal)), x_sinusoidal, label='x[n] - Senoidal', use_line_collection=True)
plt.stem(np.arange(len(d_signal)), d_signal, label='d[n]', markerfmt='ro', linefmt='r-', basefmt=" ", use_line_collection=True)
plt.stem(np.arange(len(c_signal_sinusoidal)), c_signal_sinusoidal, label='c[n]', markerfmt='go', linefmt='g-', basefmt=" ", use_line_collection=True)
plt.title('Sinusoidal Signal')
plt.xlabel('Sample Index (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Cuadrada
plt.subplot(3, 1, 2)
plt.stem(np.arange(len(x_cuadrada)), x_cuadrada, label='x[n] - Cuadrada', use_line_collection=True)
plt.stem(np.arange(len(d_signal)), d_signal, label='d[n]', markerfmt='ro', linefmt='r-', basefmt=" ", use_line_collection=True)
plt.stem(np.arange(len(c_signal_cuadrada)), c_signal_cuadrada, label='c[n]', markerfmt='go', linefmt='g-', basefmt=" ", use_line_collection=True)
plt.title('Square Signal')
plt.xlabel('Sample Index (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Triangular
plt.subplot(3, 1, 3)
plt.stem(np.arange(len(x_triangular)), x_triangular, label='x[n] - Triangular', use_line_collection=True)
plt.stem(np.arange(len(d_signal)), d_signal, label='d[n]', markerfmt='ro', linefmt='r-', basefmt=" ", use_line_collection=True)
plt.stem(np.arange(len(c_signal_triangular)), c_signal_triangular, label='c[n]', markerfmt='go', linefmt='g-', basefmt=" ", use_line_collection=True)
plt.title('Triangular Signal')
plt.xlabel('Sample Index (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Calculate the FFT of the sinusoidal signal
x_spectrum_sinusoidal = np.abs(fft(x_sinusoidal))

# Calculate the FFT of the square signal
x_spectrum_cuadrada = np.abs(fft(x_cuadrada))

# Calculate the FFT of the triangular signal
x_spectrum_triangular = np.abs(fft(x_triangular))

# Calculate the FFT of the convolved square signal
c_spectrum_cuadrada = np.abs(fft(c_signal_cuadrada))

# Calculate the FFT of the convolved triangular signal
c_spectrum_triangular = np.abs(fft(c_signal_triangular))

# Calculate the FFT of the signal c_signal_sinusoidal
c_spectrum_sinusoidal = np.abs(fft(c_signal_sinusoidal))

# Calculate the frequency axes
freq_cuadrada = np.fft.fftfreq(len(x_spectrum_cuadrada), d=periodo)
freq_triangular = np.fft.fftfreq(len(x_spectrum_triangular), d=periodo)
freq_sinusoidal  = np.fft.fftfreq(len(x_spectrum_sinusoidal), d=periodo)
freq_c_cuadrada = np.fft.fftfreq(len(c_spectrum_cuadrada), d=periodo)
freq_c_triangular = np.fft.fftfreq(len(c_spectrum_triangular), d=periodo)
freq_c_sinusoidal = np.fft.fftfreq(len(c_spectrum_sinusoidal), d=periodo)

plt.figure(figsize=(18, 12))

# Subplot para la primera fila (sinusoidal)
plt.subplot2grid((3, 2), (0, 0))
plt.semilogy(freq_c_sinusoidal[freq_c_sinusoidal > 0], c_spectrum_sinusoidal[freq_c_sinusoidal > 0], label="Spectral Density - c_sinusoidal")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Densidad Espectral de c_sinusoidal')
plt.grid(True)
plt.legend()

plt.subplot2grid((3, 2), (0, 1))
plt.semilogy(freq_sinusoidal[freq_sinusoidal > 0], x_spectrum_sinusoidal[freq_sinusoidal > 0], label="Spectral Density - x_sinusoidal")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Densidad Espectral de x_sinusoidal')
plt.grid(True)
plt.legend()

# Subplot para la segunda fila (cuadrada)
plt.subplot2grid((3, 2), (1, 0))
plt.semilogy(freq_c_cuadrada[freq_c_cuadrada > 0], c_spectrum_cuadrada[freq_c_cuadrada > 0], label="Spectral Density - c_signal_cuadrada")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Densidad Espectral de c_signal_cuadrada')
plt.grid(True)
plt.legend()


plt.subplot2grid((3, 2), (1, 1)) 
plt.semilogy(freq_cuadrada[freq_cuadrada > 0], x_spectrum_cuadrada[freq_cuadrada > 0], label="Spectral Density - x_cuadrada")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Densidad Espectral de x_cuadrada')
plt.grid(True)
plt.legend()



# Subplot para la tercera fila (convolucionada)

plt.subplot2grid((3, 2), (2, 0))
plt.semilogy(freq_c_triangular[freq_c_triangular > 0], c_spectrum_triangular[freq_c_triangular > 0], label="Spectral Density - c_signal_triangular")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Densidad Espectral de c_signal_triangular')
plt.grid(True)
plt.legend()

plt.subplot2grid((3, 2), (2, 1)) 
plt.semilogy(freq_triangular[freq_triangular > 0], x_spectrum_triangular[freq_triangular > 0], label="Spectral Density - x_triangular")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Densidad Espectral de x_triangular')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()