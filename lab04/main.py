from funcs import *

print("Выберите номер задания:\n1. Одномерная аппроксимация\n2. Двумерная аппроксимация\n3. Диффур")
try:
    n = int(input())
    if n == 1:
        one_dim_apprx("one_dim.txt", 3)
    elif n == 2:
        two_dim_apprx("two_dim.txt", 3)
    else:
        solve_equation(50)
except Exception:
    print("Ошибка ввода")

