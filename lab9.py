import pandas as pd

input_file = "API_NY.GDP.PCAP.CD_DS2_en_csv_v2_134819.csv"
output_file = "gdp_per_capita_ukraine_summary.csv"

try:
    df = pd.read_csv(input_file, skiprows=4)
except FileNotFoundError:
    print(f"Файл '{input_file}' не знайдено. Перевірте шлях і назву файлу.")
    exit()
except Exception as e:
    print(f"Сталася помилка при відкритті файлу: {e}")
    exit()

ukraine_data = df[df['Country Name'] == 'Ukraine']

if ukraine_data.empty:
    print("Дані для України не знайдено.")
    exit()

# GDP per capita 1991-2019
years = list(map(str, range(1991, 2020)))
gdp_values = ukraine_data[years].values.flatten()

print("Дані GDP per capita для України (1991-2019):")
for year, value in zip(years, gdp_values):
    print(f"{year}: {value}")

# Мін і макс значення
min_gdp = min(gdp_values)
max_gdp = max(gdp_values)
min_year = years[gdp_values.tolist().index(min_gdp)]
max_year = years[gdp_values.tolist().index(max_gdp)]

print(f"\nМінімальне GDP per capita: {min_gdp} у {min_year} році")
print(f"Максимальне GDP per capita: {max_gdp} у {max_year} році")

summary_df = pd.DataFrame({
    'Indicator': ['GDP per capita (current US$) - Min', 'GDP per capita (current US$) - Max'],
    'Year': [min_year, max_year],
    'Value': [min_gdp, max_gdp]
})
summary_df.to_csv(output_file, index=False)
print(f"\nРезультати збережено у файл '{output_file}'")
