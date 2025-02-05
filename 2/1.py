from math import factorial
# Количество каждой буквы
counts = {'A': 5, 'Б': 2, 'Р': 2, 'К': 1, 'Д': 1}
total = 0
# Перебираем все возможные комбинации
for a in range(min(5, counts['A']) + 1):
    for b in range(min(5 - a, counts['Б']) + 1):
        for r in range(min(5 - a - b, counts['Р']) + 1):
            for k in range(min(5 - a - b - r, counts['К']) + 1):
                d = 5 - a - b - r - k
                if d <= counts['Д']:
                    # Вычисляем количество перестановок для текущей комбинации
                    permutations = factorial(5) // (factorial(a) * factorial(b) * factorial(r) * factorial(k) * factorial(d))
                    total += permutations
print(total)
