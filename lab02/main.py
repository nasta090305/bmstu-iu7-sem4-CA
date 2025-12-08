from funcs import *
import numpy as np
import matplotlib.pyplot as plt


def graph(x, y):
    inter_x = np.arange(min(x), max(x), 0.1)
    plt.figure(figsize=(12, 4))
    plt.subplot(141)
    plt.plot(inter_x, [count_spline(x, y, i, 2) for i in inter_x])
    plt.subplot(142)
    plt.plot(inter_x, [count_spline(x, y, i, 3) for i in inter_x])
    plt.subplot(143)
    plt.plot(inter_x, [count_newton(x, y, 3, i) for i in inter_x])
    plt.subplot(144)
    plt.plot(inter_x, [count_spline(x, y, i, 1) for i in inter_x])
    plt.show()


with open("table.txt", "r") as f:
    nums = [list(map(float, i.split())) for i in f]
    x, y = [], []
    for i in nums:
        x += [i[0]]
        y += [i[1]]

try:
    val = float(input("Введите значение, для которого необходимо произвести интерполяцию:\n"))
except Exception:
    print("Некорректные входные данные")
    exit()

print("ньютон = ", count_newton(x, y, 3, val))
print("сплайн с естественными краевыми условиями = ", count_spline(x, y, val, 1))
print("сплайн со второй производной полинома Ньютона в Х0 = ", count_spline(x, y, val, 2))
print("сплайн со вторыми производными полинома Ньютона на краях = ", count_spline(x, y, val, 3))

#graph(x, y)