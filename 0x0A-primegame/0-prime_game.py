#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    # Step 1: Determine the maximum n we need to handle
    max_n = max(nums)
    
    # Step 2: Compute all primes up to max_n using Sieve of Eratosthenes
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    
    primes = [p for p in range(max_n + 1) if is_prime[p]]
    
    # Step 3: Play the game for each round and determine the winner
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n <= 1:
            # If n is 1 or less, Ben wins immediately because Maria cannot make a move
            ben_wins += 1
            continue
        
        # Create a DP array to determine if the current player can force a win
        dp = [False] * (n + 1)
        
        # Fill the DP array based on the available primes and optimal play
        for i in range(2, n + 1):
            if is_prime[i]:
                can_win = False
                for prime in primes:
                    if prime > i:
                        break
                    if i % prime == 0:
                        if not dp[i - prime]:
                            can_win = True
                            break
                dp[i] = can_win
        
        # Maria always starts first, so we check dp[n]
        if dp[n]:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
