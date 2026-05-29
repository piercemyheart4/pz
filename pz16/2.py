# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы".

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} выполняет базовые обязанности."

    def get_salary(self):
        return f"{self.name} получил зарплату в размере {self.salary} руб."


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self):
        return f"{self.name} управляет командой из {self.team_size} человек."


class Engineer(Employee):

    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.specialization = specialization

    def design_systems(self):
        return f"{self.name} проектирует системы в области {self.specialization}."


manager = Manager("Алексей", 120000, 8)
engineer = Engineer("Дмитрий", 95000, "программное обеспечение")

print("Тестирование класса Менеджер:")
print(manager.work())
print(manager.get_salary())
print(manager.manage_team())
print("---")

print("Тестирование класса Инженер:")
print(engineer.work())
print(engineer.get_salary())
print(engineer.design_systems())