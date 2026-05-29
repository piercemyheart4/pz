# 9. Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение" и
# "деление". Каждый метод должен принимать два аргумента и возвращать результат
# операции.

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b


calc = Calculator()

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    print("\nДоступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    
    choice = input("Выберите номер операции (1-4): ")
    print("---")
    
    if choice == '1':
        print("Результат сложения:", calc.add(num1, num2))
    elif choice == '2':
        print("Результат вычитания:", calc.subtract(num1, num2))
    elif choice == '3':
        print("Результат умножения:", calc.multiply(num1, num2))
    elif choice == '4':
        print("Результат деления:", calc.divide(num1, num2))
    else:
        print("Неверный выбор операции.")

except ValueError:
    print("Ошибка: введены некорректные данные. Пожалуйста, вводите числа.")