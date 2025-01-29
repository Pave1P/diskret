import math
def count_paths_combinations(n, m):
    return math.comb(n + m, n)
def count_paths_with_restriction(n, m):
    dp = [[[0] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1  # Начальная точка

    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0:
                dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
            if j > 0:
                dp[i][j][1] = dp[i][j - 1][0]

    return dp[n][m][0] + dp[n][m][1]

n, m = 18, 16
print("Кратчайшие пути без ограничений:", count_paths_combinations(n, m))
print("Кратчайшие пути с ограничением:", count_paths_with_restriction(n, m))
