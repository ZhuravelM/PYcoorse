from datetime import date
# ---------------  словник ------------
students = {
    "Білоус Артем Олегович": {"year": 2007, "month": 1, "day": 12},
    "Кравчук Дарина Ігорівна": {"year": 2008, "month": 3, "day": 27},
    "Семенюк Владислав Петрович": {"year": 2007, "month": 5, "day": 9},
    "Литвин Анастасія Сергіївна": {"year": 2007, "month": 6, "day": 14},
    "Мазур Денис Андрійович": {"year": 2008, "month": 7, "day": 22},
    "Гордієнко Катерина Миколаївна": {"year": 2007, "month": 9, "day": 30},
    "Онищенко Дмитро Валерійович": {"year": 2007, "month": 10, "day": 11},
    "Шевчук Марія Олександрівна": {"year": 2007, "month": 11, "day": 4},
    "Руденко Олексій Володимирович": {"year": 2008, "month": 12, "day": 18},
    "Тимчук Софія Романівна": {"year": 2007, "month": 2, "day": 25}
}
# ---------  виведення на екран всіх значень словника ---------
def print_all(students):
    print("\n============ Всі учні ============")
    for name, data in students.items():
        print(f"{name} — дата народження: {data['day']:02d}.{data['month']:02d}.{data['year']}")
# --------- додавання учня ---------
def add_student(students):
    try:
        name = input("Введіть ПІБ учня: ")
        year = int(input("Рік народження: "))
        month = int(input("Місяць народження (1–12): "))
        day = int(input("День народження: "))
        students[name] = {"year": year, "month": month, "day": day}
        print(f"Учня '{name}' додано до словника.")
    except ValueError:
        print("Помилка: потрібно вводити числа для дати.")

# --------- видалення учня ---------
def delete_student(students):
    name = input("Введіть ПІБ учня, якого треба видалити: ")
    try:
        del students[name]
        print(f"Учня '{name}' видалено.")
    except KeyError:
        print("Такого учня немає у словнику.")

# --------- перегляд вмісту словника за відсортованими ключами ---------
def print_sorted(students):
    print("\n=== Учні у відсортованому порядку ===")
    for name in sorted(students.keys()):
        data = students[name]
        print(f"{name} — дата народження: {data['day']:02d}.{data['month']:02d}.{data['year']}")

# --------- Варіант 4 - перевірка, у кого сьогодні день народження ------------
def check_birthdays(students):
    today = date.today()
    found = False
    print("\n============ Перевірка днів народження ============")
    for name, data in students.items():
        if data["day"] == today.day and data["month"] == today.month:
            print(f"Сьогодні день народження у: {name}")
            found = True
    if not found:
        print("Сьогодні немає іменинників.")

# --------- Меню ---------
def menu():
    while True:
        print("""
1 — Вивести всі записи
2 — Додати нового учня
3 — Видалити учня
4 — Вивести за відсортованими ключами
5 — Перевірити, у кого сьогодні день народження
0 — Вихід
""")
        choice = input("Вибір: ")

        if choice == "1":
            print_all(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            print_sorted(students)
        elif choice == "5":
            check_birthdays(students)
        elif choice == "0":
            print("Програму завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

menu()
