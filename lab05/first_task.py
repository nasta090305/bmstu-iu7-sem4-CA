import numpy as np


def f_1(x: float, y: float, z: float):
    return x**2 + y**2 + z**2 - 1


def f_2(x: float, y: float, z: float):
    return 2 * x**2 + y**2 - 4*z


def f_3(x: float, y: float, z: float):
    return 3 * x**2 - 4*y + z**2


def j_inverse(x: float, y: float, z: float):
    j = [[2*x, 2*y, 2*z], [4*x, 2*y, -4], [6*x, -4, 2*z]]
    j_inv = np.linalg.inv(np.array(j))
    return j_inv.tolist()


def new_params(x: float, y: float, z: float, j_inv: list[list[float]]):
    f1 = f_1(x, y, z)
    f2 = f_2(x, y, z)
    f3 = f_3(x, y, z)
    newx = x - j_inv[0][0] * f1 - j_inv[0][1] * f2 - j_inv[0][2] * f3
    newy = y - j_inv[1][0] * f1 - j_inv[1][1] * f2 - j_inv[1][2] * f3
    newz = z - j_inv[2][0] * f1 - j_inv[2][1] * f2 - j_inv[2][2] * f3
    return newx, newy, newz


def solve_system(eps: float):
    max_iter = 1000
    x = 1.0
    y = 1.0
    z = 1.0
    j_inv = j_inverse(x, y, z)
    newx, newy, newz = new_params(x, y, z, j_inv)
    iterations = 1
    while ((abs((newx - x) / x) > eps or abs((newy - y) / y) > eps or abs((newz - z) / z) > eps)
           and iterations < max_iter):
        x, y, z = newx, newy, newz
        j_inv = j_inverse(x, y, z)
        newx, newy, newz = new_params(x, y, z, j_inv)
        iterations += 1
    print(f"x = {x}, y = {y}, z = {z}")
    print(f"f1 = {f_1(x, y, z)}")
    print(f"f2 = {f_2(x, y, z)}")
    print(f"f3 = {f_3(x, y, z)}")
    print(f"Произведено {iterations} итераций")
    return x, y, z
