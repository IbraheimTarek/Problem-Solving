def coin_change(coins, amount):
    # Write your plan below
    # Step 1: Initialize the dp array with an unreachable high value (infinity)
    # Step 2: Base case, 0 amount requires 0 coins
    # Step 3: Loop through each coin
    # Step 4: If dp[amount] is still infinity, it means it's impossible to make the amount

    # Write your code below
    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test Case 1: Example 1
print(coin_change([1, 2, 5], 11))  # Expected output: 3 (5 + 5 + 1)

# Test Case 2: Example 2
print(coin_change([2], 3))  # Expected output: -1 (it's impossible to sum to 3 using only denomination 2)

# Test Case 3: Example 3
print(coin_change([1], 0))  # Expected output: 0 (no coins are needed for amount 0)

# Additional Test Case 1
print(coin_change([1, 2, 5], 7))  # Expected output: 2 (5 + 2)

# Additional Test Case 2
print(coin_change([2, 5, 10], 27))  # Expected output: 4 (10 + 10 + 5 + 2)
