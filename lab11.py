import pandas as pd

# Початковий словник з ПР №5
students = {
    "Іванов Іван Іванович": {"year": 2007, "month": 5, "day": 12},
    "Петров Петро Петрович": {"year": 2006, "month": 11, "day": 3},
    "Сидоренко Олег Андрійович": {"year": 2007, "month": 1, "day": 25},
    "Коваленко Марія Сергіївна": {"year": 2006, "month": 7, "day": 14},
    "Петров Андрій Анатолійович": {"year": 2006, "month": 11, "day": 13},
}

# Додаємо нові записи
students["Тарасенко Юлія Володимирівна"] = {"year": 2007, "month": 12, "day": 30}
students["Мельник Андрій Олександрович"] = {"year": 2006, "month": 2, "day": 17}

# Додаємо додатковий стовпець оцінка
grades = [10, 8, 11, 12, 9, 10, 7]

# Перетворюємо словник у DataFrame
df = pd.DataFrame.from_dict(students, orient='index')

# Додаємо стовпець
df["grade"] = grades

# Створюємо новий обчислювальний стовпець (наприклад, вік)
df["age"] = 2025 - df["year"]

# БАЗОВИЙ АНАЛІЗ
print("\n=== Перші 3 рядки ===")
print(df.head(3))

print("\n=== Типи даних ===")
print(df.dtypes)

print("\n=== Розмір таблиці (рядки, стовпці) ===")
print(df.shape)

print("\n=== Описова статистика ===")
print(df.describe())

# ФІЛЬТРАЦІЯ учнів старших 18 років

filtered = df[df["age"] > 18]
print("\n=== Учні старші 18 років ===")
print(filtered)

# СОРТУВАННЯ за спаданням успішності
sorted_df = df.sort_values(by="grade", ascending=False)
print("\n=== Сортування за успішністю ===")
print(sorted_df)

# ГРУПУВАННЯ середній бал по року народження
grouped = df.groupby("year")["grade"].mean()
print("\n=== Середній бал по роках народження ===")
print(grouped)

# ДОДАТКОВІ АГРЕГАЦІЇ
# Максимальна оцінка у кожному році
max_grade = df.groupby("year")["grade"].max()
print("\n=== Максимальна оцінка по роках ===")
print(max_grade)

# Кількість унікальних років народження
unique_years = df["year"].nunique()
print("\n=== Кількість унікальних років народження ===")
print(unique_years)
