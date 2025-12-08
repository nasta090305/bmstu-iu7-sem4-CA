EPS = 1e-8


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


def sort2arrays(x, y):
    ids = sorted(range(len(x)), key=lambda i: x[i])
    x = [x[i] for i in ids]
    y = [y[i] for i in ids]
    return x, y


def sort4arrays(x, y, y1, y2):
    ids = sorted(range(len(x)), key=lambda i: x[i])
    x = [x[i] for i in ids]
    y = [y[i] for i in ids]
    y1 = [y1[i] for i in ids]
    y2 = [y2[i] for i in ids]
    return x, y, y1, y2


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
    #print("newton", x[first_node:last_node], y[first_node:last_node])
    coefs = coefs_newton(x[first_node:last_node], y[first_node:last_node])
    return count_polynome(x[first_node:last_node], coefs, val)


def count_ermit(all_x, all_y, all_y1, all_y2, n, val):
    if n + 1 > len(all_x) * 3:
        return None
    count = (n + 3) // 3
    all_x, all_y, all_y1, all_y2 = sort4arrays(all_x, all_y, all_y1, all_y2)
    close_node = (sorted(range(len(all_x)), key=lambda i: abs(all_x[i] - val)))[0]
    #print("count = ", count, "close_node = ", close_node)
    if count % 2 == 0 and all_x[close_node] < val:
        close_node += 1
    first_node = close_node - count // 2
    if first_node < 0:
        first_node = 0
    last_node = first_node + count
    if last_node > len(all_x):
        last_node = len(all_x)
        first_node = last_node - count
    x = list()
    y = list()
    y1 = list()
    y2 = list()
    if n < 2:
        for k in range(n + 1):
            x.append(all_x[first_node])
            y.append(all_y[first_node])
            y1.append(all_y1[first_node])
            y2.append(all_y2[first_node])
    else:
        for i in range((n + 1) // 3 - 1):
            for j in range(3):
                x.append(all_x[first_node + i])
                y.append(all_y[first_node + i])
                y1.append(all_y1[first_node + i])
                y2.append(all_y2[first_node + i])
        if (n + 1) % 3 == 0:
            for j in range(3):
                x.append(all_x[first_node + (n + 1) // 3 - 1])
                y.append(all_y[first_node + (n + 1) // 3 - 1])
                y1.append(all_y1[first_node + (n + 1) // 3 - 1])
                y2.append(all_y2[first_node + (n + 1) // 3 - 1])
        if (n + 1) % 3 == 1:
            for i in range(2):
                for j in range(2):
                    x.append(all_x[first_node + (n + 1) // 3 - 1 + i])
                    y.append(all_y[first_node + (n + 1) // 3 - 1 + i])
                    y1.append(all_y1[first_node + (n + 1) // 3 - 1 + i])
                    y2.append(all_y2[first_node + (n + 1) // 3 - 1 + i])
        if (n + 1) % 3 == 2:
            for j in range(3):
                x.append(all_x[first_node + (n + 1) // 3 - 1])
                y.append(all_y[first_node + (n + 1) // 3 - 1])
                y1.append(all_y1[first_node + (n + 1) // 3 - 1])
                y2.append(all_y2[first_node + (n + 1) // 3 - 1])
            for j in range(2):
                x.append(all_x[first_node + n // 3])
                y.append(all_y[first_node + n // 3])
                y1.append(all_y1[first_node + n // 3])
                y2.append(all_y2[first_node + n // 3])
    coefs = coefs_ermit(x, y, y1, y2)
    return count_polynome(x, coefs, val)


def coefs_ermit(x, y, y1, y2):
    coefs = [y[0]]
    n = len(x)
    next_y = list()
    if len(y) > 1:
        for i in range(len(x) - 1):
            if abs(x[i] - x[i + 1]) < EPS:
                next_y.append(y1[i])
            else:
                next_y.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
        y = [i for i in next_y]
        next_y.clear()
        coefs.append(y[0])
    if len(y) > 1:
        for i in range(len(x) - 2):
            if abs(x[i] - x[i + 2]) < EPS:
                next_y.append(y2[i] / 2)
            else:
                next_y.append((y[i + 1] - y[i]) / (x[i + 2] - x[i]))
        y = [i for i in next_y]
        coefs.append(y[0])
    if len(y) > 1:
        for i in range(2, n - 1):
            next_y = [(y[j + 1] - y[j]) / (x[i + j + 1] - x[j]) for j in range(len(y) - 1)]
            coefs.append(next_y[0])
            y = [k for k in next_y]
    return coefs


def reverse_newton(x, y, n, val):
    x, y = sort2arrays(x, y)
    for i in range(len(y) - 1):
        if (y[i] < val and y[i + 1] > val) or (y[i] > val and y[i + 1] < val):
            y_near_root, x_near_root = [], []
            y_near_root.append(y[i])
            x_near_root.append(x[i])
            step = abs(x[i] - x[i + 1]) / n
            next_x = min(x[i], x[i + 1]) + step
            for j in range(n - 1):
                x_near_root.append(next_x)
                y_near_root.append(count_newton(x, y, n, next_x))
                next_x += step
            y_near_root.append(y[i + 1])
            x_near_root.append(x[i + 1])
            return count_newton(y_near_root, x_near_root, n, 0)
    return None


def reverse_ermit(x, y, y1, y2, val):
    x, y, y1, y2 = sort4arrays(x, y, y1, y2)
    x1 = [1 / i for i in y1]
    x2 = [((-1) * y2[i]) / (y1[i] ** 3) for i in range(len(y1))]
    for i in range(len(y) - 1):
        if (y[i] < val and y[i + 1] > val) or (y[i] > val and y[i + 1] < val):
            y_near_root = [y[i], y[i + 1]]
            x_near_root = [x[i], x[i + 1]]
            x1_near_root = [x1[i], x1[i + 1]]
            x2_near_root = [x2[i], x2[i + 1]]
            return count_ermit(y_near_root, x_near_root, x1_near_root, x2_near_root, 5, val)
    return None


def root_of_system(x1, y1, x2, y2):
    dif_x = x2
    dif_y = [count_newton(x1, y1, 5, dif_x[i]) - y2[i] for i in range(len(dif_x))]
    return reverse_newton(dif_x, dif_y, 4, 0)