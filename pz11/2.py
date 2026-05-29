
# Из заданной строки отобразить только символы нижнего регистра. Использовать
# библиотеку string. Строка 'In PyCharm, you can specify third-party standalone applications and
# run them as External Tools'.

import string

input_string = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

lowercase_letters = string.ascii_lowercase
filtered_chars = [char for char in input_string if char in lowercase_letters]
result_string = "".join(filtered_chars)

print("Исходная строка:", input_string)
print("---")
print("Символы нижнего регистра:", result_string)