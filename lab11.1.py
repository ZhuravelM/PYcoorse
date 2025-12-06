import pandas as pd
import matplotlib.pyplot as plt

# Завантаження CSV
df = pd.read_csv("comptagevelo2012.csv")

# fix
df.rename(columns={"Unnamed: 1": "Time"}, inplace=True)

#  Перетворюємо Date + Time у datetime
df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"], dayfirst=True)

# Виділяємо дату та місяць
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Month"] = df["Date"].dt.month

# Перетворюємо всі числові стовпці у числа
for col in df.columns[2:-1]:   # - Date, Time, DateTime, Month
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\n=== Перші 5 рядків ===")
print(df.head())

print("\n=== Інформація про DataFrame ===")
print(df.info())

print("\n=== Описова статистика ===")
print(df.describe())

# Загальна кількість велосипедистів за рік
total_year = df.iloc[:, 2:-1].sum().sum()
print("\n=== Загальна кількість велосипедистів за рік ===")
print(total_year)

#  Кількість по кожній велодоріжці
total_per_track = df.iloc[:, 2:-1].sum()
print("\n=== Кількість велосипедистів за рік по кожній доріжці ===")
print(total_per_track)

#  найпопулярніший місяць
tracks = df.columns[2:5]

print("\n=== Найпопулярніший місяць для трьох доріжок ===")
for track in tracks:
    best_month = df.groupby("Month")[track].sum().idxmax()
    print(f"{track}: місяць {best_month}")

# Побудова графіка
# DateTime -> індекс
df.set_index("DateTime", inplace=True)

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 10)

df.iloc[:, 1:-1].plot()  # 1:-1 -Date -Month
plt.title("Кількість велосипедистів по велодоріжках (2012)")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.legend(title="Велодоріжки", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
