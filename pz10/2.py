# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно
# поставив последнюю строку фразой введённой пользователем.

input_file = "text18-9.txt"
output_file = "text18-9_result.txt"

for encoding in ("utf-16", "utf-8-sig", "cp1251", "latin-1"):
    try:
        with open(input_file, "r", encoding=encoding) as f:
            content = f.read()
        break
    except (UnicodeDecodeError, UnicodeError):
        continue

print("Содержимое файла:")
print(content)

lowercase_count = sum(1 for c in content if c.islower())
print(f"Количество букв в нижнем регистре: {lowercase_count}")

user_phrase = input("Введите фразу для последней строки: ")

lines = content.strip().split("\n")
lines.append(user_phrase)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("\nНовый файл сформирован:")
print("\n".join(lines))