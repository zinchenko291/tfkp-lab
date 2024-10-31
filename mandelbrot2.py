import numpy as np
import matplotlib.pyplot as plt
import os
from typing import NamedTuple, Tuple

class MandelbrotConfig(NamedTuple):
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    width: int
    height: int

def mandelbrot(c: complex, max_iter: int) -> int:
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def mandelbrot_set(config: MandelbrotConfig, max_iter: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    r1 = np.linspace(config.xmin, config.xmax, num=config.width)
    r2 = np.linspace(config.ymin, config.ymax, num=config.height)
    return r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 800, 600
max_iters = (50, 100, 200, 400)

# Папка для хранения результатов
folder_name = "img/mandelbrot"
os.makedirs(folder_name, exist_ok=True)

config = MandelbrotConfig(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height)

for count, max_iter in enumerate(max_iters, start=1):
    r1, r2, mandelbrot_image = mandelbrot_set(config, max_iter)
    
    # Путь для сохранения файла
    file_path = os.path.join(folder_name, f"experiment_{count}.png")
    
    # Построение и сохранение изображения
    plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax), cmap='hot')
    plt.colorbar()
    plt.title(f"Множество Мандельброта (макс. итераций: {max_iter})")
    plt.savefig(file_path)
    plt.close()
