# В исходном текстовом файле(hotline1.txt) найти всеномера телефонов,
# соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
# элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.
import re

def process_hotlines(input_file, output_file):
    """
    Обрабатывает файл с горячими линиями, находит номера телефонов, соответствующих шаблону 8(000)000-00-00,
    подсчитывает их количество и добавляет фразу «Министерства образования Ростовской области» после «Горячая линия».
    Результат сохраняется в новый файл.

    :param input_file: Имя входного файла
    :param output_file: Имя выходного файла
    """
    # Шаблон для поиска номеров телефонов вида 8(000)000-00-00
    phone_pattern = re.compile(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}')

    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        phone_count = 0

        for line in lines:
            # Поиск номеров телефонов в строке
            phones = phone_pattern.findall(line)
            phone_count += len(phones)

            # Добавление фразы после «Горячая линия»
            modified_line = line.replace('«Горячая линия»',
                                         '«Горячая линия» Министерства образования Ростовской области')
            outfile.write(modified_line)

    print(f"Найдено номеров телефонов, соответствующих шаблону: {phone_count}")


# Пример использования
input_filename = 'hotline1.txt'
output_filename = 'hotline1_processed.txt'
process_hotlines(input_filename, output_filename)