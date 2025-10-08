# # Составить генератор (yield), который преобразует все буквенные символы в строчные.
def lowercase_generator(string):
    """Генератор, преобразующий все буквенные символы в строчные."""
    for char in string:
        yield char.lower() if char.isalpha() else char

# Использование генератора
input_string = input("Введите строку:")
lowercased_chars = lowercase_generator(input_string)

# Преобразуем генератор в список для отображения результата
result = ''.join(lowercased_chars)
print(result)  # вывод: "hello world! 123"

