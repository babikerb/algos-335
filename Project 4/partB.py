# Name: Babiker Babiker
# Email: bbabiker@csu.fullerton.edu
# Date: 4/25/2025
# Course: CPSC 335
# Part B - Dynamic Programming
def stock_maximization_dp(M, items):
    n = len(items)
    dp = [[0] * (M + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        stocks, value = items[i-1]
        for w in range(1, M + 1):
            if value > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-value] + stocks)

    w = M
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= items[i-1][1]
    
    return [dp[n][M], selected]