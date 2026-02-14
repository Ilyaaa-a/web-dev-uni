import random
import math

def circle_square_mk(r, n):
   
    inside = 0
    for _ in range(n):
        # Генерируем точку в квадрате [-r, r] x [-r, r]
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        # Проверяем, попала ли точка в круг
        if x * x + y * y <= r * r:
            inside += 1
    
    square_area = (2 * r) ** 2  # площадь квадрата = 4 * r^2
    circle_area = square_area * (inside / n)
    return circle_area

if __name__ == '__main__':
    r = 1.0
    exact = math.pi * r * r
    
    print("Точное значение (π):", f"{exact:.6f}")
    print("-" * 40)
    
    for n in [100, 1000, 10000, 100000]:
        approx = circle_square_mk(r, n)
        error = abs(approx - exact)
        print(f"n = {n:>6} → площадь ≈ {approx:.6f}, погрешность = {error:.6f}")
        
# Точное значение (π): 3.141593
# ----------------------------------------
# n =    100 → площадь ≈ 3.080000, погрешность = 0.061593
# n =   1000 → площадь ≈ 3.156000, погрешность = 0.014407
# n =  10000 → площадь ≈ 3.147600, погрешность = 0.006007
# n = 100000 → площадь ≈ 3.136400, погрешность = 0.005193