# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.

import re

with open("Dostoevsky.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Содержимое файла прочитано успешно.")
print("---")

pattern = r"\bДостоевск[а-я]{2,4}\b"
all_matches = re.findall(pattern, content)

unique_variants = list(set(all_matches))

print("Найденные уникальные варианты фамилии:")
for variant in unique_variants:
    print(variant)