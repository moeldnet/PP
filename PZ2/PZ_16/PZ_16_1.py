# Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
# методы для определения дня недели, проверки на високосный год и определения
# количества дней в месяце

import datetime


class Calendar:
    """
    Класс для работы с датами (год, месяц, день).
    Предоставляет методы для определения дня недели, проверки на високосный год
    и определения количества дней в месяце.
    """

    def __init__(self, year: int, month: int, day: int):
        """
        Инициализация объекта Календарь.

        Параметры:
            year (int): год (например, 2023)
            month (int): месяц (1-12)
            day (int): день (1-31 в зависимости от месяца)
        """
        self.year = year
        self.month = month
        self.day = day

        # Проверка валидности даты
        try:
            self.date = datetime.date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Некорректная дата: {e}")

    def get_weekday(self) -> str:
        """
        Возвращает день недели для текущей даты.

        Возвращает:
            str: Название дня недели (понедельник, вторник и т.д.)
        """
        weekdays = [
            "понедельник", "вторник", "среда",
            "четверг", "пятница", "суббота", "воскресенье"
        ]
        return weekdays[self.date.weekday()]

    def is_leap_year(self) -> bool:
        """
        Проверяет, является ли год високосным.

        Возвращает:
            bool: True если год високосный, иначе False
        """
        return (self.year % 400 == 0) or (self.year % 100 != 0 and self.year % 4 == 0)

    def days_in_month(self) -> int:
        """
        Возвращает количество дней в текущем месяце.

        Возвращает:
            int: Количество дней в месяце (28-31)
        """
        if self.month == 2:
            return 29 if self.is_leap_year() else 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31


# Пример использования класса
if __name__ == "__main__":
    try:
        # Создаем объект календаря
        cal = Calendar(2023, 11, 15)

        # Получаем день недели
        print(f"15 ноября 2023 года - это {cal.get_weekday()}")

        # Проверяем високосный год
        leap_status = "високосный" if cal.is_leap_year() else "не високосный"
        print(f"2023 год - {leap_status}")

        # Получаем количество дней в ноябре
        print(f"В ноябре 2023 года {cal.days_in_month()} дней")

        # Дополнительный пример с високосным годом
        cal_leap = Calendar(2024, 2, 1)
        print(f"\n2024 год - {'високосный' if cal_leap.is_leap_year() else 'не високосный'}")
        print(f"В феврале 2024 года {cal_leap.days_in_month()} дней")

    except ValueError as e:
        print(f"Ошибка: {e}")
