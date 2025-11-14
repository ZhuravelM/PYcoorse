import json
from datetime import datetime

json_file = "students.json"
output_file = "birthday_result.json"

# Початкові дані
students_data = [
    {"surname": "Іваненко", "name": "Олександр", "patronymic": "Петрович", "dob": "2005-03-12", "gender": "ч"},
    {"surname": "Петренко", "name": "Марія", "patronymic": "Іванівна", "dob": "2006-07-25", "gender": "ж"},
    {"surname": "Сидоренко", "name": "Віктор", "patronymic": "Михайлович", "dob": "2005-03-08", "gender": "ч"},
    {"surname": "Коваль", "name": "Анна", "patronymic": "Олександрівна", "dob": "2007-11-30", "gender": "ж"},
    {"surname": "Бондар", "name": "Ігор", "patronymic": "Сергійович", "dob": "2005-05-19", "gender": "ч"},
    {"surname": "Гончар", "name": "Наталія", "patronymic": "Вікторівна", "dob": "2006-12-03", "gender": "ж"},
    {"surname": "Ткаченко", "name": "Олег", "patronymic": "Петрович", "dob": "2005-03-22", "gender": "ч"},
    {"surname": "Кравець", "name": "Юлія", "patronymic": "Ігорівна", "dob": "2006-09-14", "gender": "ж"},
    {"surname": "Мельник", "name": "Дмитро", "patronymic": "Володимирович", "dob": "2007-07-07", "gender": "ч"},
    {"surname": "Шевченко", "name": "Оксана", "patronymic": "Петрівна", "dob": "2005-03-02", "gender": "ж"},
]

# збереження даних у JSON
def save_json(data, filename=json_file):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# завантаження даних із JSON
def load_json(filename=json_file):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не знайдено. Створюємо новий файл із початковими даними.")
        save_json(students_data)
        return students_data

# виведення на екран
def display_students(data):
    for student in data:
        print(f"{student['surname']} {student['name']} {student['patronymic']}, DOB: {student['dob']}, Gender: {student['gender']}")

# додавання нового учня
def add_student():
    surname = input("Прізвище: ")
    name = input("Ім'я: ")
    patronymic = input("По батькові: ")
    dob = input("Дата народження (рррр-мм-дд): ")
    gender = input("Стать (ч/ж): ")
    data = load_json()
    data.append({"surname": surname, "name": name, "patronymic": patronymic, "dob": dob, "gender": gender})
    save_json(data)
    print("Учень доданий.")

# видалення учня за прізвищем та ім'ям
def remove_student():
    surname = input("Прізвище учня для видалення: ")
    name = input("Ім'я учня для видалення: ")
    data = load_json()
    new_data = [s for s in data if not (s['surname'] == surname and s['name'] == name)]
    save_json(new_data)
    print("Учень видалений (якщо такий був).")

# пошук за полем
def search_student():
    field = input("Поле для пошуку (surname, name, patronymic, dob, gender): ")
    value = input(f"Значення для {field}: ")
    data = load_json()
    results = [s for s in data if s.get(field) == value]
    if results:
        print("Знайдено учнів:")
        display_students(results)
    else:
        print("Учнів не знайдено.")

# учні, що народилися у вказаному місяці
def birthday_in_month():
    month = int(input("Введіть номер місяця (1-12): "))
    data = load_json()
    results = []
    for s in data:
        try:
            dob = datetime.strptime(s['dob'], "%Y-%m-%d")
            if dob.month == month:
                results.append({"name": s['name'], "surname": s['surname']})
        except:
            continue
    if results:
        print("Учні, що народилися у цьому місяці:")
        for r in results:
            print(f"{r['name']} {r['surname']}")
    else:
        print("Учнів у цьому місяці немає.")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print(f"Результат збережено у файл '{output_file}'")

# меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Показати всіх учнів")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Пошук учня за полем")
        print("5. Учні, що народилися у вказаному місяці")
        print("0. Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            display_students(load_json())
        elif choice == "2":
            add_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            birthday_in_month()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    save_json(students_data)  # файл із початковими даними
    menu()
