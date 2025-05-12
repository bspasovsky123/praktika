# main.py
# Консольный интерфейс управления системой StroBuh

from modules import database

def show_menu():
    print("\n--- Система учёта строительной компании 'Инженер' ---")
    print("1. Инициализировать базу данных")
    print("2. Добавить клиента")
    print("3. Добавить договор")
    print("4. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            database.init_db()
        elif choice == "2":
            name = input("Введите название клиента: ")
            inn = input("Введите ИНН клиента: ")
            address = input("Введите адрес клиента: ")
            database.insert_client(name, inn, address)
        elif choice == "3":
            number = input("Введите номер договора: ")
            client_inn = input("Введите ИНН клиента: ")
            amount = float(input("Введите сумму договора: "))
            database.insert_contract(number, client_inn, amount)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Повторите попытку.")

if __name__ == "__main__":
    main()
