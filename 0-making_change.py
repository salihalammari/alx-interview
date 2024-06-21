def makeChange(coins, total):
    if total < 0:
        return 0
    
    # Initialize a list to store minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0
    
    # Iterate through all coin denominations
    for coin in coins:
        # Update dp[j] for all j from coin to total
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    
    # If dp[total] is still float('inf'), return -1 (total cannot be formed)
    return dp[total] if dp[total] != float('inf') else -1
