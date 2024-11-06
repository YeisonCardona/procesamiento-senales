# Procesamiento Digital de Señales (DSP)

Bienvenidos al curso de **Procesamiento Digital de Señales (DSP)**, un espacio diseñado para aprender y aplicar técnicas de análisis y manipulación de señales en Python. Este repositorio contiene todo el material necesario: clases teóricas, laboratorios de simulación, proyectos y recursos adicionales.

## Objetivo del Curso

Este curso tiene como objetivo desarrollar competencias en modelado, análisis y procesamiento de señales en los dominios de tiempo y frecuencia, utilizando Python como herramienta de implementación. Los estudiantes aprenderán a:

- Representar y manipular señales en el dominio del tiempo y frecuencia.
- Implementar transformadas de Fourier y wavelets.
- Diseñar y aplicar filtros digitales.
- Utilizar técnicas de detección y clasificación en señales.

## Contenidos del Curso

El curso se divide en cuatro bloques principales, cada uno con módulos específicos para desarrollar un conjunto de habilidades en el análisis de señales:

1. **Representación y Análisis de Señales**
   - Manipulación básica de señales en Python.
   - Muestreo y teorema de Nyquist.
   - Representación en dominio de frecuencia.
   - Transformada rápida de Fourier (FFT).

2. **Descomposición y Análisis en el Dominio Tiempo-Frecuencia**
   - Transformada de Fourier de Tiempo Corto (STFT).
   - Transformada Wavelet Discreta (DWT).
   - Transformada Wavelet Continua (CWT).
   - Aplicaciones prácticas y análisis comparativo.

3. **Filtrado de Señales**
   - Diseño de filtros digitales.
   - Filtros de paso bajo, paso alto, y bandas.
   - Filtrado en tiempo real.
   - Aplicaciones de filtrado en eliminación de ruido y análisis de señales biomédicas.

4. **Detección y Regresión en Señales**
   - Modelos de regresión y ajuste de curvas.
   - Clasificación y detección con el detector Bayesiano.
   - Métodos basados en vecindades y KNN.
   - Aplicaciones avanzadas en procesamiento de señales.

## Configuración del Entorno

Para trabajar con los laboratorios y ejercicios del curso, necesitarás instalar la biblioteca `dsp-utils`. Puedes encontrar el repositorio de esta biblioteca en [python-dsp-utils](https://github.com/YeisonCardona/python-dsp-utils) y usar el siguiente comando para instalarla:

```bash
pip install dsp-utils
```

Además, puedes instalar `jupyterlab` si prefieres ejecutar los laboratorios en cuadernos de Jupyter:

```bash
pip install jupyterlab
```

## Recursos y Material Adicional

Este repositorio incluye vínculos a proyectos y recursos adicionales en GitHub que complementan y expanden los temas cubiertos en el curso:

- [PythonPathway](https://github.com/YeisonCardona/PythonPathway): Serie de tutoriales de Python en niveles Básico, Intermedio y Avanzado. Aprende desde conceptos fundamentales hasta técnicas avanzadas para desarrollar habilidades sólidas en Python.
- [python-dsp-utils](https://github.com/YeisonCardona/python-dsp-utils): Conjunto de utilidades para procesamiento digital de señales en Python. Este recurso contiene funciones y herramientas específicas que se utilizarán a lo largo del curso para simplificar el desarrollo de proyectos.

## Estructura de Carpetas

- `lecturas/` – Notas y recursos teóricos.
- `proyectos/` – Proyectos finales de los estudiantes.
- `notebooks/` – Cuadernos de Jupyter con ejemplos prácticos y laboratorios.

## Metodología

La metodología del curso es activa y práctica. Cada tema incluye:
- **Teoría y ejercicios guiados** para asentar las bases.
- **Laboratorios en Python** donde aplicarás los conceptos en casos de estudio reales.
- **Proyecto final** en el que trabajarás con señales reales, implementando un análisis completo de principio a fin.

## Evaluación

1. **Laboratorios de Simulación (50%)**
   - Entrega 1: Semana 6 (Representación y Análisis de Señales).
   - Entrega 2: Semana 15 (Filtrado y Detección).

2. **Proyecto Final (50%)**
   - Entrega Propuesta: Semana 7 (Definición de objetivos y elección de datos).
   - Entrega Final: Semana 16 (Implementación y presentación de resultados).
