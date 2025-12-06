import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string

# необхідні пакети NLTK
nltk.download('gutenberg', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# Імпорт тексту та підрахунок слів
# Завантажуємо слова з тексту Біблії короля Якова
words = gutenberg.words('bible-kjv.txt')

# Визначаємо загальну кількість слів (токенів)
total_words = len(words)
print(f"Загальна кількість слів у тексті: {total_words}")


# КРОК 2: Топ-10 слів БЕЗ очищення
# Рахуємо частоту кожного слова
fdist_raw = FreqDist(words)
top_10_raw = fdist_raw.most_common(10)

print("\nТоп-10 найбільш вживаних слів до очищення:")
for word, frequency in top_10_raw:
    print(f"{word}: {frequency}")

# Побудова діаграми для неочищених даних
plt.figure(figsize=(10, 5))
words_raw, counts_raw = zip(*top_10_raw)
plt.bar(words_raw, counts_raw, color='skyblue')
plt.title('Топ-10 слів з пунктуацією та стоп-словами')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()


# Видалення стоп-слів та пунктуації
# Отримуємо список англійських стоп-слів
stop_words = set(stopwords.words('english'))

# Створюємо список пунктуації для видалення
punctuation = set(string.punctuation)

# Фільтруємо текст:
# 1. Приводимо до нижнього регістру (.lower())
# 2. Перевіряємо, чи слово не є стоп-словом
# 3. Перевіряємо, чи слово складається з літер (.isalpha()), щоб прибрати пунктуацію
clean_words = [
    w.lower() for w in words
    if w.lower() not in stop_words and w.isalpha()
]

print(f"\nКількість слів після очищення: {len(clean_words)}")


# Топ-10 слів ПІСЛЯ очищення
fdist_clean = FreqDist(clean_words)
top_10_clean = fdist_clean.most_common(10)

print("\nТоп-10 найбільш вживаних слів (після очищення):")
for word, frequency in top_10_clean:
    print(f"{word}: {frequency}")

# Побудова діаграми для очищених даних
plt.figure(figsize=(10, 5))
words_clean, counts_clean = zip(*top_10_clean)
plt.bar(words_clean, counts_clean, color='lightgreen')
plt.title('Топ-10 слів')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()

print("\ndone")