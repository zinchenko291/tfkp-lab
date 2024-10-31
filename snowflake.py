import matplotlib.pyplot as plt
import os
from typing import Tuple, List

# Константы
ITERATIONS = 6
POINTS = ((0, 0), (1, 0), (0.5, (3 ** 0.5) / 2))
SAVE_FOLDER = "img/koch_snowflake"
os.makedirs(SAVE_FOLDER, exist_ok=True)

def koch_segment(start: Tuple[float, float], end: Tuple[float, float], depth: int) -> List[Tuple[float, float]]:
    if depth == 0:
        return [start, end]
    
    s = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    d = ((end[0] - start[0]) / 3, (end[1] - start[1]) / 3)
    p1 = (start[0] + d[0], start[1] + d[1])
    p2 = (end[0] - d[0], end[1] - d[1])
    peak = (s[0] + (d[1] * (3 ** 0.5) / 2), s[1] - (d[0] * (3 ** 0.5) / 2))
    
    return koch_segment(start, p1, depth - 1) + [peak] + koch_segment(p2, end, depth - 1)

def koch_snowflake(iterations: int) -> List[Tuple[float, float]]:
    snowflake = []
    for i in range(3):
        start = POINTS[i]
        end = POINTS[(i + 1) % 3]
        snowflake += koch_segment(start, end, iterations)
    return snowflake

snowflake = koch_snowflake(ITERATIONS)

plt.figure(figsize=(8, 8))
x, y = zip(*snowflake)
plt.plot(x, y)
plt.fill(x, y, 'b', alpha=0.5)
plt.axis('equal')
plt.title(f"Снежинка Коха (Итерации: {ITERATIONS})")

file_path = os.path.join(SAVE_FOLDER, f"koch_snowflake_{ITERATIONS}.png")
plt.savefig(file_path)
plt.close()
