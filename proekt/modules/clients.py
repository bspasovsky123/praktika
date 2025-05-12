# modules/clients.py
# Модуль клиента: хранит информацию о контрагентах компании

class Client:
    def __init__(self, name: str, inn: str, address: str):
        self.name = name
        self.inn = inn
        self.address = address

    def __repr__(self):
        return f"Клиент: {self.name}, ИНН: {self.inn}, Адрес: {self.address}"

    def to_dict(self):
        return {
            "name": self.name,
            "inn": self.inn,
            "address": self.address
        }

    def validate_inn(self):
        return self.inn.isdigit() and (len(self.inn) == 10 or len(self.inn) == 12)
