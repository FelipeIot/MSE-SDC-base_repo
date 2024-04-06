import numpy as np
import matplotlib.pyplot as plt

def cuadrada(Fs, Fo, amp, muestras):
    t = np.arange(0, muestras) / Fs
    cuadrada_signal = amp * (np.sign(np.sin(2 * np.pi * Fo * t)))
    return t, cuadrada_signal

def triangular(Fs, Fo, amp, muestras):
    t = np.arange(0, muestras) / Fs
    triangular_signal = amp * (2 * np.abs((t * Fo) - np.floor(0.5 + (t * Fo))))
    return t, triangular_signal

def sinusoidal(Fs, Fo, amp, muestras, fase):
    t = np.arange(0, muestras) / Fs
    sinusoidal_signal = amp * np.sin(2 * np.pi * Fo * t + fase)
    return t, sinusoidal_signal

# Función para generar una señal delta
def delta(Fs, muestras, posicion):
    t = np.arange(0, muestras) / Fs
    delta_signal = np.zeros(muestras)
    delta_signal[posicion] = 1.0
    return t, delta_signal

# # Ejemplos de uso de las funciones
# Fs = 1000  # Frecuencia de muestreo en Hz
# Fo = 10    # Frecuencia de la señal en Hz
# amp = 1.0  # Amplitud de la señal
# muestras = 1000
# fase = 0   # Fase solo para la señal sinusoidal

# # Generar las señales
# t_cuadrada, cuadrada_signal = cuadrada(Fs, Fo, amp, muestras)
# t_triangular, triangular_signal = triangular(Fs, Fo, amp, muestras)
# t_sinusoidal, sinusoidal_signal = sinusoidal(Fs, Fo, amp, muestras, fase)
# t_delta, delta_signal = delta(Fs, muestras, posicion=500)  # Señal delta en la posición 500

# # Calcular la FFT de las señales
# fft_cuadrada = np.fft.fft(cuadrada_signal)
# fft_triangular = np.fft.fft(triangular_signal)
# fft_sinusoidal = np.fft.fft(sinusoidal_signal)
# fft_delta = np.fft.fft(delta_signal)

# frequencies = np.fft.fftfreq(muestras, 1/Fs)

# # Graficar las señales y sus FFT en una sola ventana
# plt.figure(figsize=(12, 10))

# # Señal Cuadrada en el dominio del tiempo y su FFT
# plt.subplot(4, 2, 1)
# plt.plot(t_cuadrada, cuadrada_signal)
# plt.title('Señal Cuadrada en el Dominio del Tiempo')
# plt.grid(True)

# plt.subplot(4, 2, 2)
# plt.plot(frequencies, np.abs(fft_cuadrada))
# plt.title('FFT de la Señal Cuadrada')
# plt.grid(True)

# # Señal Triangular en el dominio del tiempo y su FFT
# plt.subplot(4, 2, 3)
# plt.plot(t_triangular, triangular_signal)
# plt.title('Señal Triangular en el Dominio del Tiempo')
# plt.grid(True)

# plt.subplot(4, 2, 4)
# plt.plot(frequencies, np.abs(fft_triangular))
# plt.title('FFT de la Señal Triangular')
# plt.grid(True)

# # Señal Sinusoidal en el dominio del tiempo y su FFT
# plt.subplot(4, 2, 5)
# plt.plot(t_sinusoidal, sinusoidal_signal)
# plt.title('Señal Sinusoidal en el Dominio del Tiempo')
# plt.grid(True)

# plt.subplot(4, 2, 6)
# plt.plot(frequencies, np.abs(fft_sinusoidal))
# plt.title('FFT de la Señal Sinusoidal')
# plt.grid(True)

# # Señal Delta en el dominio del tiempo y su FFT
# plt.subplot(4, 2, 7)
# plt.plot(t_delta, delta_signal)
# plt.title('Señal Delta en el Dominio del Tiempo')
# plt.grid(True)

# plt.subplot(4, 2, 8)
# plt.plot(frequencies, np.abs(fft_delta))
# plt.title('FFT de la Señal Delta')
# plt.grid(True)

# plt.tight_layout()
# plt.show()
