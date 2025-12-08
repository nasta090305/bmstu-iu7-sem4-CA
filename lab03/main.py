from funcs import count_spline, count_newton


def newton_3d_interpolation(nodes, x0, y0, z0, nx, ny, nz):
    all_x = [i for i in range(len(nodes[0][0]))]
    all_y = [i for i in range(len(nodes[0]))]
    all_z = [i for i in range(len(nodes))]

    func_values = []
    for z in all_z:
        tmp = []
        for y in all_y:
            tmp.append(count_newton(all_x, nodes[z][y], nx, x0))
        func_values.append(count_newton(all_y, tmp, ny, y0))
    return count_newton(all_z, func_values, nz, z0)


def spline_3d_interpolation(nodes, x0, y0, z0):
    all_x = [i for i in range(len(nodes[0][0]))]
    all_y = [i for i in range(len(nodes[0]))]
    all_z = [i for i in range(len(nodes))]

    func_values = []
    for z in all_z:
        tmp = []
        for y in all_y:
            tmp.append(count_spline(all_x, nodes[z][y], x0, 3))
        func_values.append(count_spline(all_y, tmp, y0, 3))
    return count_spline(all_z, func_values, z0, 3)


def mixed_3d_interpolation(nodes, x0, y0, z0):
    all_x = [i for i in range(len(nodes[0][0]))]
    all_y = [i for i in range(len(nodes[0]))]
    all_z = [i for i in range(len(nodes))]
    nx, ny, nz = 3, 3, 3
    func_values = []
    for z in all_z:
        tmp = []
        for y in all_y:
            tmp.append(count_spline(all_x, nodes[z][y], x0, 3))
        func_values.append(count_newton(all_y, tmp, ny, y0))
    return count_spline(all_z, func_values, z0, 3)


def read_table(filename):
    nodes = []
    with open(filename, "r") as f:
        line = f.readline()
        i = -1
        flag = True
        while line != '':
            if line[0].isnumeric():
                cur = list(map(int, line.split()))
                nodes[i].append(cur[1:])
            elif flag:
                nodes.append([])
                i += 1
                flag = False
            else:
                flag = True
            line = f.readline()
    return nodes


nodes = read_table("table.txt")
x, y, z = map(float, input("Enter (x, y, z): ").split())
nx, ny, nz = 3, 3, 3
res_n = newton_3d_interpolation(nodes, x, y, z, nx, ny, nz)
res_s = spline_3d_interpolation(nodes, x, y, z)
res_m = mixed_3d_interpolation(nodes, x, y, z)
print("Newton interpolation:", res_n)
print("Spline interpolation:", res_s)
print("Mixed interpolation:", res_m)