import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import csv
# Математична модель
def fuel_consumption(speed):
 # Cпоживання палива залежно від швидкості.
 # Базове споживання 5л + опір
    return 5 + 0.001 * (speed ** 2)
def total_cost_func(speed, distance, driver_wage, fuel_price):
# speed: швидкість (км/год)
# distance: відстань (км)
# driver_wage: оплата водія ($/год)
# fuel_price: ціна палива ($/л)
    if speed <= 0: return float('inf')
    time = distance / speed
    wage_cost = time * driver_wage
    fuel_needed = (distance / 100) * fuel_consumption(speed)
    fuel_cost = fuel_needed * fuel_price

    return wage_cost + fuel_cost
# Структура взаємодії з користувачем + валідація
def get_user_parameters():

    print("\n--- Введення параметрів маршруту ---")
    while True:
        try:
            dist = float(input("Введіть відстань маршруту (км): "))
            wage = float(input("Введіть погодинну оплату водія ($/год): "))
            fuel = float(input("Введіть вартість палива ($/л): "))

            # валідація
            if dist <= 0 or wage < 0 or fuel <= 0:
                raise ValueError("Значення повинні бути додатними.")

            return dist, wage, fuel
        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, введіть коректні числа.")
# Збереження результатів
def save_results(speed_range, cost_range, optimal_speed, min_cost, filename="logistic_report"):

    # Збереження CSV
    csv_file = f"{filename}.csv"
    try:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Speed (km/h)", "Total Cost ($)"])  # Заголовок

            # Записуємо дані, які згенерували
            for s, c in zip(speed_range, cost_range):
                writer.writerow([f"{s:.1f}", f"{c:.2f}"])
            # Додаємо окремий рядок з результатом
            writer.writerow([])
            writer.writerow(["OPTIMAL SPEED", f"{optimal_speed:.2f}"])
            writer.writerow(["MIN COST", f"{min_cost:.2f}"])
        print(f"Таблицю збережено у: {csv_file}")
    except IOError as e:
        print(f"Помилка запису файлу: {e}")

    # 2. Збереження зображення
    png_file = f"{filename}.png"
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(speed_range, cost_range, label='Функція витрат', color='blue')
        plt.scatter(optimal_speed, min_cost, color='red', s=100, label=f'Оптимум ({optimal_speed:.1f} км/год)',
                    zorder=5)
        plt.title('Залежність витрат від швидкості доставки')
        plt.xlabel('Швидкість (км/год)')
        plt.ylabel('Загальні витрати ($)')
        plt.grid(True, linestyle='--')
        plt.legend()

        plt.savefig(png_file)
        print(f"Графік збережено у: {png_file}")
        plt.close()
    except Exception as e:
        print(f"Помилка побудови графіка: {e}")

#  Логіка програми

def main():
    print("Система оптимізації логістики")
    # Отримання даних
    try:
        dist, wage, price = get_user_parameters()
    except KeyboardInterrupt:
        print("\nРоботу перервано.")
        return
    print("\nВиконується розрахунок оптимальної швидкості...")
    try:
        # Використання оптимізації
        # minimize_scalar шукає мінімум функції в заданому діапазоні
        result = minimize_scalar(
            total_cost_func,
            bounds=(10, 150),  # Шукаємо швидкість від 10 до 150 км/год
            args=(dist, wage, price),
            method='bounded'
        )
        if result.success:
            opt_speed = result.x
            min_cost = result.fun
            print(f"\n--------- Результат аналізу ---------")
            print(f"Оптимальна швидкість: {opt_speed:.2f} км/год")
            print(f"Мінімальні витрати:   ${min_cost:.2f}")
        else:
            raise RuntimeError("Не вдалося знайти оптимум.")
        # Підготовка даних для візуалізації та звіту
        # Генеруємо масив швидкостей для побудови гладкої кривої
        speeds = np.linspace(20, 140, 100)
        # Розраховуємо витрати для кожної точки
        costs = [total_cost_func(s, dist, wage, price) for s in speeds]
        # Збереження результатів
        save_results(speeds, costs, opt_speed, min_cost)
    except Exception as e:
        print(f"Критична помилка під час обробки: {e}")
    print("\nПрограму завершено")
if __name__ == "__main__":
    main()