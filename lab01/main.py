from funcs import count_newton, count_ermit, reverse_newton, reverse_ermit, root_of_system

with open("table.txt", "r") as f:
    nums = [list(map(float, i.split())) for i in f]
    x, y, y1, y2 = [], [], [], []
    for i in nums:
        x += [i[0]]
        y += [i[1]]
        y1 += [i[2]]
        y2 += [i[3]]

try:
    val = float(input("Введите значение, для которого необходимо произвести интерполяцию:\n"))
except Exception:
    print("Некорректные входные данные")
    exit()

print("-----------------------------------")
print("|  n  |   newton    |    ermit    |")
print("-----------------------------------")
for n in range(1, 6):
    if count_newton(x, y, n, val) is None:
        print("|  -  |      -      |      --     |")
    else:
        print(f"|  {n}  |  {count_newton(x, y, n, val):+8.6f}  |  {count_ermit(x, y, y1, y2, n, val):+8.6f}  |")
    print("-----------------------------------")
print("Корень по Ньютону:", reverse_newton(x, y, 4, 0))
print("Корень по Эрмиту:", reverse_ermit(x, y, y1, y2, 0))

with open("table1.txt") as f1:
    nums = [list(map(float, i.split())) for i in f1]
    x1, y1 = [], []
    for i in nums:
        y1 += [i[0]]
        x1 += [i[1]]
with open("table2.txt") as f2:
    nums = [list(map(float, i.split())) for i in f2]
    x2, y2 = [], []
    for i in nums:
        x2 += [i[0]]
        y2 += [i[1]]

print("Корень системы:", root_of_system(x1, y1, x2, y2))