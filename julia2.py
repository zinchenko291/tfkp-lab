import numpy as np
import matplotlib.pyplot as plt
import os
from typing import NamedTuple, Tuple

class JuliaSetConfig(NamedTuple):
    c: complex
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    width: int
    height: int
    max_iter: int

def julia(c: complex, max_iter: int, z: complex) -> int:
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def julia_set(config: JuliaSetConfig) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    r1 = np.linspace(config.xmin, config.xmax, num=config.width)
    r2 = np.linspace(config.ymin, config.ymax, num=config.height)
    return r1, r2, np.array([[julia(config.c, config.max_iter, complex(r, i)) for r in r1] for i in r2])

c_values = (complex(-0.7, 0.27015), complex(0.355, 0.355), complex(-0.4, 0.6))
max_iters = (50, 100, 200, 400)
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5
width, height = 800, 600

for idx, c in enumerate(c_values, start=1):
    folder_name = f"img/julya/experiment_{idx}"
    os.makedirs(folder_name, exist_ok=True)

    for count, max_iter in enumerate(max_iters, start=1):
        config = JuliaSetConfig(c=c, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
        r1, r2, julia_image = julia_set(config)
        file_path = os.path.join(folder_name, f"{count}.png")
        plt.imshow(julia_image, extent=(xmin, xmax, ymin, ymax), cmap='hot')
        plt.colorbar()
        plt.title(f"Множество Жюлиа для c={c} (макс. итераций: {max_iter})")
        plt.savefig(file_path)
        plt.close()
