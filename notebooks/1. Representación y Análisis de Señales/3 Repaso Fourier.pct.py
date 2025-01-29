# %% [markdown]
# # Repaso Fourier


# %% [markdown]
# # 1. Introducción
#
# En esta sección, exploraremos una breve introducción al trabajo de Fourier y su importancia en el área de señales y sistemas.

# %% [markdown]
# ## Breve historia de Fourier y sus aplicaciones
#
# Jean-Baptiste Joseph Fourier (1768-1830) fue un matemático y físico francés que desarrolló la idea de que cualquier función periódica puede representarse como la suma de funciones sinusoidales. Este concepto, conocido como la Serie de Fourier, es una herramienta fundamental en matemáticas, ingeniería y ciencia.
#
# ### Principales aportes:
# - Descomposición de funciones periódicas.
# - Aplicación a la transferencia de calor y la dinámica de sistemas.
#
# ### Ejemplos de aplicaciones modernas:
# - Procesamiento de señales: audio, video e imágenes.
# - Telecomunicaciones: modulación de señales.
# - Análisis espectral: investigación científica en física y química.

# %% [markdown]
# ## Importancia de la Transformada de Fourier en señales y sistemas
#
# La Transformada de Fourier permite convertir una señal del dominio del tiempo al dominio de la frecuencia, proporcionando información clave sobre el contenido frecuencial de la misma.
#
# ### Razones clave de su importancia:
# - **Análisis de sistemas lineales invariantes en el tiempo (LTI):** permite estudiar la respuesta de sistemas a diferentes frecuencias.
# - **Filtrado:** diseño y análisis de filtros pasa-bajo, pasa-alto, entre otros.
# - **Compresión de datos:** aplicación en algoritmos de compresión como JPEG o MP3.

# %% [markdown]
# ### Ejemplo visual:
# Más adelante, incluiremos código para demostrar cómo una señal compuesta puede descomponerse en componentes sinusoidales utilizando la Transformada de Fourier.


# %% [markdown]
# # 2. Conceptos Básicos
#
# En esta sección, se introducen los conceptos fundamentales necesarios para comprender el análisis de Fourier, incluyendo las series de Fourier y sus propiedades.

# %% [markdown]
# ## Series de Fourier
#
# Una serie de Fourier permite expresar una función periódica $f(t)$ como una suma infinita de funciones sinusoidales (senos y cosenos):
#
# $f(t) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos(2\pi n t) + b_n \sin(2\pi n t) \right)$
#
# Donde:
# - $a_0$: Término constante (promedio de la función).
# - $a_n, b_n$: Coeficientes de Fourier calculados como:
#
# $a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(2\pi n t) dt, \quad b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(2\pi n t) dt$

# %% [markdown]
# ## Propiedades fundamentales de Fourier
#
# Las series y transformadas de Fourier poseen propiedades que facilitan su aplicación en problemas reales. Algunas de las más importantes son:
#
# 1. **Linealidad:** La transformada de la suma de dos funciones es la suma de sus transformadas.
# 2. **Desplazamiento en el tiempo:** Un desplazamiento en el tiempo introduce un factor exponencial complejo en la transformada.
# 3. **Escalado:** Cambiar la escala del tiempo afecta inversamente la frecuencia.
# 4. **Dualidad:** Existe simetría entre el dominio del tiempo y el dominio de la frecuencia.

# %% [markdown]
# ## Diferencia entre Serie de Fourier y Transformada de Fourier
#
# | **Característica**                | **Serie de Fourier**                                              | **Transformada de Fourier**               |
# |-----------------------------------|-------------------------------------------------------------------|------------------------------------------|
# | **Dominio**                       | Tiempo continuo y periódico                                      | Tiempo continuo, no necesariamente periódico |
# | **Representación**                | Suma infinita de senos y cosenos                                  | Integral que relaciona tiempo y frecuencia |
# | **Aplicaciones principales**      | Análisis de señales periódicas                                   | Análisis de señales generales             |



# %% [markdown]
# # 3. Representaciones Matemáticas de Fourier
#
# La Transformada de Fourier puede representarse de diversas formas matemáticas, cada una con sus ventajas en aplicaciones específicas.

# %% [markdown]
# ## Representación exponencial
#
# La forma exponencial de Fourier utiliza exponentes complejos:
#
# $f(t) = \sum_{n=-\infty}^{\infty} C_n e^{j 2\pi n t}$
#
# donde $C_n$ son los coeficientes de Fourier en la representación compleja. Esta forma es útil en análisis de sistemas lineales y convolución en frecuencia.

# %% [markdown]
# ## Representación sinusoidal
#
# En esta representación, la función se expresa como la suma de senos y cosenos:
#
# $f(t) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos(2\pi n t) + b_n \sin(2\pi n t) \right)$
#
# donde los coeficientes $a_n$ y $b_n$ determinan la amplitud de las componentes senoidales.

# %% [markdown]
# ## Representación en forma matricial
#
# Se puede expresar la Transformada de Fourier en forma matricial, útil en computación numérica y análisis digital de señales. Para una señal discreta $x[n]$ de longitud $N$:
#
# $X = W_N x$
#
# donde $W_N$ es la matriz de coeficientes exponenciales de Fourier, y $x$ es el vector de valores de la señal.

# %% [markdown]
# ## Comparación entre formas
#
# - La **forma exponencial** es útil para análisis teórico y algebraico.
# - La **forma sinusoidal** es intuitiva y se usa en aplicaciones de audio y vibraciones.
# - La **forma matricial** es ideal para computación digital y aplicaciones en procesadores de señal.

# %% [markdown]
# Estas diferentes representaciones permiten analizar señales y sistemas de manera flexible dependiendo del contexto y la aplicación específica.




# %% [markdown]
# # 4. Transformada de Fourier
#
# La Transformada de Fourier es una herramienta matemática fundamental que permite analizar señales en el dominio de la frecuencia.

# %% [markdown]
# ## Definición matemática
#
# La Transformada de Fourier de una función $f(t)$ está dada por:
#
# $$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt$$
#
# Donde:
# - $F(\omega)$ representa la señal en el dominio de la frecuencia.
# - $f(t)$ es la señal en el dominio del tiempo.
# - $\omega$ es la frecuencia angular en radianes por segundo.

# %% [markdown]
# ## Ejemplos básicos
#
# ### 1. Transformada de un pulso rectangular
#
# Un pulso rectangular en el dominio del tiempo tiene la siguiente representación:
#
# $$f(t) = \begin{cases} 
# 1, & \text{si } |t| \leq \frac{T}{2} \\
# 0, & \text{si } |t| > \frac{T}{2}
# \end{cases}$$
#
# Su transformada de Fourier es:
#
# $$F(\omega) = T \text{sinc}\left(\frac{\omega T}{2}\right)$$

# %% [markdown]
# ### 2. Transformada de una función exponencial
#
# Para una función exponencial decreciente:
#
# $$f(t) = e^{-at}, \quad t \geq 0$$
#
# Su transformada de Fourier está dada por:
#
# $$F(\omega) = \frac{1}{a + j\omega}$$

# %% [markdown]
# ## Propiedades de la Transformada de Fourier
#
# 1. **Linealidad:**
#    $$\mathcal{F}\{af_1(t) + bf_2(t)\} = aF_1(\omega) + bF_2(\omega)$$
#
# 2. **Desplazamiento en el tiempo:**
#    $$\mathcal{F}\{f(t-t_0)\} = e^{-j\omega t_0}F(\omega)$$
#
# 3. **Escalado:**
#    $$\mathcal{F}\{f(at)\} = \frac{1}{|a|}F\left(\frac{\omega}{a}\right)$$
#
# 4. **Convolución:**
#    $$\mathcal{F}\{f_1(t) * f_2(t)\} = F_1(\omega)F_2(\omega)$$

# %% [markdown]
# Estas propiedades facilitan la manipulación de señales y la implementación de filtrado en el dominio de la frecuencia.


# %% [markdown]
# # 5. Transformada Rápida de Fourier (FFT)
#
# La Transformada Rápida de Fourier (FFT) es un algoritmo eficiente para calcular la Transformada Discreta de Fourier (DFT). Permite analizar rápidamente la composición frecuencial de señales discretas.

# %% [markdown]
# ## Introducción a la FFT
#
# La FFT es ampliamente utilizada en procesamiento de señales, compresión de datos y análisis espectral. Su principal ventaja es su eficiencia computacional, logrando reducir el tiempo de cálculo de $O(N^2)$ a $O(N \log N)$ en comparación con la DFT directa.

# %% [markdown]
# ## Ejemplos prácticos utilizando Python
#
# A continuación, implementaremos la FFT utilizando la librería `numpy` en Python.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Generar una señal senoidal con ruido
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)
freq1, freq2 = 50, 120  # Frecuencias en Hz
signal = np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t) + 0.5 * np.random.randn(len(t))

# Aplicar FFT
fft_signal = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(t), 1/fs)

# Graficar la transformada
plt.figure(figsize=(10, 5))
plt.plot(freqs[:fs//2], np.abs(fft_signal[:fs//2]))
plt.title("Espectro de la señal (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# %% [markdown]
# La FFT nos permite visualizar la composición espectral de la señal de manera rápida y eficiente, siendo una herramienta esencial en el análisis de señales.



# %% [markdown]
# # 6. Transformada de Fourier en Tiempo Discreto (DTFT)
#
# La Transformada de Fourier en Tiempo Discreto (DTFT) es una extensión de la Transformada de Fourier para señales discretas en el tiempo, proporcionando una representación continua en el dominio de la frecuencia.

# %% [markdown]
# ## Diferencias con la Transformada Continua
#
# - La **Transformada de Fourier Continua (CFT)** se aplica a señales continuas en el tiempo y proporciona un espectro continuo.
# - La **DTFT** trabaja con señales discretas en el tiempo pero produce una función continua en la frecuencia, lo que la diferencia de la Transformada Discreta de Fourier (DFT), que genera una versión discreta del espectro.
# - La DTFT es periódica en el dominio de la frecuencia con periodo $2\pi$.

# %% [markdown]
# ## Aplicaciones prácticas
#
# - Análisis de señales digitales en telecomunicaciones.
# - Diseño y análisis de filtros digitales.
# - Evaluación de estabilidad en sistemas de control discretos.

# %% [markdown]
# A continuación, se ilustrará cómo calcular la DTFT en Python utilizando la función de Fourier Transform en señales discretas.



# %% [markdown]
# # 7. Ejemplos Prácticos
#
# En esta sección, exploraremos ejemplos prácticos de análisis de señales utilizando la Transformada de Fourier.

# %% [markdown]
# ## Análisis de una señal periódica
#
# Se analizará cómo una señal periódica puede representarse en el dominio de la frecuencia mediante la Transformada de Fourier.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Generar una señal periódica (senoidal)
fs = 1000  # Frecuencia de muestreo
T = 1      # Duración de la señal en segundos
t = np.linspace(0, T, fs, endpoint=False)
freq = 50  # Frecuencia de la señal
signal = np.sin(2 * np.pi * freq * t)

# Aplicar FFT
fft_signal = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(t), 1/fs)

# Graficar la transformada
plt.figure(figsize=(10, 5))
plt.plot(freqs[:fs//2], np.abs(fft_signal[:fs//2]))
plt.title("Espectro de la señal periódica (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# %% [markdown]
# ## Análisis de una señal no periódica
#
# Evaluaremos cómo una señal no periódica se comporta en el dominio de la frecuencia y qué información podemos extraer de ella.

# %%
# Generar una señal no periódica (pulso)
signal = np.zeros(fs)
signal[fs//4:3*fs//4] = 1  # Pulso rectangular

# Aplicar FFT
fft_signal = np.fft.fft(signal)

# Graficar la transformada
plt.figure(figsize=(10, 5))
plt.plot(freqs[:fs//2], np.abs(fft_signal[:fs//2]))
plt.title("Espectro de la señal no periódica (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# %% [markdown]
# ## Filtrado en el dominio de la frecuencia
#
# Se mostrará cómo aplicar filtros en el dominio de la frecuencia para eliminar componentes no deseadas de una señal.

# %%
# Generar una señal con ruido
noisy_signal = signal + 0.5 * np.random.randn(len(signal))

# Aplicar FFT
fft_noisy_signal = np.fft.fft(noisy_signal)

# Filtrado: Eliminar frecuencias altas
threshold = 100  # Frecuencia de corte
fft_filtered = fft_noisy_signal.copy()
fft_filtered[np.abs(freqs) > threshold] = 0

# Reconstrucción con IFFT
filtered_signal = np.fft.ifft(fft_filtered)

# Graficar la señal filtrada
plt.figure(figsize=(10, 5))
plt.plot(t, noisy_signal, label="Señal con ruido")
plt.plot(t, filtered_signal.real, label="Señal filtrada", linewidth=2)
plt.title("Filtrado en el dominio de la frecuencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()



# %% [markdown]
# # 8. Aplicaciones de Fourier
#
# La Transformada de Fourier es ampliamente utilizada en diversas áreas. Algunas aplicaciones incluyen:

# %% [markdown]
# ## Procesamiento de señales
#
# - Análisis y filtrado de señales de audio.
# - Procesamiento de imágenes y video.
# - Identificación de patrones en señales biológicas.

# %% [markdown]
# ## Compresión de datos (imágenes y audio)
#
# - Compresión de imágenes mediante algoritmos como JPEG.
# - Reducción de datos en señales de audio mediante MP3 y otros formatos.
# - Eliminación de redundancias en señales digitales para optimización de almacenamiento.

# %% [markdown]
# ## Análisis espectral
#
# - Identificación de componentes frecuenciales en señales físicas.
# - Uso en espectroscopia, telecomunicaciones y otras disciplinas científicas.
# - Evaluación de estructuras y vibraciones en ingeniería.

# %% [markdown]
# Estas aplicaciones hacen de la Transformada de Fourier una herramienta esencial en múltiples áreas de la ciencia y la tecnología.















































