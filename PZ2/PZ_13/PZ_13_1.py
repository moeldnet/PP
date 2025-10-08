# В двумерном списке элементы последнего столбца заменить на -1.

import random

while True:
    try:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        if rows <= 0 or cols <= 0:
            print("Размер должен быть положительным.")
            continue
        break
    except ValueError:
        print("Некорректный ввод. Введите целое число.")

# Генерация случайной матрицы
matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Замена последнего столбца на -1
matrix = [row[:-1] + [-1] for row in matrix]

print("\nМатрица после замены последнего столбца на -1:")
for row in matrix:
    print(row)