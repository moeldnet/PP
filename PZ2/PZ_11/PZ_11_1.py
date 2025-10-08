# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Количество элементов, общих для двух файлов:
# Количество четных элементов первого файла:
# Количество нечетных элементов второго файла:

import random

# Функция для создания текстового файла с последовательностью чисел
def create_file(filename, count, positive=True):
    with open(filename, 'w') as f:
        if positive:
            numbers = [random.randint(1, 100) for _ in range(count)]  # Положительные числа
        else:
            numbers = [random.randint(-100, -1) for _ in range(count)]  # Отрицательные числа
        f.write(' '.join(map(str, numbers)))

# Создаем два файла: один с положительными, другой с отрицательными числами
create_file('positive_numbers.txt', 10, positive=True)
create_file('negative_numbers.txt', 10, positive=False)

# Функция для обработки файлов и записи результатов в новый файл
def process_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Читаем числа из файлов
        numbers1 = list(map(int, f1.read().strip().split()))
        numbers2 = list(map(int, f2.read().strip().split()))

    # Обработка данных
    common_elements = set(numbers1) & set(numbers2)
    even_count_file1 = sum(1 for num in numbers1 if num % 2 == 0)
    odd_count_file2 = sum(1 for num in numbers2 if num % 2 != 0)

    # Запись результатов в новый файл
    with open(output_file, 'w') as out:
        out.write(f"Элементы первого файла: {numbers1}\n")
        out.write(f"Элементы второго файла: {numbers2}\n")
        out.write(f"Количество элементов первого файла: {len(numbers1)}\n")
        out.write(f"Количество элементов второго файла: {len(numbers2)}\n")
        out.write(f"Количество элементов, общих для двух файлов: {len(common_elements)}\n")
        out.write(f"Количество четных элементов первого файла: {even_count_file1}\n")
        out.write(f"Количество нечетных элементов второго файла: {odd_count_file2}\n")

# Обрабатываем файлы и создаем выходной файл
process_files('positive_numbers.txt', 'negative_numbers.txt', 'output.txt')

print("Обработка завершена. Результаты записаны в 'output.txt'.")

