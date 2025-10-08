# Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
# шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
# "кличка" и "порода".

class Animal:
    """
    Базовый класс, описывающий животное.

    Атрибуты:
        species (str): Вид животного (например, "собака", "кошка").
        legs (int): Количество лап у животного.
        fur_color (str): Цвет шерсти животного.
    """

    def __init__(self, species: str, legs: int, fur_color: str) -> None:
        """
        Инициализация объекта класса Animal.

        Параметры:
            species (str): Вид животного.
            legs (int): Количество лап.
            fur_color (str): Цвет шерсти.
        """
        self.species = species
        self.legs = legs
        self.fur_color = fur_color

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.

        Возвращает:
            str: Информация о животном.
        """
        return (f"Вид: {self.species}, "
                f"Количество лап: {self.legs}, "
                f"Цвет шерсти: {self.fur_color}")


class Dog(Animal):
    """
    Класс, описывающий собаку. Наследуется от класса Animal.

    Дополнительные атрибуты:
        name (str): Кличка собаки.
        breed (str): Порода собаки.
    """

    def __init__(self, species: str, legs: int, fur_color: str,
                 name: str, breed: str) -> None:
        """
        Инициализация объекта класса Dog.

        Параметры:
            species (str): Вид животного.
            legs (int): Количество лап.
            fur_color (str): Цвет шерсти.
            name (str): Кличка собаки.
            breed (str): Порода собаки.
        """
        super().__init__(species, legs, fur_color)
        self.name = name
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки.

        Возвращает:
            str: Информация о собаке.
        """
        return (f"{super().__str__()}, "
                f"Кличка: {self.name}, "
                f"Порода: {self.breed}")


# Пример использования классов
if __name__ == "__main__":
    # Создаем экземпляр базового класса Animal
    animal = Animal("кошка", 4, "рыжий")
    print(animal)

    # Создаем экземпляр производного класса Dog
    dog = Dog("собака", 4, "черный", "Бобик", "овчарка")
    print(dog)