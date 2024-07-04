#!/usr/bin/python3
"""Module for Prime Game"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def simulate_round(nums):
    """Simulate one round of the game."""
    # Check if the first number is prime
    if is_prime(nums[0]):
        # Maria starts with an advantage
        while len(nums) > 1:
            prime_num = next((num for num in nums if is_prime(num)), None)
            if prime_num is None:
                break
            nums.remove(prime_num)
            nums = [num for num in nums if num % prime_num != 0]
    else:
        # Ben starts with an advantage
        while len(nums) > 1:
            prime_num = next((num for num in nums if is_prime(num)), None)
            if prime_num is None:
                break
            nums.remove(prime_num)
            nums = [num for num in nums if num % prime_num != 0]

    # Determine the winner of the round
    if len(nums) == 1:
        return "Maria" if is_prime(nums[0]) else "Ben"
    else:
        return None

def isWinner(x, nums):
    """Determine the winner of the game."""
    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        result = simulate_round(nums[:])
        if result == "Maria":
            maria_wins += 1
        elif result == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

