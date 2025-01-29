from itertools import permutations
from collections import Counter

# Исходное слово
word = "АБРАКАДАБРА"

# Подсчет количества каждой буквы
letter_counts = Counter(word)

# Функция для проверки, можно ли составить слово из заданных букв
def is_valid_combination(combination, letter_counts):
    combo_counts = Counter(combination)
    for letter in combo_counts:
        if combo_counts[letter] > letter_counts[letter]:
            return False
    return True

# Генерация всех уникальных комбинаций из 5 букв
unique_combinations = set()
for combo in permutations(word, 5):
    if is_valid_combination(combo, letter_counts):
        unique_combinations.add(combo)

# Вывод количества уникальных слов
print(f"Количество различных слов из 5 букв: {len(unique_combinations)}")