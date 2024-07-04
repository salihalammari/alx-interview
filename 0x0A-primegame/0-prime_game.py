#!/usr/bin/python3
"""Module defining isWinner function."""


def sieve_of_eratosthenes(max_num):
    """ Return a list of primes up to max_num (inclusive) """
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    p = 2
    while (p * p <= max_num):
        if (sieve[p] == True):
            # Updating all multiples of p to not prime
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1
    primes = []
    for p in range(max_num + 1):
        if sieve[p]:
            primes.append(p)
    return primes


def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins_count = 0
    ben_wins_count = 0
    
    for n in nums:
        if n == 1:
            ben_wins_count += 1
            continue
        
        rounds_set = list(range(1, n + 1))
        is_maria_turn = True
        
        while True:
            if not any(rounds_set):
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break
            
            available_primes = [p for p in primes if p in rounds_set]
            
            if not available_primes:
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break
            
            chosen_prime = available_primes[0]
            rounds_set = [x for x in rounds_set if x % chosen_prime != 0]
            
            is_maria_turn = not is_maria_turn
    
    if maria_wins_count > ben_wins_count:
        return "Winner: Maria"
    elif ben_wins_count > maria_wins_count:
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
