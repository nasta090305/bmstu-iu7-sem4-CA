from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

xa = 0.0
xb = 1.0
ya = 1.0
yb = 3.0

N = 100
h = 1 / N
tol = 1e-6
max_iter = 1000


def F(y):
    f = np.zeros(N + 1)
    f[0] = y[0] - ya
    f[N] = y[N] - yb
    for i in range(1, N):
        f[i] = ((y[i - 1] - 2 * y[i] + y[i + 1]) / (h ** 2) - y[i] ** 3 - (i * h) ** 2)  # Аппроксимируем вторую производную разностным аналогом
    return f


def J(y):
    jac = np.zeros((N + 1, N + 1))

    jac[0, 0] = 1.0
    jac[N][N] = 1.0

    for i in range(1, N):
        jac[i][i - 1] = 1.0 / (h ** 2)
        jac[i][i] = -2.0 / (h ** 2) - 3.0 * y[i] ** 2
        jac[i][i + 1] = 1.0 / (h ** 2)

    return jac


def gauss(A, B):
    n = len(B)
    for i in range(n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k
        for k in range(i, n):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
        tmp = B[maxRow]
        B[maxRow] = B[i]
        B[i] = tmp
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            B[k] += c * B[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x


def newton(x_init):
    jac = J(x_init)
    func_y = F(x_init)
    dx = gauss(jac, -func_y)
    return x_init + dx


def iter_newton(x_init):
    iter = 0

    x_old = x_init
    x_new = newton(x_old)

    diff = np.linalg.norm(x_old - x_new)

    while diff > tol and iter < max_iter:
        iter += 1
        x_new = newton(x_old)
        diff = np.linalg.norm(x_old - x_new)
        x_old = x_new

    convergent_val = x_new
    return convergent_val


def solve():
    x = np.linspace(xa, xb, N + 1)
    y = np.linspace(ya, yb, N + 1)

    y = iter_newton(y)

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()