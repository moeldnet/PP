import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Создает соединение с базой данных SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключено к базе данных SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    """Создает таблицу услуг, если она не существует"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            master_name TEXT NOT NULL,
            client_name TEXT NOT NULL,
            cleaning_type TEXT NOT NULL,
            price REAL NOT NULL,
            discount REAL DEFAULT 0
        );
        """)
        print("Таблица услуг создана или уже существует")
    except Error as e:
        print(e)


def insert_initial_data(conn):
    """Вставляет начальные данные в таблицу (10 записей)"""
    services = [
        ("Иванов Иван Иванович", "Петров Петр Петрович", "Химчистка дивана", 3500, 0),
        ("Сидорова Анна Владимировна", "Кузнецова Елена Сергеевна", "Чистка ковра", 2500, 5),
        ("Петрова Ольга Дмитриевна", "Васильев Михаил Игоревич", "Чистка штор", 1800, 10),
        ("Иванов Иван Иванович", "Смирнов Алексей Викторович", "Химчистка матраса", 4200, 0),
        ("Козлов Дмитрий Анатольевич", "Федорова Наталья Олеговна", "Чистка пуховика", 2900, 15),
        ("Сидорова Анна Владимировна", "Николаева Ирина Петровна", "Химчистка кресла", 3100, 5),
        ("Петрова Ольга Дмитриевна", "Алексеев Денис Сергеевич", "Чистка пальто", 2300, 0),
        ("Козлов Дмитрий Анатольевич", "Борисова Марина Андреевна", "Химчистка автомобильных сидений", 3800, 10),
        ("Иванов Иван Иванович", "Тимофеев Артем Валерьевич", "Чистка дубленки", 4500, 5),
        ("Сидорова Анна Владимировна", "Григорьева Светлана Ивановна", "Химчистка покрывала", 2100, 0)
    ]

    try:
        cursor = conn.cursor()
        cursor.executemany("""
        INSERT INTO services (master_name, client_name, cleaning_type, price, discount)
        VALUES (?, ?, ?, ?, ?)
        """, services)
        conn.commit()
        print("Добавлено 10 начальных записей")
    except Error as e:
        print(e)


def add_service(conn):
    """Добавляет новую услугу в базу данных"""
    print("\nДобавление новой услуги:")
    master = input("ФИО мастера: ")
    client = input("ФИО клиента: ")
    cleaning_type = input("Тип чистки: ")

    try:
        price = float(input("Стоимость: "))
        discount = float(input("Скидка (%): "))

        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO services (master_name, client_name, cleaning_type, price, discount)
        VALUES (?, ?, ?, ?, ?)
        """, (master, client, cleaning_type, price, discount))
        conn.commit()
        print("Услуга успешно добавлена!")
    except ValueError:
        print("Ошибка: стоимость и скидка должны быть числами")
    except Error as e:
        print(f"Ошибка базы данных: {e}")


def find_services(conn):
    """Поиск услуг по различным критериям"""
    print("\nВарианты поиска:")
    print("1. По ФИО мастера")
    print("2. По ФИО клиента")
    print("3. По типу чистки")
    print("4. По стоимости (до указанной суммы)")
    print("5. По наличию скидки")

    try:
        choice = int(input("Выберите вариант поиска (1-5): "))

        cursor = conn.cursor()

        if choice == 1:
            master = input("Введите ФИО мастера: ")
            cursor.execute("SELECT * FROM services WHERE master_name LIKE ?", (f"%{master}%",))
        elif choice == 2:
            client = input("Введите ФИО клиента: ")
            cursor.execute("SELECT * FROM services WHERE client_name LIKE ?", (f"%{client}%",))
        elif choice == 3:
            cleaning_type = input("Введите тип чистки: ")
            cursor.execute("SELECT * FROM services WHERE cleaning_type LIKE ?", (f"%{cleaning_type}%",))
        elif choice == 4:
            max_price = float(input("Введите максимальную стоимость: "))
            cursor.execute("SELECT * FROM services WHERE price <= ?", (max_price,))
        elif choice == 5:
            cursor.execute("SELECT * FROM services WHERE discount > 0")
        else:
            print("Неверный выбор")
            return

        services = cursor.fetchall()

        if not services:
            print("Услуги не найдены")
        else:
            print("\nНайденные услуги:")
            print("-" * 90)
            print(
                "ID  | Мастер                | Клиент                 | Тип чистки                     | Стоимость | Скидка")
            print("-" * 90)
            for service in services:
                print(
                    f"{service[0]:<3} | {service[1]:<20} | {service[2]:<20} | {service[3]:<30} | {service[4]:<8} | {service[5]}%")
            print("-" * 90)

    except ValueError:
        print("Ошибка: введите число от 1 до 5")
    except Error as e:
        print(f"Ошибка базы данных: {e}")


def delete_service(conn):
    """Удаление услуг по различным критериям"""
    print("\nВарианты удаления:")
    print("1. По ID услуги")
    print("2. По ФИО клиента")
    print("3. По типу чистки")

    try:
        choice = int(input("Выберите вариант удаления (1-3): "))

        cursor = conn.cursor()

        if choice == 1:
            service_id = int(input("Введите ID услуги для удаления: "))
            cursor.execute("DELETE FROM services WHERE id = ?", (service_id,))
        elif choice == 2:
            client = input("Введите ФИО клиента: ")
            cursor.execute("DELETE FROM services WHERE client_name LIKE ?", (f"%{client}%",))
        elif choice == 3:
            cleaning_type = input("Введите тип чистки: ")
            cursor.execute("DELETE FROM services WHERE cleaning_type LIKE ?", (f"%{cleaning_type}%",))
        else:
            print("Неверный выбор")
            return

        conn.commit()
        print(f"Удалено {cursor.rowcount} записей")

    except ValueError:
        print("Ошибка: введите корректное число или ID")
    except Error as e:
        print(f"Ошибка базы данных: {e}")


def update_service(conn):
    """Редактирование услуг"""
    print("\nРедактирование услуги")

    try:
        service_id = int(input("Введите ID услуги для редактирования: "))

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM services WHERE id = ?", (service_id,))
        service = cursor.fetchone()

        if not service:
            print("Услуга с таким ID не найдена")
            return

        print("\nТекущие данные услуги:")
        print(f"1. ФИО мастера: {service[1]}")
        print(f"2. ФИО клиента: {service[2]}")
        print(f"3. Тип чистки: {service[3]}")
        print(f"4. Стоимость: {service[4]}")
        print(f"5. Скидка: {service[5]}%")

        field = int(input("\nВыберите поле для редактирования (1-5): "))

        if field == 1:
            new_value = input("Введите новое ФИО мастера: ")
            cursor.execute("UPDATE services SET master_name = ? WHERE id = ?", (new_value, service_id))
        elif field == 2:
            new_value = input("Введите новое ФИО клиента: ")
            cursor.execute("UPDATE services SET client_name = ? WHERE id = ?", (new_value, service_id))
        elif field == 3:
            new_value = input("Введите новый тип чистки: ")
            cursor.execute("UPDATE services SET cleaning_type = ? WHERE id = ?", (new_value, service_id))
        elif field == 4:
            new_value = float(input("Введите новую стоимость: "))
            cursor.execute("UPDATE services SET price = ? WHERE id = ?", (new_value, service_id))
        elif field == 5:
            new_value = float(input("Введите новую скидку (%): "))
            cursor.execute("UPDATE services SET discount = ? WHERE id = ?", (new_value, service_id))
        else:
            print("Неверный выбор поля")
            return

        conn.commit()
        print("Данные успешно обновлены!")

    except ValueError:
        print("Ошибка: введите корректное число или значение")
    except Error as e:
        print(f"Ошибка базы данных: {e}")


def show_all_services(conn):
    """Отображает все услуги в базе данных"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM services")
        services = cursor.fetchall()

        if not services:
            print("В базе данных нет услуг")
        else:
            print("\nВсе услуги:")
            print("-" * 90)
            print(
                "ID  | Мастер                | Клиент                 | Тип чистки                     | Стоимость | Скидка")
            print("-" * 90)
            for service in services:
                print(
                    f"{service[0]:<3} | {service[1]:<20} | {service[2]:<20} | {service[3]:<30} | {service[4]:<8} | {service[5]}%")
            print("-" * 90)

    except Error as e:
        print(f"Ошибка базы данных: {e}")


def main_menu():
    """Отображает главное меню и обрабатывает выбор пользователя"""
    print("\nХимчистка - система управления услугами")
    print("1. Показать все услуги")
    print("2. Добавить новую услугу")
    print("3. Найти услуги")
    print("4. Удалить услуги")
    print("5. Редактировать услугу")
    print("0. Выход")

    try:
        return int(input("Выберите действие: "))
    except ValueError:
        print("Ошибка: введите число от 0 до 5")
        return -1


def main():
    """Основная функция программы"""
    database = "dry_cleaning.db"

    # Создаем соединение с базой данных
    conn = create_connection(database)
    if conn is None:
        return

    # Создаем таблицу и добавляем начальные данные
    create_table(conn)

    # Проверяем, есть ли данные в таблице
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM services")
    count = cursor.fetchone()[0]

    if count == 0:
        insert_initial_data(conn)

    # Основной цикл программы
    while True:
        choice = main_menu()

        if choice == 1:
            show_all_services(conn)
        elif choice == 2:
            add_service(conn)
        elif choice == 3:
            find_services(conn)
        elif choice == 4:
            delete_service(conn)
        elif choice == 5:
            update_service(conn)
        elif choice == 0:
            print("Выход из программы")
            break
        elif choice != -1:
            print("Неверный выбор. Попробуйте снова.")

    # Закрываем соединение с базой данных
    conn.close()


if __name__ == "__main__":
    main()