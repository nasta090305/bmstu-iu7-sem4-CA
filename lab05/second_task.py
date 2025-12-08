import math as m


def laplas_func(left: float, right: float, steps: int):
    summ = 0
    if left >= right:
        return 0
    h = (right - left) / steps
    x = left
    while x < right:
        summ += h * (m.exp(-x**2 / 2) + m.exp(-(x + h)**2 / 2)) / 2
        x += h
    summ /= m.sqrt(m.pi * 2)
    return summ


def find_x(f_x: float, eps: float):
    if f_x >= 0.5:
        return None
    x_big = 1
    f_big = laplas_func(0, x_big, 1000)
    while f_big < f_x:
        x_big *= 2
        f_big = laplas_func(0, x_big, 1000)
    x_r = x_big
    x_l = 0
    f = laplas_func(0, (x_r + x_l) / 2, 1000)
    max_iter = 1000
    iterations = 1
    while abs((f - f_x) / f_x) > eps and iterations < max_iter:
        if f > f_x:
            x_r = (x_r + x_l) / 2
        else:
            x_l = (x_r + x_l) / 2
        f = laplas_func(0, (x_r + x_l) / 2, 1000)
        iterations += 1
    print(f"Найденный x = {(x_r + x_l) / 2}")
    print(f"Значение F(x) = {f}")
    print(f"Произведено {iterations} итераций")
    return (x_r + x_l) / 2
