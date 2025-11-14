import matplotlib.pyplot as plt
import numpy as np

# Дані
years = np.arange(2003, 2023)

# Умовні дані
ukraine = [4.1, 4.0, 3.8, 3.5, 3.4, 3.1, 2.9, 2.5, 2.2, 1.9, 1.7, 1.6, 1.5, 1.5, 1.4, 1.3, 1.2, 1.2, 1.1, 1.1]
usa =     [1.7, 1.8, 1.7, 1.5, 1.6, 1.5, 1.4, 1.4, 1.3, 1.3, 1.2, 1.1, 1.1, 1.0, 1.0, 1.0, 0.9, 0.8, 0.8, 0.7]


# 2.1 Лінійні графіки для двох країн

plt.figure(figsize=(12, 6))

plt.plot(years, ukraine, label="Ukraine", linewidth=2, marker="o")
plt.plot(years, usa, label="USA", linewidth=2, marker="o")

plt.xlabel("Year")
plt.ylabel("Children out of school (%)")
plt.title("Dynamics of 'Children out of school, primary' (2003–2022)")
plt.grid(True)
plt.legend()
plt.show()

# 2.2 Стовпчаста діаграма країна вводиться користувачем

country = input("Enter country (Ukraine or USA): ")

if country.lower() == "ukraine":
    data = ukraine
elif country.lower() == "usa":
    data = usa
else:
    print("Incorrect country name! Use 'Ukraine' or 'USA'")
    exit()

plt.figure(figsize=(12, 6))
plt.bar(years, data)

plt.xlabel("Year")
plt.ylabel("Children out of school (%)")
plt.title(f"Bar chart for {country}")
plt.grid(axis='y')
plt.show()