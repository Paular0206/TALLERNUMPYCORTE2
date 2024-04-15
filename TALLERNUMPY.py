import numpy as np  # Importamos la biblioteca para trabajar con números de forma eficiente
import matplotlib.pyplot as plt  # Importamos la biblioteca para crear imágenes

def mandelbrot(h, w, maxit=20, r=2):
    """Devuelve una imagen del fractal de Mandelbrot de tamaño (h,w)."""

    # Definimos el área del plano complejo que nos interesa
    x = np.linspace(-2.5, 1.5, 4*h+1)  # Crea un array de coordenadas x con valores espaciados uniformemente
    y = np.linspace(-1.5, 1.5, 3*w+1)  # Crea un array de coordenadas y con valores espaciados uniformemente
    A, B = np.meshgrid(x, y)  # Combina x e y en una cuadrícula de números complejos (c = x + yi)
    C = A + B*1j  # Crea un plano complejo (cada punto representa un valor 'c')

    # Inicializamos variables para seguir las iteraciones
    z = np.zeros_like(C)  # Crea un array vacío para almacenar resultados (mismo tamaño que C)
    divtime = maxit + np.zeros(z.shape, dtype=int)  # Crea un array para registrar cuántas iteraciones toma para que cada punto (c) diverja (por defecto: max iteraciones)

    # Bucle que itera un número máximo de veces (maxit)
    for i in range(maxit):
        z = z**2 + C  # Este es el cálculo central de Mandelbrot (z = z^2 + c)
        diverge = abs(z) > r  # Comprueba si el valor absoluto de z supera un umbral determinado (indicando divergencia)
        div_now = diverge & (divtime == maxit)  # Comprueba qué puntos están divergiendo *ahora* (y no han divergido antes)
        divtime[div_now] = i  # Registra el número de iteración donde cada punto diverge
        z[diverge] = r  # Limita el valor de z para evitar cálculos extremos

    return divtime  # La función devuelve el array que contiene los conteos de iteración

# Borra cualquier gráfico existente
plt.clf()

# Crea una imagen (gráfico) usando la salida de la función mandelbrot con un tamaño de 400x400 píxeles
plt.imshow(mandelbrot(400, 400))