# Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной
# нагрузки по кафедре. Таблица Дисциплины должна иметь следующую структуру записи:
# Код дисциплины, Наименование дисциплины, Специальность, Лекции (колич.часов),
# Практические (колич.часов), Лабораторные (колич.часов), Форма отчетности.

import sqlite3


def init_db():
    conn = sqlite3.connect("curriculum.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS disciplines (
            code INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            specialty TEXT NOT NULL,
            lectures_hours INTEGER NOT NULL,
            practical_hours INTEGER NOT NULL,
            lab_hours INTEGER NOT NULL,
            report_form TEXT NOT NULL
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM disciplines")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            (101, "Программирование", "Информатика", 36, 18, 18, "Экзамен"),
            (102, "Базы данных", "Информатика", 32, 16, 16, "Экзамен"),
            (103, "Высшая математика", "Экономика", 54, 36, 0, "Экзамен"),
            (104, "Операционные системы", "Информатика", 28, 0, 28, "Зачет"),
            (105, "Web-технологии", "Дизайн", 20, 20, 20, "Зачет"),
            (106, "Философия", "Юриспруденция", 32, 16, 0, "Зачет"),
            (107, "Компьютерная графика", "Дизайн", 24, 0, 24, "Экзамен"),
            (108, "Иностранный язык", "Экономика", 0, 54, 0, "Зачет"),
            (109, "Сети и телекоммуникации", "Информатика", 30, 15, 15, "Экзамен"),
            (110, "История", "Юриспруденция", 34, 16, 0, "Зачет")
        ]
        cursor.executemany("""
            INSERT INTO disciplines (code, name, specialty, lectures_hours, practical_hours, lab_hours, report_form)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, initial_data)
        conn.commit()
    
    conn.close()


def show_all():
    conn = sqlite3.connect("curriculum.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM disciplines")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


init_db()

print("Исходное состояние базы данных (10 позиций):")
show_all()
print("---")

conn = sqlite3.connect("curriculum.db")
cursor = conn.cursor()

# ПОИСК: Запрос 1 (Поиск дисциплин по конкретной специальности)
cursor.execute("SELECT * FROM disciplines WHERE specialty = 'Информатика'")
search_1 = cursor.fetchall()

# ПОИСК: Запрос 2 (Поиск дисциплин с формой отчетности 'Экзамен' и лекциями > 30 часов)
cursor.execute("SELECT * FROM disciplines WHERE report_form = 'Экзамен' AND lectures_hours > 30")
search_2 = cursor.fetchall()

# ПОИСК: Запрос 3 (Поиск дисциплин, где нет лабораторных занятий)
cursor.execute("SELECT * FROM disciplines WHERE lab_hours = 0")
search_3 = cursor.fetchall()

print("Результат поиска 1 (Специальность 'Информатика'):", search_1)
print("Результат поиска 2 (Экзамен и Лекции > 30ч):", search_2)
print("Результат поиска 3 (Без лабораторных):", search_3)
print("---")

# РЕДАКТИРОВАНИЕ: Запрос 1 (Изменение количества практических часов для конкретного кода)
cursor.execute("UPDATE disciplines SET practical_hours = 40 WHERE code = 103")

# РЕДАКТИРОВАНИЕ: Запрос 2 (Изменение формы отчетности для всех дисциплин дизайна)
cursor.execute("UPDATE disciplines SET report_form = 'Диф.зачет' WHERE specialty = 'Дизайн'")

# РЕДАКТИРОВАНИЕ: Запрос 3 (Увеличение лекционных часов на 2 для всех экзаменационных предметов)
cursor.execute("UPDATE disciplines SET lectures_hours = lectures_hours + 2 WHERE report_form = 'Экзамен'")

conn.commit()
print("База данных после выполнения 3 запросов редактирования:")
show_all()
print("---")

# УДАЛЕНИЕ: Запрос 1 (Удаление конкретной дисциплины по её коду)
cursor.execute("DELETE FROM disciplines WHERE code = 110")

# УДАЛЕНИЕ: Запрос 2 (Удаление дисциплин, где суммарно часов на лекции и практики меньше 40)
cursor.execute("DELETE FROM disciplines WHERE (lectures_hours + practical_hours) < 40")

# УДАЛЕНИЕ: Запрос 3 (Удаление дисциплин для специальности 'Юриспруденция')
cursor.execute("DELETE FROM disciplines WHERE specialty = 'Юриспруденция'")

conn.commit()
print("Результирующее состояние базы данных после выполнения 3 запросов удаления:")
show_all()

conn.close()