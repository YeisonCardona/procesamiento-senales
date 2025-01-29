# %% [markdown]
# # Representación Matricial de la Transformada de Fourier
#
# En esta sección, exploraremos la representación de la Transformada de Fourier en forma matricial, utilizada frecuentemente en aplicaciones computacionales y en álgebra lineal.

# %% [markdown]
# ## Definición Matemática
#
# La Transformada Discreta de Fourier (DFT) puede expresarse en forma matricial como:
#
# $$ X = W_N x $$
#
# Donde:
# - $X$ es el vector transformado en el dominio de la frecuencia.
# - $x$ es el vector de entrada en el dominio del tiempo.
# - $W_N$ es la matriz de Fourier de tamaño $N \times N$, cuyos elementos están definidos como:
#
# $$ W_N(k, n) = e^{-j 2\pi kn/N} $$
#
# La matriz $W_N$ es una matriz de coeficientes exponenciales complejos que permite calcular la DFT mediante un producto matricial en lugar de una suma directa.

# %% [markdown]
# ## Construcción de la Matriz de Fourier
#
# La matriz $W_N$ tiene una estructura especial donde cada elemento está dado por una raíz de la unidad compleja elevada a una potencia específica.
#
# - La primera fila y la primera columna de $W_N$ contienen solo unos.
# - Cada fila representa una frecuencia armónica creciente.
# - Los valores son simétricos y periódicos en torno a $N$.

# %% [markdown]
# ## Ejemplo: Matriz de Fourier $4 \times 4$
#
# Para $N = 4$, la matriz de Fourier $W_4$ se construye como:
#
# $$
# W_4 = \begin{bmatrix}
# 1 & 1 & 1 & 1 \\
# 1 & e^{-j\pi/2} & e^{-j\pi} & e^{-j3\pi/2} \\
# 1 & e^{-j\pi} & e^{-j2\pi} & e^{-j3\pi} \\
# 1 & e^{-j3\pi/2} & e^{-j3\pi} & e^{-j9\pi/2}
# \end{bmatrix}
# $$

# %%
import numpy as np

# Definir N
N = 4

# Construcción de la matriz de Fourier cuadrada
k = np.arange(N)
n = k.reshape((N, 1))  # Convertir en columna para el producto matricial
W_4 = np.exp(-2j * np.pi * k * n / N)

# Mostrar la matriz
print("Matriz de Fourier W_4:")
print(np.round(W_4, 3))  # Redondear para mejor visualización

# %% [markdown]
# ## Matriz de Fourier Rectangular ($6 \times 4$)
#
# En ciertos casos, podemos definir una matriz de Fourier **no cuadrada**, como cuando tenemos más frecuencias en la salida que muestras en la señal original.
#
# Para una matriz $W_{6,4}$ de dimensiones $6 \times 4$:

# %%
M, N = 6, 4  # Filas y columnas
k = np.arange(M).reshape(M, 1)  # Vector de frecuencias
n = np.arange(N).reshape(1, N)  # Vector de tiempo
W_6_4 = np.exp(-2j * np.pi * k * n / N)  # Matriz rectangular

# Mostrar la matriz rectangular
print("Matriz de Fourier W_6_4:")
print(np.round(W_6_4, 3))  # Redondear para mejor visualización

# %% [markdown]
# ## Implementación en Python
#
# A continuación, implementaremos la DFT en forma matricial utilizando `numpy`.

# %%
# Definir la función para calcular la DFT mediante la matriz de Fourier
def dft_matrix(N):
    k = np.arange(N)
    n = k.reshape((N, 1))  # Convertir en columna para el producto matricial
    W = np.exp(-2j * np.pi * k * n / N)
    return W

# Señal de ejemplo
N = 8  # Tamaño de la señal
t = np.arange(N)
x = np.sin(2 * np.pi * t / N)  # Señal senoidal de ejemplo

# Calcular la DFT usando la matriz de Fourier
W = dft_matrix(N)
X = W @ x  # Multiplicación matricial

# Mostrar la matriz de Fourier
print("Matriz de Fourier W_N:")
print(np.round(W, 3))  # Redondear para mejor visualización

# %% [markdown]
# ## Visualización de la Transformada
#
# Se graficarán la señal original y su espectro de Fourier.

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))

# Señal original
t = np.linspace(0, N-1, N)
plt.subplot(1, 2, 1)
plt.stem(t, x, use_line_collection=True)
plt.title("Señal original")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.grid()

# Magnitud del espectro de Fourier
plt.subplot(1, 2, 2)
plt.stem(np.abs(X), use_line_collection=True)
plt.title("Espectro de Fourier (Magnitud)")
plt.xlabel("Frecuencia")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()

# %% [markdown]
# Esta implementación muestra cómo la Transformada de Fourier puede calcularse eficientemente usando su representación matricial, tanto en forma cuadrada como rectangular.
