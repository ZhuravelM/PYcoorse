import json
import matplotlib.pyplot as plt

# JSON-дані
students = [
    {"surname": "Іваненко", "name": "Олександр", "patronymic": "Петрович", "dob": "2005-03-12", "gender": "ч"},
    {"surname": "Петренко", "name": "Марія", "patronymic": "Іванівна", "dob": "2006-07-25", "gender": "ж"},
    {"surname": "Сидоренко", "name": "Віктор", "patronymic": "Михайлович", "dob": "2005-03-08", "gender": "ч"},
    {"surname": "Коваль", "name": "Анна", "patronymic": "Олександрівна", "dob": "2007-11-30", "gender": "ж"},
    {"surname": "Бондар", "name": "Ігор", "patronymic": "Сергійович", "dob": "2005-05-19", "gender": "ч"},
    {"surname": "Гончар", "name": "Наталія", "patronymic": "Вікторівна", "dob": "2006-12-03", "gender": "ж"},
    {"surname": "Ткаченко", "name": "Олег", "patronymic": "Петрович", "dob": "2005-03-22", "gender": "ч"},
    {"surname": "Кравець", "name": "Юлія", "patronymic": "Ігорівна", "dob": "2006-09-14", "gender": "ж"},
    {"surname": "Мельник", "name": "Дмитро", "patronymic": "Володимирович", "dob": "2007-07-07", "gender": "ч"},
    {"surname": "Шевченко", "name": "Оксана", "patronymic": "Петрівна", "dob": "2005-03-02", "gender": "ж"}
]

# Підрахунок
boys = sum(1 for s in students if s["gender"] == "ч")
girls = sum(1 for s in students if s["gender"] == "ж")

values = [boys, girls]
labels = ["Хлопці", "Дівчата"]

# Кольори секторів
colors = ["skyblue", "lightcoral"]

# Побудова кругової діаграми
plt.figure(figsize=(7, 7))
plt.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Розподіл учнів за статтю")
plt.show()
