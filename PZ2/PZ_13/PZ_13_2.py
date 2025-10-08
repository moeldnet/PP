# В двумерном списке элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности

import random

while True:
    try:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        if rows < 3 or cols <= 0:
            print("Для выполнения задачи необходимо минимум 3 строки.")
            continue
        break
    except ValueError:
        print("Некорректный ввод. Введите целое число.")

# Генерация случайной матрицы
matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Создание одномерного динамического массива той же длины, что и третья строка
dynamic_array = [x * 5 for x in range(cols)]  # Пример: [0, 5, 10, ...]

# Замена третьей строки (индекс 2) на dynamic_array
if len(matrix[2]) == len(dynamic_array):
    matrix[2] = dynamic_array
else:
    print("Ошибка: размер массива не совпадает с длиной строки.")

print("\nОдномерный массив:", dynamic_array)
print("\nМатрица после замены третьей строки:")
for row in matrix:
    print(row)