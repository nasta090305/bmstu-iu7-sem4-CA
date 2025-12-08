def second_der(a, x, val):
    return 2 * (a[2] - a[3] * x[1] - a[3] * x[2] - a[3] * x[0] + 3 * a[3] * val)


def count_newton(x, y, n, val):
    if n + 1 > len(x):
        return None
    x, y = sort2arrays(x, y)
    close_node = (sorted(range(len(x)), key=lambda i: abs(x[i] - val)))[0]
    if (n + 1) % 2 == 0 and x[close_node] < val:
        close_node += 1
    first_node = close_node - (n + 1) // 2
    if first_node < 0:
        first_node = 0
    last_node = first_node + n + 1
    if last_node > len(x):
        last_node = len(x)
        first_node = last_node - (n + 1)
    coefs = coefs_newton(x[first_node:last_node], y[first_node:last_node])
    return count_polynome(x[first_node:last_node], coefs, val)


def sort2arrays(x, y):
    ids = sorted(range(len(x)), key=lambda i: x[i])
    x = [x[i] for i in ids]
    y = [y[i] for i in ids]
    return x, y


def coefs_newton(x, y):
    coefs = [y[0]]
    n = len(y)
    for i in range(n - 1):
        next_y = [(y[j + 1] - y[j]) / (x[i + j + 1] - x[j]) for j in range(len(y) - 1)]
        #print(y, next_y)
        #print()
        coefs.append(next_y[0])
        y = [i for i in next_y]
    return coefs


def count_polynome(x, coefs, val):
    res = coefs[0]
    cur = 1
    for i in range(len(x) - 1):
        cur *= (val - x[i])
        res += coefs[i + 1] * cur
    return res


def a_coefs(y):
    return y[:-1]


def run_coefs(x, y, h):
    n = len(x) - 1
    e = [0] * n
    m = [0] * n
    for i in range(1, n):
        A = h[i - 1]
        B = (- 2) * (h[i - 1] + h[i])
        D = h[i]
        F = (-3) * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
        #print(A, B, D, F)
        e[i] = D / (B - A * e[i - 1])
        m[i] = (F + A * m[i - 1]) / (B - A * e[i - 1])
    #print("e = ", e)
    #print("m = ", m)
    return e, m


def c_coefs(x, y, h, mode):
    n = len(x) - 1
    c = [0] * (n + 1)
    if mode == 2:
        c[0] = second_der(coefs_newton(x[:4], y[:4]), x[:3], x[0]) / 2
    if mode == 3:
        c[0] = second_der(coefs_newton(x[:4], y[:4]), x[:3], x[0]) / 2
        c[n] = second_der(coefs_newton(x[-4:], y[-4:]), x[-3:], x[-1]) / 2
    e, m = run_coefs(x, y, h)
    for i in range(n - 1, 0, -1):
        c[i] = e[i] * c[i + 1] + m[i]
    return c


def spline_coefs(x, y, mode):
    n = len(x) - 1
    a = a_coefs(y)
    #print("a = ", a)
    h = [x[i + 1] - x[i] for i in range(n)]
    c = c_coefs(x, y, h, mode)
    #print("c = ", c)
    d = [(c[i + 1] - c[i]) / (3 * h[i]) for i in range(n - 1)] + [0]
    d[n - 1] = (-1) * c[n - 1] / (3 * h[n - 1])
    #print("d = ", d)
    b = [(y[i + 1] - y[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3 for i in range(n - 1)] + [0]
    b[n - 1] = (y[n] - y[n - 1]) / h[n - 1] - 2 * h[n - 1] * c[n - 1] / 3
    #print("b = ", b)
    return a, b, c, d


def count_spline(x, y, val, mode):
    x, y = sort2arrays(x, y)
    a, b, c, d = spline_coefs(x, y, mode)
    i = 0
    while val >= x[i + 1]:
        i += 1
    #print(a[i], b[i], c[i], d[i], x[i])
    res = a[i] + b[i] * (val - x[i]) + c[i] * ((val - x[i]) ** 2) + d[i] * ((val - x[i]) ** 3)
    return res