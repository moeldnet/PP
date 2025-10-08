# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.
# ПЗ №9 Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее
# значение роста (в см.). (Пример, {"Андрей": 178, "Виктор": 150, "Максим": 200, …},
# наибольшее 200, наименьшее 150)


import tkinter as tk
from tkinter import messagebox


def find_min_max_heights():
    """Функция для нахождения и вывода минимального и максимального роста."""
    # Данные: словарь с именами и ростом в см
    height_data = {
        "Андрей": 178,
        "Виктор": 150,
        "Максим": 200,
        "Алексей": 165,
        "Дмитрий": 190,
        "Сергей": 175,
    }

    if not height_data:
        messagebox.showerror("Ошибка", "Словарь пуст!")
        return

    # Находим минимальный и максимальный рост
    min_height = min(height_data.values())
    max_height = max(height_data.values())

    # Формируем сообщение с результатами
    result_message = (
        f"Данные о росте:\n\n"
        f"Словарь: {height_data}\n\n"
        f"Наименьший рост: {min_height} см\n"
        f"Наибольший рост: {max_height} см"
    )

    # Выводим результат в окне сообщения
    messagebox.showinfo("Результат", result_message)


def main():
    """Основная функция для создания графического интерфейса."""
    # Создаем главное окно
    root = tk.Tk()
    root.title("Анализ роста")
    root.geometry("300x150")

    # Добавляем метку с инструкцией
    label = tk.Label(
        root,
        text="Нажмите кнопку, чтобы найти\nнаибольший и наименьший рост",
        font=("Arial", 12),
    )
    label.pack(pady=10)

    # Добавляем кнопку для запуска анализа
    button = tk.Button(
        root,
        text="Найти min и max рост",
        command=find_min_max_heights,
        font=("Arial", 12),
        bg="lightblue",
    )
    button.pack(pady=10)

    # Запускаем главный цикл
    root.mainloop()


# Запускаем программу
main()