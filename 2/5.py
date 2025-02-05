def count_paths(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m][n]

def count_paths_no_consecutive_vertical(m, n):
    dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0][0] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0:
                dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][1]
            if j > 0:
                dp[i][j][1] += dp[i][j - 1][0]
    return dp[m][n][0] + dp[m][n][1]

# Решение для сетки 18x16
m, n = 18, 16
print("Количество путей без ограничений:", count_paths(m, n))
print("Количество путей с ограничением на два вертикальных участка подряд:", count_paths_no_consecutive_vertical(m, n))
