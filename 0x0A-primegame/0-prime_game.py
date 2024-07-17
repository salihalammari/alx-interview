#!/usr/bin/python3
"""Module defining isWinner function."""



def isWinner(x, nums):
    """Function to determine the winner in the prime game."""
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while primesSet:
            smallestPrime = primesSet.pop(0)
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]
            isMariaTurns = not isMariaTurns

        if isMariaTurns:
            mariaWinsCount += 1
        else:
            benWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"
    elif benWinsCount > mariaWinsCount:
        return "Winner: Ben"
    else:
        return None

def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
