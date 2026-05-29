# Средствами языка Python сформировать текстовый файл (.txt),
# содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Количество элементов, индекс последнего максимального элемента,
# меняем местами первую и последнюю трети.

import random

input_file = "numbers.txt"
output_file = "numbers_result.txt"

numbers = [random.randint(-50, 50) for _ in range(12)]

with open(input_file, "w") as f:
    f.write(" ".join(map(str, numbers)))

with open(input_file, "r") as f:
    data = list(map(int, f.read().split()))

count = len(data)

last_max_index = max(range(count), key=lambda i: (data[i], i))

third = count // 3
first_third = data[:third]
last_third = data[count - third:]
middle = data[third:count - third]

new_data = last_third + middle + first_third

with open(output_file, "w") as f:
    f.write(f"Исходные данные: {data}\n")
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Индекс последнего максимального элемента: {last_max_index}\n")
    f.write(f"Меняем местами первую и последнюю трети: {new_data}\n")

print(f"Исходные данные: {data}")
print(f"Количество элементов: {count}")
print(f"Индекс последнего максимального элемента: {last_max_index}")
print(f"Меняем местами первую и последнюю трети: {new_data}")