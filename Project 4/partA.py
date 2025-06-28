# Name: Babiker Babiker
# Email: bbabiker@csu.fullerton.edu
# Date: 4/25/2025
# Course: CPSC 335
# Part A - Exhaustive Search
def stock_maximization_exhaustive(M, items):
    max_stocks = 0
    best_combo = []
    n = len(items)

    for mask in range(1, 1 << n):
        current_combo = []
        total_value = 0
        total_stocks = 0
        
        for i in range(n):
            if mask & (1 << i):
                current_combo.append(i)
                total_value += items[i][1]
                total_stocks += items[i][0]
        
        if total_value <= M and total_stocks > max_stocks:
            max_stocks = total_stocks
            best_combo = current_combo
    
    return [max_stocks, best_combo]