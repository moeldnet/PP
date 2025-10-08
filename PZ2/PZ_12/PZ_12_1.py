# Организовать и вывести последовательность на N произвольных целых
# элементов, сформировать новую последовательность куда поместить положительные
# четные элементы, найти их сумму и среднее арифметическое.

import random
from functools import reduce

# Количество элементов в последовательности
n = 10

# Генерация случайной последовательности из n целых чисел от -50 до 50
sequence = [random.randint(-50, 50) for _ in range(n)]

# Отфильтровываем положительные чётные числа
positive_even_elem = [num for num in sequence if num > 0 and num % 2 == 0]

print(f"Исходная последовательность: {sequence}")
print(f"Положительные чётные числа: {positive_even_elem}")

if positive_even_elem:
    # Используем reduce для одновременного подсчёта суммы и количества
    total_sum, count = reduce(
        lambda acc, val: (acc[0] + val, acc[1] + 1),
        positive_even_elem,
        (0, 0)
    )

    average = total_sum / count
    print(f"Сумма положительных чётных чисел: {total_sum}")
    print(f"Среднее арифметическое: {average:.2f}")
else:
    print("Нет положительных чётных чисел для вычисления.")